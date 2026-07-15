# Smart Farming Decision Support System - Complete Development Prompt

## Project Overview

Create a **Smart Farming Decision Support System** that recommends a suitable crop and fertilizer plan based on soil, weather, and location inputs. The system combines machine learning (Random Forest classifier) with rule-based reasoning to provide actionable agricultural guidance through a responsive Flask web interface and JSON API.

### Core Objectives
- Predict the most suitable crop from 16 crop classes based on soil nutrients, climate, and contextual variables
- Generate fertilizer recommendations with explanations of matched conditions and attention points
- Deliver a polished web interface for manual field input and results visualization
- Provide JSON API endpoints for programmatic access
- Achieve ~96% accuracy through robust preprocessing, feature selection, and model evaluation

---

## Technical Stack

### Backend
- **Framework**: Flask 3.0+ (Python web framework)
- **Model Training**: scikit-learn 1.5+ (RandomForest, preprocessing, feature selection)
- **Data Processing**: pandas 2.2+, numpy 2.0+
- **Model Serialization**: joblib 1.4+
- **Visualization**: matplotlib 3.8+, seaborn 0.13+ (for evaluation plots)
- **Reporting**: python-docx 1.1+ (optional: DOCX report generation)

### Frontend
- **Templating**: Jinja2 templates (HTML)
- **Styling**: Custom CSS with earth-tone color palette
- **Interactivity**: Vanilla JavaScript (region-to-state filtering)
- **Responsiveness**: Mobile-first CSS Grid and Flexbox

### Development & Deployment
- Python 3.10+
- Virtual environment (venv or equivalent)
- Development server: Flask built-in (debug mode during development)

---

## Project Structure

```
project-root/
├── app.py                          # Flask application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── data/
│   └── crop_recommendation_dataset.csv        # Synthetic training dataset (1,920 rows)
├── models/
│   ├── crop_recommender_pipeline.joblib       # Trained model artifact
│   └── training_metrics.json                  # Model performance metrics
├── reports/
│   ├── feature_importance.csv                 # Top features ranked by importance
│   ├── feature_importance.png                 # Bar chart of top 12 features
│   ├── confusion_matrix.csv                   # Confusion matrix for all crops
│   ├── confusion_matrix.png                   # Heatmap visualization
│   ├── classification_report.txt              # Class-wise precision/recall/F1
│   └── SmartFarmingDecisionSupportSystem_Report.md
├── src/
│   ├── __init__.py                            # Package marker
│   ├── config.py                              # Path constants and configuration
│   ├── schema.py                              # Field definitions and feature columns
│   ├── crop_profiles.py                       # Crop parameter profiles and data
│   ├── dataset_builder.py                     # Dataset generation logic
│   ├── generate_dataset.py                    # Script to create dataset
│   ├── modeling.py                            # Pipeline construction and training
│   ├── train_model.py                         # Script to train and evaluate model
│   └── recommendation.py                      # Inference and fertilizer logic
├── static/
│   ├── styles.css                             # Complete stylesheet
│   └── app.js                                 # Browser interactivity (region filtering)
├── templates/
│   ├── base.html                              # Base layout template
│   ├── index.html                             # Input form page
│   └── result.html                            # Recommendation result page
└── scripts/
    └── generate_smartfarming_report_docx.py   # DOCX report generator (optional)
```

---

## Frontend Specifications

### Design & Styling

#### Color Palette (CSS Variables)
```css
--bg: #f1ebdf                              /* Main background */
--bg-soft: #faf6ee                         /* Soft background */
--panel: rgba(255, 255, 255, 0.78)        /* Semi-transparent white panels */
--panel-strong: rgba(255, 255, 255, 0.92) /* Stronger panels */
--text: #203326                            /* Primary text (dark green) */
--muted: #617165                           /* Muted text */
--border: rgba(32, 51, 38, 0.12)          /* Subtle borders */
--green: #2f6a50                           /* Primary green */
--green-deep: #184934                      /* Deep green accents */
--olive: #6c8b47                           /* Olive green */
--gold: #c48b2f                            /* Gold accents */
--sand: #f0d8a0                            /* Sand color */
--shadow: 0 26px 60px rgba(25, 42, 31, 0.14) /* Subtle shadows */
```

#### Styling Features
- **Typography**: Georgia serif for headings, Trebuchet MS sans-serif for body text
- **Spacing**: 18-22px padding in panels, consistent gap spacing
- **Borders**: Subtle 1px borders with 24px border-radius on main components
- **Glassmorphism**: Semi-transparent panels with backdrop blur (18px) effect
- **Animations**: Smooth scroll behavior, backdrop filters for depth
- **Ambient Effects**: Two large blurred gradient circles in background (non-interactive)
- **Responsiveness**: Mobile-first design with CSS Grid for form layout

### Page Structure

#### Header (Sticky/Fixed)
- Brand mark: "SF" with text "Smart Farming" + subtitle "Decision support for crops and fertilizers"
- Navigation links: "Insights", "Predictor" (smooth scroll to sections)
- Styling: Panel background with shadow, centered layout

