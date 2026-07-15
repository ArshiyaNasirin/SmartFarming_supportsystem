
🌱 Smart Farming Decision Support System

A Machine Learning-based web application that helps farmers identify the most suitable crop and recommends the appropriate fertilizer based on soil nutrients, weather conditions, and location. The system uses a Random Forest Classifier to provide accurate crop recommendations through a user-friendly Flask web interface.

📌 Features
🌾 Crop Recommendation using Machine Learning
🌱 Fertilizer Recommendation
🌍 Region & State Selection
🌦️ Weather and Soil Parameter Analysis
📊 High Prediction Accuracy (96.09%)
💻 Responsive Web Interface
🔗 JSON Prediction API
📈 Model Evaluation Reports
🛠 Technology Stack

📂 Project Structure

Smart-Farming-Decision-Support-System/
│
├── app.py
├── requirements.txt
├── data/
├── docs/
├── models/
├── reports/
├── scripts/
├── src/
├── static/
├── templates/
└── README.md

⚙️ Installation
1. Clone the Repository
git clone https://github.com/ArshiyaNasirin/farming.git
2. Navigate to Project
cd farming
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
python app.py
5. Open Browser
http://127.0.0.1:5000/

🚀 How It Works
Enter soil and weather details.
Click Predict.
The Flask backend processes the input.
The Random Forest model predicts the most suitable crop.
The system recommends the appropriate fertilizer.
Results are displayed on the web interface.

📊 Machine Learning Model
Algorithm: Random Forest Classifier
Dataset Size: 1,920 Records
Crop Classes: 16
Training Accuracy: 96.09%
Cross Validation: 95.25%

📥 Input Parameters
Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
Rainfall
Soil Type
Region
State
Season
Irrigation Method

📤 Output
Recommended Crop
Fertilizer Suggestion
Prediction Confidence

📈 Model Performance
Metric	Value
Accuracy	96.09%
Precision	96.42%
Recall	96.09%
F1-Score	96.12%
Cross Validation	95.25%

This project was developed during the Technical Training Program under the guidance of the project mentor and Mr. Manoj Sir (R-Sequence Organization). I sincerely thank them for their continuous support, valuable guidance, and encouragement throughout the successful completion of this project.

📄 License

This project is developed for educational and academic purposes.

