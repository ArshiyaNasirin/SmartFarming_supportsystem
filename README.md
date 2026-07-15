# Smart Farming Decision Support System

This project recommends a suitable crop and fertilizer plan from soil, weather, and location inputs using a machine learning pipeline with a Flask web interface.

## Core features

🌾 Crop Recommendation using Machine Learning
🌱 Fertilizer Recommendation
🌍 Region & State Selection
🌦️ Weather and Soil Parameter Analysis
📊 High Prediction Accuracy (96.09%)
💻 Responsive Web Interface
🔗 JSON Prediction API
📈 Model Evaluation Reports

## Project structure

- `src/generate_dataset.py` creates the crop recommendation dataset
- `src/train_model.py` trains and evaluates the model
- `app.py` runs the Flask application
- `data/` stores the prepared dataset
- `models/` stores the trained pipeline and metrics
- `reports/` stores evaluation artifacts and the written project report

- 🚀 How It Works
Enter soil and weather details.
Click Predict.
The Flask backend processes the input.
The Random Forest model predicts the most suitable crop.
The system recommends the appropriate fertilizer.
Results are displayed on the web interface.

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

5. Open  http://127.0.0.1:5000 in a browser.

📤 Output
Recommended Crop
Fertilizer Suggestion
Prediction Confidence
