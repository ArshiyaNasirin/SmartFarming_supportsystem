from __future__ import annotations

import json
from pathlib import Path

import joblib
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectPercentile, mutual_info_classif
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from src.config import (
    CLASSIFICATION_REPORT_FILE,
    CONFUSION_MATRIX_FILE,
    CONFUSION_MATRIX_PLOT,
    DATASET_FILE,
    FEATURE_IMPORTANCE_FILE,
    FEATURE_IMPORTANCE_PLOT,
    METRICS_FILE,
    MODEL_FILE,
    RANDOM_STATE,
    RECORD_ID_COLUMN,
    REPORTS_DIR,
    TARGET_COLUMN,
)
from src.schema import CATEGORICAL_FEATURES, FEATURE_COLUMNS, NUMERIC_FEATURES


def build_pipeline() -> Pipeline:
    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
        ]
    )

    selector = SelectPercentile(score_func=mutual_info_classif, percentile=75)
    model = RandomForestClassifier(
        n_estimators=260,
        max_depth=14,
        min_samples_split=4,
        min_samples_leaf=2,
        class_weight="balanced_subsample",
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )

    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("select", selector),
            ("model", model),
        ]
    )


def _ensure_output_dirs() -> None:
    for directory in (MODEL_FILE.parent, REPORTS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def _build_feature_importance_table(pipeline: Pipeline) -> pd.DataFrame:
    preprocessor = pipeline.named_steps["preprocess"]
    selector = pipeline.named_steps["select"]
    model = pipeline.named_steps["model"]

    feature_names = np.array(preprocessor.get_feature_names_out())
    selected_mask = selector.get_support()
    selected_features = feature_names[selected_mask]
    importance_frame = pd.DataFrame(
        {
            "feature": selected_features,
            "importance": model.feature_importances_,
        }
    ).sort_values("importance", ascending=False)
    return importance_frame.reset_index(drop=True)


def _save_plots(feature_importance: pd.DataFrame, confusion: pd.DataFrame) -> None:
    plt.figure(figsize=(11, 7))
    top_features = feature_importance.head(12)
    sns.barplot(data=top_features, x="importance", y="feature", color="#2f6a50")
    plt.title("Top model features")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.savefig(FEATURE_IMPORTANCE_PLOT, dpi=220)
    plt.close()

    plt.figure(figsize=(11, 8))
    sns.heatmap(confusion, annot=False, cmap="Greens", cbar=True)
    plt.title("Confusion matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(CONFUSION_MATRIX_PLOT, dpi=220)
    plt.close()


def train_and_evaluate(dataset_path: Path = DATASET_FILE, model_path: Path = MODEL_FILE) -> dict[str, object]:
    _ensure_output_dirs()
    frame = pd.read_csv(dataset_path)

    features = frame[FEATURE_COLUMNS]
    target = frame[TARGET_COLUMN]

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=target,
    )

    pipeline = build_pipeline()

    cross_validator = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    cross_validation_scores = cross_val_score(
        pipeline,
        x_train,
        y_train,
        cv=cross_validator,
        scoring="accuracy",
        n_jobs=-1,
    )

    pipeline.fit(x_train, y_train)
    predictions = pipeline.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average="weighted", zero_division=0)
    recall = recall_score(y_test, predictions, average="weighted", zero_division=0)
    f1 = f1_score(y_test, predictions, average="weighted", zero_division=0)
    report_text = classification_report(y_test, predictions, zero_division=0)
    class_labels = sorted(target.unique())
    confusion = confusion_matrix(y_test, predictions, labels=class_labels)
    confusion_frame = pd.DataFrame(confusion, index=class_labels, columns=class_labels)

    feature_importance = _build_feature_importance_table(pipeline)

    joblib.dump(pipeline, model_path)
    feature_importance.to_csv(FEATURE_IMPORTANCE_FILE, index=False)
    confusion_frame.to_csv(CONFUSION_MATRIX_FILE)
    CLASSIFICATION_REPORT_FILE.write_text(report_text, encoding="utf-8")

    _save_plots(feature_importance, confusion_frame)

    metrics = {
        "records": int(len(frame)),
        "train_records": int(len(x_train)),
        "test_records": int(len(x_test)),
        "classes": int(target.nunique()),
        "accuracy": round(float(accuracy), 4),
        "precision_weighted": round(float(precision), 4),
        "recall_weighted": round(float(recall), 4),
        "f1_weighted": round(float(f1), 4),
        "cross_validation_accuracy_mean": round(float(cross_validation_scores.mean()), 4),
        "cross_validation_accuracy_std": round(float(cross_validation_scores.std()), 4),
        "top_features": feature_importance.head(10).round(4).to_dict(orient="records"),
        "selected_feature_count": int(len(feature_importance)),
    }

    METRICS_FILE.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


def load_trained_pipeline(model_path: Path = MODEL_FILE) -> Pipeline:
    return joblib.load(model_path)
