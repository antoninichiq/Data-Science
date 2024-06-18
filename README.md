# Data Science
### This repository contains two different projects related to machine learning:

# SVR Web App for Prediction
## Overview
This repository contains code for building a Support Vector Regression (SVR) model to predict the total bill amount in a restaurant based on various factors like:
* **Sex of the customer**
* **Whether the customer is a smoker**
* **Day of the week**
* **Time of the day (Lunch or Dinner)**
* **Size of the party**
### Dataset
The dataset used for training and testing the model is the "tips" dataset from seaborn. It contains information about tips, total bill, sex, smoker, day, time, and size of the party for a set of restaurant customers.

## Methodology
1. **Data Loading and Preprocessing:**

    - The "tips" dataset is loaded using seaborn.
    - Features are identified and target variable (total bill) is extracted.
    - Feature encoding is performed using label encoding and one-hot encoding.

2. **Model Training:**

    - SVR model is initialized and trained on the preprocessed data.
    - Hyperparameter tuning is performed using GridSearchCV to optimize model performance.

3. **Model Evaluation:**

    - The trained model is evaluated using metrics like:
        - R2 score
        - Mean squared error 
        - Mean absolute error
        - Root mean squared error

4. **Model Saving:**

    - The best performing SVR model is saved using pickle for future use and integrated into a web application.

# RandomForest Travel Product Prediction

## Overview

This project focuses on predicting the likelihood of customers purchasing a travel package based on various demographic and behavioral factors. It employs machine learning techniques, specifically the Random Forest Classifier, to build a predictive model.

## Dataset

The project utilizes a dataset named "Travel". This dataset likely contains information about:

* **Customer Demographics:** Age, Gender, Marital Status, Occupation, City Tier, Monthly Income, etc.
* **Travel History:** Number of Trips, Passport Ownership, etc.
* **Marketing Interactions:** Type of Contact, Duration of Pitch, Number of Follow-ups, Product Pitched, Preferred Property Star, Pitch Satisfaction Score, etc.
* **Target Variable:**  `ProdTaken` (indicates whether the customer purchased a travel package)

## Project Structure

* **`RandomForest-Travel-Product-Prediction.ipynb`**:  Contains the Python code for data preprocessing, model training, evaluation, and visualization.

## Methodology

1. **Data Preprocessing:**
   - Handling missing values (using mean, median, or mode imputation).
   - Feature engineering (e.g., creating the 'TotalVisiting' feature).
   - Encoding categorical variables (using One-Hot Encoding).
   - Scaling numerical features (using StandardScaler).
2. **Model Selection:** Random Forest Classifier is chosen for its robustness to outliers and ability to handle high-dimensional data.
3. **Model Training:** The dataset is split into training and testing sets. The Random Forest model is trained on the training data.
4. **Hyperparameter Tuning:** RandomizedSearchCV is employed to find optimal hyperparameters for the Random Forest model, enhancing its performance.
5. **Model Evaluation:** The trained model is evaluated using metrics like accuracy, precision, recall, F1-score, and ROC-AUC score.
6. **Visualization:**  An ROC curve is generated to visualize the model's performance across different thresholds.

### Both projects demonstrate the application of machine learning techniques for solving real-world problems.
