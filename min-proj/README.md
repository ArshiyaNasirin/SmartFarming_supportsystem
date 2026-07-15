# Smart Farming Decision Support System

This project recommends a suitable crop and fertilizer plan from soil, weather, and location inputs using a machine learning pipeline with a Flask web interface.

## Core features

- Crop recommendation using a Random Forest classifier
- Feature preprocessing and selection before classification
- Fertilizer suggestion based on nutrient balance and crop profile rules
- Responsive Flask interface for manual field input
- JSON API endpoint for programmatic predictions

## Project structure

- `src/generate_dataset.py` creates the crop recommendation dataset
- `src/train_model.py` trains and evaluates the model
- `app.py` runs the Flask application
- `data/` stores the prepared dataset
- `models/` stores the trained pipeline and metrics
- `reports/` stores evaluation artifacts and the written project report

## How to run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Generate the dataset:

   ```bash
   python src/generate_dataset.py
   ```

3. Train and evaluate the model:

   ```bash
   python src/train_model.py
   ```

4. Start the web app:

   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000 in a browser.

## Outputs

- Dataset: `data/crop_recommendation_dataset.csv`
- Trained model: `models/crop_recommender_pipeline.joblib`
- Metrics: `models/training_metrics.json`
- Feature importance plot: `reports/feature_importance.png`
- Confusion matrix plot: `reports/confusion_matrix.png`
- Project report: `reports/SmartFarmingDecisionSupportSystem_Report.md`