#### Index Page (index.html)

**Hero Section**
- Eyebrow text: "Crop intelligence platform"
- Headline: "Predict the most suitable crop and fertilizer plan from field conditions."
- Lead paragraph explaining the system
- Three highlight cards:
  1. **Model**: "Random Forest" with description "Selected because it handles mixed feature types and nonlinear agronomic relationships."
  2. **Training Data**: Display `{{ model_stats.records }}` records with `{{ model_stats.classes }}` crop classes
  3. **Validation**: Display accuracy percentage `{{ (model_stats.accuracy * 100) | round(1) }}%`

**Prediction Form** (id="predictor")
- Organized into three sections (fieldsets):

  **Section 1: Soil Nutrients**
  - Description: "Core fertility indicators that influence crop suitability."
  - Fields:
    - Nitrogen (kg/ha): number input, min=0, max=200, step=1, default=85
    - Phosphorus (kg/ha): number input, min=0, max=120, step=1, default=48
    - Potassium (kg/ha): number input, min=0, max=180, step=1, default=55
    - Soil pH: number input, min=4.0, max=9.0, step=0.1, default=6.8
    - Organic Matter (%): number input, min=0, max=8, step=0.1, default=2.2
    - Soil Moisture (%): number input, min=0, max=100, step=0.1, default=42

  **Section 2: Weather Profile**
  - Description: "Climate inputs that shape growth potential and yield stability."
  - Fields:
    - Temperature (°C): number input, min=0, max=45, step=0.1, default=27
    - Humidity (%): number input, min=0, max=100, step=0.1, default=68
    - Rainfall (mm/year): number input, min=0, max=3500, step=1, default=950
    - Sunlight (hours/day): number input, min=0, max=14, step=0.1, default=8.5
    - Altitude (meters): number input, min=0, max=3500, step=10, default=350

  **Section 3: Location and Management**
  - Description: "Geographic and field settings used for contextual recommendations."
  - Fields:
    - Soil Type: select dropdown (options: alluvial, black, clay, laterite, loam, red, sandy_loam, silty_loam), default=loam
    - Agro-climatic Region: select dropdown, default=central
    - State: select dropdown (dynamically filtered by region), default=Madhya Pradesh
    - Season: select dropdown (kharif, rabi, zaid, perennial), default=kharif
    - Irrigation Method: select dropdown (rainfed, canal, drip, sprinkler, flood), default=canal

- Submit button: "Generate recommendation" (primary button styling)
- Error handling: Display error message banner if form validation fails
- JavaScript enhancement: Dynamic region → state filtering updates state options based on selected region

**Insights Section** (id="insights")
- Three insight cards describing:
  1. **Feature Selection**: "Relevant variables are retained before classification. The pipeline keeps the most informative encoded and numeric features so the model stays compact and focused."
  2. **Output**: "Crop choice plus fertilizer guidance. The response includes the recommended crop, a fertilizer plan, and condition checks that explain the recommendation."
  3. **Interface**: "Responsive and presentation-ready. The form adapts to desktop and mobile layouts with a clean visual hierarchy and practical field grouping."

#### Result Page (result.html)

**Hero Section with Results**
- Primary card showing:
  - Eyebrow: "Recommended crop"
  - Large heading: `{{ result.predicted_crop|title }}`
  - Badges: "Confidence {{ result.confidence_pct }}%", "Validated model"
  - Description paragraph explaining alignment

- Secondary card showing:
  - Eyebrow: "Suggested fertilizer"
  - Large text: `{{ result.fertilizer }}`
  - Note: "Base crop plan: {{ result.crop_profile.base_fertilizer }}. This recommendation is adjusted from the observed nutrient and management inputs."

**Results Grid** (Four columns)
1. **Top Alternatives** card
   - List of top 3 predictions with confidence percentages
   - Visual progress bars showing confidence proportion

2. **What Matched** card
   - Bullet list of up to 6 matched conditions from `{{ result.matched_conditions }}`
   - Examples: "Nitrogen is within the preferred range for Rice.", "Region north is suitable for Wheat."

3. **Attention Points** card (styled as caution-card)
   - Bullet list of up to 6 caution conditions from `{{ result.caution_conditions }}`
   - Examples: "Rainfall is 150 below the preferred band for Wheat.", "Soil type clay is less aligned with the profile for Maize."

4. **Input Summary** card
   - Definition list (dl/dt/dd) displaying all input values used for prediction

**Footer**
- Action button: "Run another analysis" (links back to index)

### JavaScript Interactivity (app.js)

**Region-to-State Filtering**
```javascript
// On DOM load:
1. Find region select and state select elements
2. Store the REGION_STATE_MAP from window object (injected by Flask)
3. Add change listener to region select
4. When region changes:
   - Get new states for selected region
   - Rebuild state options dropdown
   - Preserve current state if it's in the new region's list
   - Otherwise select first state in new region
```

