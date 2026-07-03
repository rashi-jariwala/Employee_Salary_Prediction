import os
import json
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# Load Dataset
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "employee_salary_dataset.xlsx"
)

df = pd.read_excel(DATA_PATH)

print(df.head())


# ==========================================
# Dataset Information
# ==========================================

print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())


# ==========================================
# Separate Features & Target
# ==========================================

X = df.drop("salary", axis=1)
y = df["salary"]


# ==========================================
# Convert Categorical Columns
# ==========================================

X = pd.get_dummies(
    X,
    columns=["education", "city", "department"],
    drop_first=True
)


# ==========================================
# Save Columns
# ==========================================

columns = {
    "data_columns": list(X.columns)
}

MODEL_DIR = os.path.join(BASE_DIR, "model")

with open(os.path.join(MODEL_DIR, "columns.json"), "w") as f:
    json.dump(columns, f, indent=4)


# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ==========================================
# Train Model
# ==========================================

linear_reg = LinearRegression()

linear_reg.fit(X_train, y_train)


# ==========================================
# Prediction
# ==========================================

y_pred = linear_reg.predict(X_test)


# ==========================================
# Model Evaluation
# ==========================================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("-" * 50)
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


# ==========================================
# Save Model
# ==========================================

with open(os.path.join(MODEL_DIR, "salary_model.pkl"), "wb") as f:
    pickle.dump(linear_reg, f)

print("\nModel Saved Successfully")