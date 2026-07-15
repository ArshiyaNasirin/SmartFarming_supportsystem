from __future__ import annotations

from functools import lru_cache
from typing import Any

import pandas as pd

from src.config import MODEL_FILE
from src.crop_profiles import CROP_PROFILES
from src.modeling import load_trained_pipeline
from src.schema import DEFAULT_INPUT_VALUES, FIELD_DEFINITIONS, FEATURE_COLUMNS


NUMERIC_CORRECTION_MAP = {
    "nitrogen_kg_ha": "Urea",
    "phosphorus_kg_ha": "DAP",
    "potassium_kg_ha": "MOP",
}


@lru_cache(maxsize=1)
def get_model():
    if not MODEL_FILE.exists():
        raise FileNotFoundError(
            "Model artifact is missing. Run src/train_model.py before starting the Flask app."
        )
    return load_trained_pipeline(MODEL_FILE)


def coerce_payload(payload: dict[str, Any]) -> dict[str, Any]:
    cleaned: dict[str, Any] = {}
    for field_name in FEATURE_COLUMNS:
        definition = FIELD_DEFINITIONS[field_name]
        raw_value = payload.get(field_name, definition["default"])
        if definition["kind"] == "number":
            try:
                value = float(raw_value)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{definition['label']} must be a number.") from exc
            minimum = float(definition["min"])
            maximum = float(definition["max"])
            if value < minimum or value > maximum:
                raise ValueError(
                    f"{definition['label']} must be between {minimum} and {maximum}."
                )
            cleaned[field_name] = round(value, 2)
        else:
            options = tuple(definition["options"])
            if raw_value not in options:
                raise ValueError(f"{definition['label']} must be one of the available options.")
            cleaned[field_name] = str(raw_value)
    return cleaned


def _tokenize_fertilizer(plan: str) -> list[str]:
    tokens: list[str] = []
    for chunk in plan.replace(" and ", " + ").split("+"):
        token = chunk.strip()
        if token and token not in tokens:
            tokens.append(token)
    return tokens


def recommend_fertilizer(features: dict[str, Any], crop: str) -> tuple[str, list[str], list[str]]:
    profile = CROP_PROFILES[crop]
    fertilizer_tokens = _tokenize_fertilizer(profile.base_fertilizer)
    caution_notes: list[str] = []
    matches: list[str] = []

    comparisons = [
        ("nitrogen_kg_ha", "Nitrogen", profile.nitrogen),
        ("phosphorus_kg_ha", "Phosphorus", profile.phosphorus),
        ("potassium_kg_ha", "Potassium", profile.potassium),
        ("temperature_c", "Temperature", profile.temperature),
        ("humidity_pct", "Humidity", profile.humidity),
        ("soil_ph", "Soil pH", profile.soil_ph),
        ("rainfall_mm", "Rainfall", profile.rainfall),
        ("soil_moisture_pct", "Soil moisture", profile.soil_moisture),
        ("organic_matter_pct", "Organic matter", profile.organic_matter),
        ("sunlight_hours", "Sunlight", profile.sunlight_hours),
        ("altitude_m", "Altitude", profile.altitude),
    ]

    for field_name, label, bounds in comparisons:
        value = float(features[field_name])
        low, high = bounds
        if low <= value <= high:
            matches.append(f"{label} is within the preferred range for {crop}.")
        elif value < low:
            caution_notes.append(
                f"{label} is {round(low - value, 2)} below the preferred band for {crop}."
            )
            correction = NUMERIC_CORRECTION_MAP.get(field_name)
            if correction and correction not in fertilizer_tokens:
                fertilizer_tokens.append(correction)
        else:
            caution_notes.append(
                f"{label} is {round(value - high, 2)} above the preferred band for {crop}."
            )

    if features["soil_type"] in profile.soil_types:
        matches.append(f"Soil type {features['soil_type']} matches the crop profile.")
    else:
        caution_notes.append(
            f"Soil type {features['soil_type']} is less aligned with the profile for {crop}."
        )

    if features["region"] in profile.regions:
        matches.append(f"Region {features['region']} is suitable for {crop}.")
    else:
        caution_notes.append(
            f"Region {features['region']} is outside the most suitable zones for {crop}."
        )

    if features["season"] in profile.seasons:
        matches.append(f"The {features['season']} season aligns with {crop} cultivation.")
    else:
        caution_notes.append(
            f"Season {features['season']} is less ideal for {crop}."
        )

    if features["irrigation_method"] in profile.irrigation_methods:
        matches.append(f"{features['irrigation_method'].title()} irrigation suits {crop}.")
    else:
        caution_notes.append(
            f"Irrigation method {features['irrigation_method']} is not a primary match for {crop}."
        )

    fertilizer_plan = " + ".join(fertilizer_tokens)
    return fertilizer_plan, matches, caution_notes


def predict_recommendation(payload: dict[str, Any]) -> dict[str, Any]:
    cleaned = coerce_payload(payload)
    model = get_model()
    input_frame = pd.DataFrame([cleaned], columns=FEATURE_COLUMNS)

    predicted_crop = str(model.predict(input_frame)[0])
    probabilities = model.predict_proba(input_frame)[0]
    classes = model.named_steps["model"].classes_

    ranking = sorted(
        (
            {"crop": str(crop_name), "confidence_pct": round(float(probability) * 100.0, 2)}
            for crop_name, probability in zip(classes, probabilities)
        ),
        key=lambda item: item["confidence_pct"],
        reverse=True,
    )
    confidence = ranking[0]["confidence_pct"] if ranking else 0.0

    fertilizer, matches, cautions = recommend_fertilizer(cleaned, predicted_crop)

    return {
        "predicted_crop": predicted_crop,
        "confidence_pct": confidence,
        "top_predictions": ranking[:3],
        "fertilizer": fertilizer,
        "matched_conditions": matches[:6],
        "caution_conditions": cautions[:6],
        "input_values": cleaned,
        "crop_profile": {
            "soil_types": list(CROP_PROFILES[predicted_crop].soil_types),
            "regions": list(CROP_PROFILES[predicted_crop].regions),
            "seasons": list(CROP_PROFILES[predicted_crop].seasons),
            "irrigation_methods": list(CROP_PROFILES[predicted_crop].irrigation_methods),
            "base_fertilizer": CROP_PROFILES[predicted_crop].base_fertilizer,
        },
    }


def default_form_values() -> dict[str, Any]:
    return dict(DEFAULT_INPUT_VALUES)