---

## Backend Specifications

### Flask Application (app.py)

**Entry Point**
- Factory function: `create_app() -> Flask`
- Create app instance with SECRET_KEY = "smart-farming-decision-support"
- Register context processors and routes
- Return app instance

**Context Processor** (inject_globals)
Returns dictionary with:
- `field_definitions`: FIELD_DEFINITIONS from schema.py
- `form_groups`: FORM_GROUPS from schema.py
- `default_values`: default_form_values() from recommendation.py
- `region_state_map`: REGION_STATE_MAP from crop_profiles.py
- `model_stats`: Loaded from METRICS_FILE if exists, else empty dict with defaults

**Routes**

1. **GET /** (index page)
   - Render `index.html` with:
     - title="Smart Farming Decision Support System"
     - form_values=default_form_values()
     - error_message=None

2. **POST /predict** (form-based prediction)
   - Extract form data into payload dict (field_name -> form_value)
   - Apply default values for missing fields
   - Call predict_recommendation(payload)
   - On success: render `result.html` with result data
   - On ValueError (validation error): render `index.html` with error_message and original form_values, return 400 status

3. **POST /api/predict** (JSON API)
   - Accept JSON payload (request.get_json)
   - Call predict_recommendation(payload)
   - Return JSON response with result dict

4. **GET /api/health** (health check endpoint)
   - Return JSON with:
     - status: "ok"
     - model_available: bool (MODEL_FILE exists)
     - metrics_available: bool (METRICS_FILE exists)

**Main Execution**
```python
app = create_app()
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
```

### Configuration (src/config.py)

Define path constants:
- `PROJECT_ROOT = Path(__file__).resolve().parent.parent`
- `SRC_DIR = PROJECT_ROOT / "src"`
- `DATA_DIR = PROJECT_ROOT / "data"`
- `MODELS_DIR = PROJECT_ROOT / "models"`
- `REPORTS_DIR = PROJECT_ROOT / "reports"`
- `TEMPLATES_DIR = PROJECT_ROOT / "templates"`
- `STATIC_DIR = PROJECT_ROOT / "static"`
- `DATASET_FILE = DATA_DIR / "crop_recommendation_dataset.csv"`
- `MODEL_FILE = MODELS_DIR / "crop_recommender_pipeline.joblib"`
- `METRICS_FILE = MODELS_DIR / "training_metrics.json"`
- `CLASSIFICATION_REPORT_FILE = REPORTS_DIR / "classification_report.txt"`
- `FEATURE_IMPORTANCE_FILE = REPORTS_DIR / "feature_importance.csv"`
- `FEATURE_IMPORTANCE_PLOT = REPORTS_DIR / "feature_importance.png"`
- `CONFUSION_MATRIX_FILE = REPORTS_DIR / "confusion_matrix.csv"`
- `CONFUSION_MATRIX_PLOT = REPORTS_DIR / "confusion_matrix.png"`

Constants:
- `TARGET_COLUMN = "crop_label"`
- `RECORD_ID_COLUMN = "record_id"`
- `RANDOM_STATE = 42`

### Schema (src/schema.py)

**Field Definitions** (FIELD_DEFINITIONS dict)
Each field has: label, kind (number or select), unit, min/max (for numbers), step, default, and options (for selects).

Complete field list:
- nitrogen_kg_ha: number, unit="kg/ha", min=0, max=200, step=1, default=85
- phosphorus_kg_ha: number, unit="kg/ha", min=0, max=120, step=1, default=48
- potassium_kg_ha: number, unit="kg/ha", min=0, max=180, step=1, default=55
- temperature_c: number, unit="°C", min=0, max=45, step=0.1, default=27
- humidity_pct: number, unit="%", min=0, max=100, step=0.1, default=68
- soil_ph: number, unit="pH", min=4.0, max=9.0, step=0.1, default=6.8
- rainfall_mm: number, unit="mm/year", min=0, max=3500, step=1, default=950
- soil_moisture_pct: number, unit="%", min=0, max=100, step=0.1, default=42
- organic_matter_pct: number, unit="%", min=0, max=8, step=0.1, default=2.2
- sunlight_hours: number, unit="hours/day", min=0, max=14, step=0.1, default=8.5
- altitude_m: number, unit="meters", min=0, max=3500, step=10, default=350
- soil_type: select, options=(alluvial, black, clay, laterite, loam, red, sandy_loam, silty_loam), default=loam
- region: select, options=REGION_OPTIONS (from crop_profiles), default=central
- state: select, options=STATE_OPTIONS (sorted unique states), default=Madhya Pradesh
- season: select, options=(kharif, rabi, zaid, perennial), default=kharif
- irrigation_method: select, options=(rainfed, canal, drip, sprinkler, flood), default=canal

**Form Groups** (FORM_GROUPS list)
Three sections for UI organization:
1. Soil nutrients: nitrogen_kg_ha, phosphorus_kg_ha, potassium_kg_ha, soil_ph, organic_matter_pct, soil_moisture_pct
2. Weather profile: temperature_c, humidity_pct, rainfall_mm, sunlight_hours, altitude_m
3. Location and management: soil_type, region, state, season, irrigation_method

**Feature Lists**
- NUMERIC_FEATURES: list of all numeric fields
- CATEGORICAL_FEATURES: list of all select fields
- FEATURE_COLUMNS: NUMERIC_FEATURES + CATEGORICAL_FEATURES
- DEFAULT_INPUT_VALUES: dict from FIELD_DEFINITIONS defaults

### Crop Profiles (src/crop_profiles.py)

**Constants**
- SOIL_TYPES: tuple of soil type options
- REGION_STATE_MAP: dict mapping region names to state tuples
- SEASON_OPTIONS: (kharif, rabi, zaid, perennial)
- IRRIGATION_OPTIONS: (rainfed, canal, drip, sprinkler, flood)
- REGION_OPTIONS: tuple of region names from REGION_STATE_MAP

**CropProfile Dataclass**
Immutable dataclass with fields:
- crop: str (crop name)
- nitrogen, phosphorus, potassium: tuple (low, high) bounds
- temperature, humidity, soil_ph, rainfall, soil_moisture, organic_matter, sunlight_hours, altitude: tuple bounds
- soil_types: tuple of compatible soil types
- regions: tuple of suitable regions
- seasons: tuple of suitable seasons
- irrigation_methods: tuple of suitable irrigation methods
- base_fertilizer: str (base fertilizer recommendation)

**CROP_PROFILES Dict** (16 crops)
Each crop entry includes complete profile with realistic agronomic bounds and recommendations:

1. **rice**
   - N: (85, 130), P: (35, 60), K: (40, 85)
   - Temp: (22, 34), Humidity: (70, 95), pH: (5.5, 7.0)
   - Rainfall: (1500, 2600), Moisture: (55, 85), Organic: (1.5, 3.5)
   - Sunlight: (6.0, 9.0), Altitude: (0, 800)
   - Soils: alluvial, clay, silty_loam
   - Regions: east, south, coastal
   - Seasons: kharif, perennial
   - Irrigation: flood, canal
   - Base fertilizer: "Urea + DAP"

2. **wheat**
   - N: (70, 120), P: (30, 55), K: (35, 70)
   - Temp: (10, 24), Humidity: (45, 70), pH: (6.0, 7.8)
   - Rainfall: (400, 900), Moisture: (20, 45), Organic: (1.2, 2.8)
   - Sunlight: (8.0, 11.0), Altitude: (100, 1500)
   - Soils: loam, silty_loam, alluvial
   - Regions: north, central, plateau
   - Seasons: rabi
   - Irrigation: canal, sprinkler
   - Base fertilizer: "Urea + SSP"

3. **maize**
   - N: (60, 110), P: (25, 55), K: (35, 75)
   - Temp: (18, 32), Humidity: (45, 80), pH: (5.8, 7.5)
   - Rainfall: (500, 1200), Moisture: (25, 55), Organic: (1.4, 3.0)
   - Sunlight: (8.0, 11.0), Altitude: (0, 1200)
   - Soils: loam, red, sandy_loam
   - Regions: north, west, central, plateau
   - Seasons: kharif, zaid
   - Irrigation: canal, drip, sprinkler
   - Base fertilizer: "Balanced NPK 10:26:26"

4. **sugarcane**
   - N: (90, 140), P: (35, 60), K: (50, 95)
   - Temp: (20, 38), Humidity: (60, 90), pH: (6.0, 7.5)
   - Rainfall: (1200, 2400), Moisture: (45, 75), Organic: (1.8, 3.5)
   - Sunlight: (8.0, 12.0), Altitude: (0, 900)
   - Soils: alluvial, black, loam
   - Regions: west, south, coastal, central
   - Seasons: kharif, perennial
   - Irrigation: canal, drip, flood
   - Base fertilizer: "Urea + MOP"

5. **cotton**
   - N: (50, 90), P: (25, 50), K: (40, 80)
   - Temp: (21, 35), Humidity: (35, 70), pH: (6.0, 8.0)
   - Rainfall: (450, 1200), Moisture: (20, 45), Organic: (1.0, 2.5)
   - Sunlight: (9.0, 12.0), Altitude: (0, 1000)
   - Soils: black, red, loam
   - Regions: west, central, south
   - Seasons: kharif
   - Irrigation: drip, sprinkler
   - Base fertilizer: "DAP + MOP"

6. **jute**
   - N: (70, 120), P: (30, 55), K: (40, 80)
   - Temp: (24, 34), Humidity: (75, 95), pH: (6.0, 7.5)
   - Rainfall: (1500, 2800), Moisture: (55, 85), Organic: (1.8, 3.5)
   - Sunlight: (7.0, 10.0), Altitude: (0, 700)
   - Soils: alluvial, clay, silty_loam
   - Regions: east, coastal
   - Seasons: kharif
   - Irrigation: rainfed, flood
   - Base fertilizer: "Urea + Potash"

7. **chickpea**
   - N: (20, 50), P: (35, 70), K: (30, 65)
   - Temp: (10, 30), Humidity: (30, 70), pH: (6.0, 8.5)
   - Rainfall: (300, 700), Moisture: (15, 35), Organic: (1.0, 2.5)
   - Sunlight: (8.0, 11.0), Altitude: (0, 1200)
   - Soils: loam, sandy_loam, black
   - Regions: north, central, west
   - Seasons: rabi
   - Irrigation: rainfed, sprinkler
   - Base fertilizer: "DAP + Rhizobium inoculant"

8. **pigeonpea**
   - N: (30, 60), P: (30, 60), K: (30, 70)
   - Temp: (20, 35), Humidity: (40, 80), pH: (6.0, 7.8)
   - Rainfall: (600, 1200), Moisture: (20, 40), Organic: (1.2, 2.8)
   - Sunlight: (8.0, 11.0), Altitude: (0, 1000)
   - Soils: loam, red, black
   - Regions: central, west, south, plateau
   - Seasons: kharif
   - Irrigation: rainfed, drip
   - Base fertilizer: "DAP + FYM"

9. **kidneybeans**
   - N: (25, 55), P: (30, 60), K: (30, 70)
   - Temp: (15, 28), Humidity: (45, 80), pH: (6.0, 7.5)
   - Rainfall: (350, 900), Moisture: (20, 40), Organic: (1.2, 2.5)
   - Sunlight: (7.0, 10.0), Altitude: (200, 1600)
   - Soils: loam, sandy_loam, red
   - Regions: north, west, central, hill
   - Seasons: rabi, kharif
   - Irrigation: drip, sprinkler
   - Base fertilizer: "DAP + MOP"

10. **lentil**
    - N: (20, 45), P: (30, 60), K: (25, 55)
    - Temp: (8, 25), Humidity: (30, 70), pH: (6.0, 8.0)
    - Rainfall: (250, 600), Moisture: (15, 35), Organic: (1.0, 2.5)
    - Sunlight: (7.0, 10.0), Altitude: (0, 1500)
    - Soils: loam, silty_loam, sandy_loam
    - Regions: north, east, central, hill
    - Seasons: rabi
    - Irrigation: rainfed, sprinkler
    - Base fertilizer: "SSP + Compost"

11. **mungbean**
    - N: (20, 45), P: (30, 60), K: (25, 60)
    - Temp: (20, 35), Humidity: (45, 80), pH: (6.0, 7.5)
    - Rainfall: (400, 1000), Moisture: (20, 45), Organic: (1.0, 2.5)
    - Sunlight: (8.0, 11.0), Altitude: (0, 1000)
    - Soils: loam, red, sandy_loam
    - Regions: west, south, central, plateau
    - Seasons: kharif, zaid
    - Irrigation: drip, rainfed
    - Base fertilizer: "Balanced NPK 12:32:16"

12. **blackgram**
    - N: (25, 50), P: (30, 60), K: (25, 60)
    - Temp: (20, 35), Humidity: (50, 85), pH: (6.0, 7.5)
    - Rainfall: (450, 1000), Moisture: (20, 45), Organic: (1.2, 2.8)
    - Sunlight: (8.0, 11.0), Altitude: (0, 1000)
    - Soils: loam, black, sandy_loam
    - Regions: south, east, coastal
    - Seasons: kharif
    - Irrigation: rainfed, drip
    - Base fertilizer: "DAP + Micronutrient mix"

13. **groundnut**
    - N: (30, 60), P: (35, 65), K: (35, 70)
    - Temp: (20, 30), Humidity: (40, 70), pH: (6.0, 7.5)
    - Rainfall: (500, 1100), Moisture: (15, 35), Organic: (1.0, 2.5)
    - Sunlight: (9.0, 12.0), Altitude: (0, 800)
    - Soils: sandy_loam, loam, red
    - Regions: south, west, coastal, plateau
    - Seasons: kharif, zaid
    - Irrigation: drip, sprinkler
    - Base fertilizer: "Gypsum + SSP"

14. **banana**
    - N: (80, 140), P: (40, 80), K: (70, 130)
    - Temp: (24, 35), Humidity: (75, 95), pH: (5.5, 7.0)
    - Rainfall: (1200, 2500), Moisture: (45, 75), Organic: (2.0, 4.0)
    - Sunlight: (8.0, 11.0), Altitude: (0, 900)
    - Soils: alluvial, loam, black
    - Regions: south, coastal, east
    - Seasons: perennial, kharif
    - Irrigation: drip, flood
    - Base fertilizer: "NPK 12:12:17 + MOP"

15. **potato**
    - N: (60, 110), P: (35, 70), K: (60, 120)
    - Temp: (12, 25), Humidity: (55, 85), pH: (5.0, 6.5)
    - Rainfall: (500, 1000), Moisture: (30, 60), Organic: (1.5, 3.0)
    - Sunlight: (6.0, 9.0), Altitude: (500, 2500)
    - Soils: loam, sandy_loam, silty_loam
    - Regions: north, hill, central
    - Seasons: rabi
    - Irrigation: sprinkler, drip
    - Base fertilizer: "NPK 13:13:21 + Potash"

16. **apple**
    - N: (40, 80), P: (25, 55), K: (40, 90)
    - Temp: (4, 24), Humidity: (50, 80), pH: (5.5, 6.8)
    - Rainfall: (600, 1600), Moisture: (30, 60), Organic: (2.0, 4.5)
    - Sunlight: (6.0, 9.0), Altitude: (1200, 3000)
    - Soils: loam, sandy_loam, silty_loam
    - Regions: hill, north
    - Seasons: rabi, perennial
    - Irrigation: drip, sprinkler
    - Base fertilizer: "Calcium nitrate + MOP"

**Region-State Mapping** (REGION_STATE_MAP)
```python
{
    "north": (Punjab, Haryana, Uttar Pradesh, Uttarakhand, Himachal Pradesh, Jammu and Kashmir),
    "south": (Tamil Nadu, Kerala, Karnataka, Andhra Pradesh, Telangana),
    "east": (West Bengal, Odisha, Bihar, Jharkhand, Assam),
    "west": (Maharashtra, Gujarat, Rajasthan, Goa),
    "central": (Madhya Pradesh, Chhattisgarh),
    "coastal": (Kerala, Goa, Odisha, Andhra Pradesh, Tamil Nadu),
    "hill": (Himachal Pradesh, Uttarakhand, Sikkim, Arunachal Pradesh, Jammu and Kashmir),
    "plateau": (Karnataka, Telangana, Maharashtra, Jharkhand, Chhattisgarh),
}
```

### Recommendation Service (src/recommendation.py)

**get_model() function** (LRU cached, maxsize=1)
- Check if MODEL_FILE exists; raise FileNotFoundError if missing
- Load and return pipeline using load_trained_pipeline(MODEL_FILE)

**coerce_payload(payload: dict) -> dict**
- For each field in FEATURE_COLUMNS:
  - Get raw value from payload or use default
  - For numeric fields:
    - Convert to float (raise ValueError if cannot)
    - Validate within min/max bounds (raise ValueError if out of bounds)
    - Round to 2 decimal places
  - For select fields:
    - Validate value is in allowed options (raise ValueError if not)
    - Convert to string
- Return cleaned dict

**_tokenize_fertilizer(plan: str) -> list[str]**
- Split plan by " + " (after replacing " and " with " + ")
- Strip whitespace and remove duplicates
- Return ordered list of fertilizer tokens

**recommend_fertilizer(features: dict, crop: str) -> tuple(fertilizer_plan: str, matches: list, cautions: list)**
- Get crop profile from CROP_PROFILES
- Start with base fertilizer tokens
- For each comparison (N, P, K, temp, humidity, pH, rainfall, moisture, organic, sunlight, altitude):
  - Check if value is within crop's preferred range
  - If within: add to matches
  - If below: add caution note with gap size; add Urea/DAP/MOP if applicable
  - If above: add caution note with excess size
- Check soil type, region, season, irrigation compatibility
- Add matches and cautions for each
- Return (fertilizer_plan, matches[:6], cautions[:6])

**predict_recommendation(payload: dict) -> dict**
- Coerce payload to cleaned dict (raises ValueError on validation failure)
- Get model using get_model()
- Create DataFrame with single row of cleaned values
- Predict crop using model.predict()
- Get probabilities using model.predict_proba()
- Build ranking of top 3 crops with confidence percentages
- Call recommend_fertilizer() to get plan, matches, cautions
- Return dict with:
  - predicted_crop: str
  - confidence_pct: float (confidence of top prediction)
  - top_predictions: list of dicts (crop, confidence_pct)
  - fertilizer: str (recommended plan)
  - matched_conditions: list of match strings
  - caution_conditions: list of caution strings
  - input_values: cleaned dict
  - crop_profile: dict with soil_types, regions, seasons, irrigation_methods, base_fertilizer

**default_form_values() -> dict**
- Return copy of DEFAULT_INPUT_VALUES

### Modeling Pipeline (src/modeling.py)

**build_pipeline() -> Pipeline**
- Create ColumnTransformer with:
  - Numeric pipeline: SimpleImputer (strategy='median')
  - Categorical pipeline: SimpleImputer (strategy='most_frequent') + OneHotEncoder (sparse_output=False)
- Create SelectPercentile with mutual_info_classif, percentile=75
- Create RandomForestClassifier with:
  - n_estimators=260
  - max_depth=14
  - min_samples_split=4
  - min_samples_leaf=2
  - class_weight='balanced_subsample'
  - random_state=RANDOM_STATE (42)
  - n_jobs=-1
- Return Pipeline with steps: preprocess, select, model

**train_and_evaluate(dataset_path, model_path) -> dict**
- Load dataset from CSV
- Split into X_train/X_test/y_train/y_test (80/20, stratified)
- Create pipeline
- Perform 5-fold stratified cross-validation on training set
- Fit pipeline on training set
- Predict on test set
- Calculate: accuracy, precision, recall, F1 (all weighted)
- Generate classification report and confusion matrix
- Build feature importance table from pipeline
- Save artifacts:
  - Pipeline to MODEL_FILE (joblib)
  - Metrics to METRICS_FILE (JSON)
  - Classification report to CLASSIFICATION_REPORT_FILE
  - Feature importance to FEATURE_IMPORTANCE_FILE
  - Confusion matrix to CONFUSION_MATRIX_FILE
  - Feature importance plot PNG
  - Confusion matrix plot PNG
- Return metrics dict with: records, train_records, test_records, classes, accuracy, precision_weighted, recall_weighted, f1_weighted, cross_validation_accuracy_mean, cross_validation_accuracy_std, top_features, selected_feature_count

**load_trained_pipeline(model_path) -> Pipeline**
- Return joblib.load(model_path)

### Dataset Builder (src/dataset_builder.py)

**_sample_numeric(rng, bounds, precision=1) -> float**
- Calculate midpoint and span of bounds
- Generate normal distribution around midpoint with sigma = span / 4.8
- Clamp value to slightly expanded bounds
- Return rounded value

**_choose_state(rng, region) -> str**
- Return random state from REGION_STATE_MAP[region]

**generate_dataset(records_per_crop=120, random_state=RANDOM_STATE) -> pd.DataFrame**
- For each crop in CROP_PROFILES, generate 120 records:
  - Sample numeric values from crop profile ranges
  - Select categorical values from profile options
  - Populate row with all 16 features + crop_label
- Return shuffled DataFrame with columns: record_id, features..., crop_label
- Total: 16 crops × 120 = 1,920 records

**save_dataset(path, records_per_crop=120, random_state) -> df**
- Create parent directory if needed
- Generate dataset
- Save to CSV
- Return dataset

**load_dataset(path) -> df**
- Load and return CSV

### Training Scripts (src/train_model.py, src/generate_dataset.py)

**generate_dataset.py**
```python
def main():
    dataset = save_dataset(DATASET_FILE)
    print(f"Dataset created at {DATASET_FILE}")
    print(f"Rows: {len(dataset)}")
    print(dataset.head(5).to_string(index=False))
```

**train_model.py**
```python
def main():
    if not DATASET_FILE.exists():
        save_dataset(DATASET_FILE)
    else:
        load_dataset(DATASET_FILE)
    metrics = train_and_evaluate(DATASET_FILE)
    print("Training complete")
    for key, value in metrics.items():
        if key != "top_features":
            print(f"{key}: {value}")
```

---

## ML Model Specifications

### Architecture
- **Algorithm**: Random Forest Classifier
- **Feature Preprocessing**:
  - Numeric: SimpleImputer (median strategy)
  - Categorical: SimpleImputer (most_frequent) + OneHotEncoder
- **Feature Selection**: SelectPercentile (mutual_info_classif, 75th percentile)
- **Hyperparameters**:
  - n_estimators=260
  - max_depth=14
  - min_samples_split=4
  - min_samples_leaf=2
  - class_weight='balanced_subsample'
  - random_state=42

### Training Data
- **Dataset Size**: 1,920 records (120 per crop class)
- **Classes**: 16 crop types
- **Features**: 16 (11 numeric, 5 categorical)
- **Train/Test Split**: 80/20 (stratified)

### Expected Performance
- **Accuracy**: ~96.09%
- **Weighted Precision**: ~96.42%
- **Weighted Recall**: ~96.09%
- **Weighted F1-Score**: ~96.12%
- **5-Fold CV Mean Accuracy**: ~95.25%

### Evaluation Artifacts Generated
- Confusion matrix (CSV + PNG heatmap)
- Classification report (per-class metrics)
- Feature importance ranking (CSV + PNG bar chart showing top 12 features)
- Metrics JSON (summary of all numbers)

---

## Data Flow

### Request Processing Flow (Online Inference)
1. User submits form on index.html
2. JavaScript validates region selection, updates state options dynamically
3. Form POSTs to /predict with field data
4. Flask extracts payload and calls predict_recommendation()
5. Recommendation service validates and coerces all inputs
6. Model pipeline preprocesses and predicts crop
7. Rule engine compares inputs against crop profile
8. Generate matched conditions and caution notes
9. Render result.html with crop, confidence, fertilizer, conditions
10. User reviews results and can submit new analysis

### Model Build Flow (Offline Training)
1. Run `python src/generate_dataset.py` to create synthetic dataset
2. Run `python src/train_model.py` to train:
   - Load dataset
   - Split 80/20
   - Cross-validate on training set
   - Fit model on full training set
   - Evaluate on test set
   - Save pipeline, metrics, reports
3. Flask app loads pre-trained model on startup

---

## API Specification

### Endpoints

**POST /predict** (Form-based)
- Accepts form data (application/x-www-form-urlencoded)
- Returns HTML result page or error page with 400 status
- Query fields: all 16 input fields from schema

**POST /api/predict** (JSON)
- Request body: JSON dict with field names as keys, values as numbers or strings
- Response: JSON dict with predictions, confidence, fertilizer, matched/caution conditions
- Example response:
  ```json
  {
    "predicted_crop": "wheat",
    "confidence_pct": 95.2,
    "top_predictions": [
      {"crop": "wheat", "confidence_pct": 95.2},
      {"crop": "barley", "confidence_pct": 3.1},
      {"crop": "rice", "confidence_pct": 1.7}
    ],
    "fertilizer": "Urea + SSP",
    "matched_conditions": ["Nitrogen is within the preferred range for wheat.", ...],
    "caution_conditions": ["Rainfall is 50 above the preferred band for wheat.", ...],
    "input_values": {...},
    "crop_profile": {...}
  }
  ```

**GET /api/health**
- No request body required
- Response: JSON dict with status, model_available, metrics_available
- Used for deployment health checks

---

## Deployment & Execution

### Prerequisites
- Python 3.10+
- Virtual environment (venv, conda, or uv)

### Installation
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate
pip install -r requirements.txt
```

### Running the Pipeline

**Step 1: Generate Dataset**
```bash
python src/generate_dataset.py
```
Output: `data/crop_recommendation_dataset.csv` (1,920 rows)

**Step 2: Train Model**
```bash
python src/train_model.py
```
Outputs:
- `models/crop_recommender_pipeline.joblib`
- `models/training_metrics.json`
- `reports/classification_report.txt`
- `reports/feature_importance.csv`
- `reports/feature_importance.png`
- `reports/confusion_matrix.csv`
- `reports/confusion_matrix.png`

**Step 3: Start Web Application**
```bash
python app.py
```
Server runs at `http://127.0.0.1:5000/`

### Directory Verification
Before running the app, ensure these files exist:
- `models/crop_recommender_pipeline.joblib` (required)
- `models/training_metrics.json` (optional; creates defaults if missing)

---

## Key Design Decisions

### 1. Hybrid Architecture (ML + Rules)
- Classifier provides crop prediction with confidence
- Rule engine adds explainability via matched/caution conditions
- Fertilizer suggestions are adjusted based on detected nutrient gaps
- Farmers get both a recommendation AND a rationale

### 2. Feature Validation & Coercion
- All numeric inputs validated against min/max constraints
- Categorical inputs validated against allowed options
- Validation failures return 400 with error message (not 500)
- Error messages clearly specify which field failed and why

### 3. Cross-Validation & Class Weighting
- Stratified K-fold CV ensures stable estimates across crops
- Balanced subsample weighting prevents majority-class bias
- Feature selection keeps pipeline compact (~75th percentile)
- Reproducible with RANDOM_STATE=42

### 4. Responsive Web Interface
- Single-page form with grouped fields (soil, weather, location)
- Dynamic region-to-state filtering via JavaScript
- Clean earth-tone styling aligned with agricultural theme
- Result page clearly highlights recommendation and reasoning

### 5. Extensibility
- JSON API enables integration with mobile apps, dashboards, external systems
- Crop profiles are modular; adding new crops only requires expanding CROP_PROFILES dict
- Dataset generation is parameterized; records_per_crop can be increased for larger models
- Model hyperparameters centralized in build_pipeline(); easy to tune

---

## Testing Checklist

- [ ] Form submits successfully with default values
- [ ] Form validates numeric bounds (e.g., nitrogen > 200 triggers error)
- [ ] Form validates categorical options (e.g., invalid soil_type triggers error)
- [ ] Region-to-state filtering updates state dropdown dynamically
- [ ] Result page displays predicted crop, confidence, fertilizer, matched/caution conditions
- [ ] JSON /api/predict endpoint returns valid response with same predictions as form
- [ ] /api/health endpoint returns status=ok and correct availability flags
- [ ] Feature importance plot shows top 12 features in descending order
- [ ] Confusion matrix plot is readable heatmap with crop names
- [ ] Model metrics (accuracy, F1, etc.) are ~96% on test set
- [ ] Result page links back to index for re-running analysis

---

## Summary

This complete prompt encapsulates every aspect of the Smart Farming Decision Support System:
- **Frontend**: Responsive form UI with earth-tone styling, dynamic filtering, result visualization
- **Backend**: Flask routes, validation, and context injection
- **ML Pipeline**: Random Forest with preprocessing, feature selection, and cross-validation
- **Data**: 16-crop dataset with realistic agronomic profiles and ranges
- **Inference**: Hybrid classifier + rule-based fertilizer engine
- **API**: Form-based and JSON endpoints for programmatic use

A developer given this prompt should be able to build the exact project structure, functionality, UI/UX, and performance characteristics.
