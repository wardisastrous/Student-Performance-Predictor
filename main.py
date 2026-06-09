import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("student_data.csv")

# Feature engineering
df["study_efficiency"] = df["hours_studied"] * df["attendance"] / 100

# Features & target
X = df.drop("final_score", axis=1)
y = df["final_score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Test custom input
import pandas as pd

new_student = pd.DataFrame({
    "hours_studied": [6],
    "attendance": [85],
    "sleep_hours": [7],
    "previous_score": [75],
    "extracurricular": [1],
    "study_efficiency": [5.1]
})

prediction = model.predict(new_student)

print("Predicted Score:", prediction[0])