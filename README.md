
# Student Performance Prediction System Using Machine Learning

## Overview

This project predicts a student's final academic score using Machine Learning techniques. The model analyzes factors such as study hours, attendance, sleep duration, previous scores, and extracurricular participation to estimate academic performance.

## Features

- Data preprocessing using Pandas
- Feature engineering for improved prediction
- Linear Regression model using Scikit-Learn
- Performance evaluation using MAE and R² Score
- Student score prediction based on custom inputs

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

## Dataset Attributes

| Feature | Description |
|----------|-------------|
| hours_studied | Daily study hours |
| attendance | Attendance percentage |
| sleep_hours | Average sleep duration |
| previous_score | Previous academic score |
| extracurricular | Participation in extracurricular activities |
| final_score | Target variable (student score) |

## Project Workflow

1. Load dataset
2. Perform feature engineering
3. Split data into training and testing sets
4. Train Linear Regression model
5. Evaluate model performance
6. Predict student scores

## Performance Metrics

- Mean Absolute Error (MAE)
- R² Score

## Installation

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Run Project

```bash
python main.py
```

## Sample Output

```text
MAE: 0.96
R2 Score: 0.94
Predicted Score: 79.98
```

## Future Improvements

- Larger real-world dataset
- Random Forest and XGBoost implementation
- Streamlit web application
- Model deployment on cloud platforms

## Author

Uday Kapila

<img width="1977" height="330" alt="Screenshot 2026-06-09 095038" src="https://github.com/user-attachments/assets/e63d258d-f2e4-48d2-be9d-8bc199e6001d" />
