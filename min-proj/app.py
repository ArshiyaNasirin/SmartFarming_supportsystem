from __future__ import annotations

import json

from flask import Flask, jsonify, render_template, request

from src.config import METRICS_FILE, MODEL_FILE
from src.crop_profiles import REGION_STATE_MAP
from src.recommendation import default_form_values, predict_recommendation
from src.schema import FIELD_DEFINITIONS, FORM_GROUPS


def _load_metrics() -> dict[str, object]:
    if METRICS_FILE.exists():
        return json.loads(METRICS_FILE.read_text(encoding="utf-8"))

    return {
        "records": 0,
        "classes": 0,
        "accuracy": 0.0,
        "cross_validation_accuracy_mean": 0.0,
        "cross_validation_accuracy_std": 0.0,
        "selected_feature_count": 0,
    }


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "smart-farming-decision-support"

    @app.context_processor
    def inject_globals() -> dict[str, object]:
        return {
            "field_definitions": FIELD_DEFINITIONS,
            "form_groups": FORM_GROUPS,
            "default_values": default_form_values(),
            "region_state_map": REGION_STATE_MAP,
            "model_stats": _load_metrics(),
        }

    @app.get("/")
    def index():
        return render_template(
            "index.html",
            title="Smart Farming Decision Support System",
            form_values=default_form_values(),
            error_message=None,
        )

    def _extract_form_payload(form_data) -> dict[str, object]:
        return {
            field_name: form_data.get(field_name, definition["default"])
            for field_name, definition in FIELD_DEFINITIONS.items()
        }

    @app.post("/predict")
    def predict():
        raw_payload = _extract_form_payload(request.form)
        try:
            result = predict_recommendation(raw_payload)
        except ValueError as exc:
            return (
                render_template(
                    "index.html",
                    title="Smart Farming Decision Support System",
                    form_values=raw_payload,
                    error_message=str(exc),
                ),
                400,
            )

        return render_template(
            "result.html",
            title="Recommendation Result",
            result=result,
        )

    @app.post("/api/predict")
    def api_predict():
        payload = request.get_json(silent=True) or {}
        result = predict_recommendation(payload)
        return jsonify(result)

    @app.get("/api/health")
    def health():
        return jsonify(
            {
                "status": "ok",
                "model_available": MODEL_FILE.exists(),
                "metrics_available": METRICS_FILE.exists(),
            }
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
