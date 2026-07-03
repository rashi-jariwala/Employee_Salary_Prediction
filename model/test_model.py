import json
import pickle
import pandas as pd
import os

# ----------------------------------------
# Base Directory
# ----------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "model")

# ----------------------------------------
# Load Model
# ----------------------------------------

with open(os.path.join(MODEL_DIR, "salary_model.pkl"), "rb") as f:
    model = pickle.load(f)

print("Model Loaded Successfully")

# ----------------------------------------
# Load Columns
# ----------------------------------------

with open(os.path.join(MODEL_DIR, "columns.json"), "r") as f:
    data_columns = json.load(f)["data_columns"]

print("Columns Loaded Successfully")


#Now Create User Input
input_data = [0] * len(data_columns)

input_data[data_columns.index("experience")] = 5
input_data[data_columns.index("age")] = 28
input_data[data_columns.index("skill_score")] = 90

input_data[data_columns.index("education_Masters")] = 1
input_data[data_columns.index("city_Surat")] = 1
input_data[data_columns.index("department_IT")] = 1


#Convert to DataFrame
input_df = pd.DataFrame(
    [input_data],
    columns=data_columns
)

print(input_df)

#Predict
prediction = model.predict(input_df)

print("Predicted Salary :", prediction[0])