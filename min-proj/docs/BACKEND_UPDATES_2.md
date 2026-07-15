# Backend Updates 2

## BE-1 Crop recommendation pipeline

- Added the data model, preprocessing pipeline, feature selection, Random Forest classifier, and evaluation flow.
- Saved the trained pipeline, metrics JSON, classification report, feature importance table, and confusion matrix artifacts.
- Model performance after the final training run:
  - Accuracy: 96.09%
  - Weighted precision: 96.42%
  - Weighted recall: 96.09%
  - Weighted F1-score: 96.12%
  - 5-fold cross-validation mean: 95.25%

## DB-1 Dataset preparation

- Built a 1,920-row crop recommendation dataset with 16 crop classes.
- Included soil nutrients, climate attributes, soil type, region, state, season, irrigation method, and crop label.
- Generated the CSV file at `data/crop_recommendation_dataset.csv`.

## BE-2 Mini-project report DOCX generator

- Added a reproducible DOCX report generator script at `scripts/generate_smartfarming_report_docx.py`.
- Regenerated `SmartFarmingDecisionSupportSystem_MiniProject_Report.docx` to match the sample report’s titles/structure and closely match section sizes.
- Added `python-docx` to `requirements.txt` so the report generator works in fresh environments.

## Manual steps

- Run `python scripts/generate_smartfarming_report_docx.py` to rebuild the DOCX report.
- Run `python src/generate_dataset.py` if the dataset file needs to be regenerated.
- Run `python src/train_model.py` after dataset generation to refresh the trained pipeline and evaluation artifacts.
