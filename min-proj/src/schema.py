from src.crop_profiles import IRRIGATION_OPTIONS, REGION_OPTIONS, REGION_STATE_MAP, SEASON_OPTIONS, SOIL_TYPES


STATE_OPTIONS = tuple(sorted({state for states in REGION_STATE_MAP.values() for state in states}))

FIELD_DEFINITIONS = {
    "nitrogen_kg_ha": {
        "label": "Nitrogen",
        "kind": "number",
        "unit": "kg/ha",
        "min": 0,
        "max": 200,
        "step": 1,
        "default": 85,
    },
    "phosphorus_kg_ha": {
        "label": "Phosphorus",
        "kind": "number",
        "unit": "kg/ha",
        "min": 0,
        "max": 120,
        "step": 1,
        "default": 48,
    },
    "potassium_kg_ha": {
        "label": "Potassium",
        "kind": "number",
        "unit": "kg/ha",
        "min": 0,
        "max": 180,
        "step": 1,
        "default": 55,
    },
    "temperature_c": {
        "label": "Temperature",
        "kind": "number",
        "unit": "\u00b0C",
        "min": 0,
        "max": 45,
        "step": 0.1,
        "default": 27,
    },
    "humidity_pct": {
        "label": "Humidity",
        "kind": "number",
        "unit": "%",
        "min": 0,
        "max": 100,
        "step": 0.1,
        "default": 68,
    },
    "soil_ph": {
        "label": "Soil pH",
        "kind": "number",
        "unit": "pH",
        "min": 4.0,
        "max": 9.0,
        "step": 0.1,
        "default": 6.8,
    },
    "rainfall_mm": {
        "label": "Rainfall",
        "kind": "number",
        "unit": "mm/year",
        "min": 0,
        "max": 3500,
        "step": 1,
        "default": 950,
    },
    "soil_moisture_pct": {
        "label": "Soil moisture",
        "kind": "number",
        "unit": "%",
        "min": 0,
        "max": 100,
        "step": 0.1,
        "default": 42,
    },
    "organic_matter_pct": {
        "label": "Organic matter",
        "kind": "number",
        "unit": "%",
        "min": 0,
        "max": 8,
        "step": 0.1,
        "default": 2.2,
    },
    "sunlight_hours": {
        "label": "Sunlight",
        "kind": "number",
        "unit": "hours/day",
        "min": 0,
        "max": 14,
        "step": 0.1,
        "default": 8.5,
    },
    "altitude_m": {
        "label": "Altitude",
        "kind": "number",
        "unit": "meters",
        "min": 0,
        "max": 3500,
        "step": 10,
        "default": 350,
    },
    "soil_type": {
        "label": "Soil type",
        "kind": "select",
        "options": SOIL_TYPES,
        "default": "loam",
    },
    "region": {
        "label": "Agro-climatic region",
        "kind": "select",
        "options": REGION_OPTIONS,
        "default": "central",
    },
    "state": {
        "label": "State",
        "kind": "select",
        "options": STATE_OPTIONS,
        "default": "Madhya Pradesh",
    },
    "season": {
        "label": "Season",
        "kind": "select",
        "options": SEASON_OPTIONS,
        "default": "kharif",
    },
    "irrigation_method": {
        "label": "Irrigation method",
        "kind": "select",
        "options": IRRIGATION_OPTIONS,
        "default": "canal",
    },
}

FORM_GROUPS = [
    {
        "title": "Soil nutrients",
        "description": "Core fertility indicators that influence crop suitability.",
        "fields": [
            "nitrogen_kg_ha",
            "phosphorus_kg_ha",
            "potassium_kg_ha",
            "soil_ph",
            "organic_matter_pct",
            "soil_moisture_pct",
        ],
    },
    {
        "title": "Weather profile",
        "description": "Climate inputs that shape growth potential and yield stability.",
        "fields": [
            "temperature_c",
            "humidity_pct",
            "rainfall_mm",
            "sunlight_hours",
            "altitude_m",
        ],
    },
    {
        "title": "Location and management",
        "description": "Geographic and field settings used for contextual recommendations.",
        "fields": [
            "soil_type",
            "region",
            "state",
            "season",
            "irrigation_method",
        ],
    },
]

DEFAULT_INPUT_VALUES = {name: definition["default"] for name, definition in FIELD_DEFINITIONS.items()}

NUMERIC_FEATURES = [
    "nitrogen_kg_ha",
    "phosphorus_kg_ha",
    "potassium_kg_ha",
    "temperature_c",
    "humidity_pct",
    "soil_ph",
    "rainfall_mm",
    "soil_moisture_pct",
    "organic_matter_pct",
    "sunlight_hours",
    "altitude_m",
]

CATEGORICAL_FEATURES = [
    "soil_type",
    "region",
    "state",
    "season",
    "irrigation_method",
]

FEATURE_COLUMNS = NUMERIC_FEATURES + CATEGORICAL_FEATURES
