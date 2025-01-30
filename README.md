# Chronic Kidney Disease (CKD) Prediction Using SVM

## Overview

This project focuses on predicting Chronic Kidney Disease (CKD) using a Support Vector Machine (SVM) model. The dataset contains various health-related features such as age, gender, race, creatinine levels, albumin levels, blood pressure, and more. The goal is to classify whether a patient has CKD based on these features.

## The project includes:

- **Data Preprocessing**: Cleaning and preparing the dataset for model training.
- **Feature Scaling**: Standardizing the features to improve model performance.
- **Model Training**: Using SVM with hyperparameter tuning to achieve the best performance.
- **Model Evaluation**: Evaluating the model using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
- **Model Saving**: Saving the trained model using pickle for future use.

## Dataset

The dataset contains the following columns:

| Column Name | Description                                      |
| ----------- | ------------------------------------------------ |
| RIDAGEYR    | Age of the patient                               |
| RIAGENDER   | Gender of the patient                            |
| RIDRETH3    | Race of the patient                              |
| LBXSCR      | Serum creatinine level                           |
| URXUMA      | Albumin level in urine                           |
| URXUCR      | Creatinine level in urine                        |
| LBXGH       | Glycohemoglobin level                            |
| LBXHGB      | Hemoglobin level                                 |
| BPXDI1      | Diastolic blood pressure                         |
| BPXSY1      | Systolic blood pressure                          |
| BMXBMI      | Body Mass Index (BMI)                            |
| DIQ010      | Whether the patient has diabetes                 |
| MCQ160b     | Whether the patient has congestive heart failure |
| MCQ160c     | Whether the patient has coronary heart disease   |
| SMQ020      | Whether the patient has smoked 100 cigarettes    |
| Target      | Target variable (1: CKD, 2: No CKD)              |

## Key Metrics

Two key metrics are used in this project to assess kidney health:

### eGFR (Estimated Glomerular Filtration Rate):

- Measures how well the kidneys are filtering waste from the blood.
- Normal eGFR: ≥ 90 mL/min/1.73m².
- eGFR < 60: Indicates chronic kidney disease (CKD).

### ACR (Albumin-to-Creatinine Ratio):

- Measures the ratio of albumin to creatinine in urine.
- Normal ACR: < 30 mg/g.
- ACR > 30: Indicates kidney damage.

## Code Workflow

### Data Preprocessing:

1. Load the dataset.
2. Drop unnecessary columns (Albumin\_to\_Creatinine\_Ratio and Glomerular\_Filtration\_Rate).
3. Check for missing values and data types.

### Exploratory Data Analysis (EDA):

- Visualize the distribution of the target variable.
- Plot a correlation heatmap to understand feature relationships.

### Feature Scaling:

- Standardize the features using `StandardScaler`.

### Model Training:

1. Split the data into training and testing sets.
2. Use `GridSearchCV` to tune hyperparameters for the SVM model.
3. Train the SVM model with the best hyperparameters.

### Model Evaluation:

- Evaluate the model using classification metrics (accuracy, precision, recall, F1-score).
- Plot the confusion matrix and ROC curve.

### Model Saving:

- Save the trained SVM model using `pickle`.

## Results

The SVM model achieved the following performance metrics:

- **Training Accuracy**: 0.98
- **Testing Accuracy**: 0.92
- **F1-Score**: 0.91
- **Precision**: 0.93
- **Recall**: 0.89
- **ROC-AUC**: 0.98

The model shows good performance in predicting CKD, with no significant overfitting.

## How to Use the Model

### Load the Model:

```python
import pickle

with open('svm_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
```

### Make Predictions:

```python
predictions = loaded_model.predict(X_test)
```

### Evaluate the Model:

Use the same evaluation metrics (accuracy, precision, recall, F1-score, ROC-AUC) to assess the model's performance on new data.

## Dependencies

- **Python 3.x**
- **Libraries:**
  - pandas
  - numpy
  - scikit-learn
  - seaborn
  - matplotlib
  - pickle

## Future Work

- Incorporate additional features such as patient medical history.
- Experiment with other machine learning models (e.g., Random Forest, XGBoost).
- Deploy the model as a web application for real-time predictions.

## Conclusion

This project demonstrates the use of SVM for predicting chronic kidney disease. The model performs well and can be further improved with additional data and feature engineering. The saved model can be used for future predictions and deployed in healthcare applications.

