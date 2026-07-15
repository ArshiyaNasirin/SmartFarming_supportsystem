from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
TEMPLATES_DIR = PROJECT_ROOT / "templates"
STATIC_DIR = PROJECT_ROOT / "static"

DATASET_FILE = DATA_DIR / "crop_recommendation_dataset.csv"
MODEL_FILE = MODELS_DIR / "crop_recommender_pipeline.joblib"
METRICS_FILE = MODELS_DIR / "training_metrics.json"
CLASSIFICATION_REPORT_FILE = REPORTS_DIR / "classification_report.txt"
FEATURE_IMPORTANCE_FILE = REPORTS_DIR / "feature_importance.csv"
FEATURE_IMPORTANCE_PLOT = REPORTS_DIR / "feature_importance.png"
CONFUSION_MATRIX_FILE = REPORTS_DIR / "confusion_matrix.csv"
CONFUSION_MATRIX_PLOT = REPORTS_DIR / "confusion_matrix.png"

TARGET_COLUMN = "crop_label"
RECORD_ID_COLUMN = "record_id"

RANDOM_STATE = 42
