import os
import json
import pickle
import numpy as np
import pandas as pd


class SalaryPrediction:

    def __init__(self):

        # Project root (two levels up from this file)
        BASE_DIR = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        self.model_path = os.path.join(
            BASE_DIR,
            "model",
            "salary_model.pkl"
        )

        self.column_path = os.path.join(
            BASE_DIR,
            "model",
            "columns.json"
        )

        # Load Model
        with open(self.model_path, "rb") as file:

            self.model = pickle.load(file)

        # Load Columns
        with open(self.column_path, "r") as file:

            self.columns = json.load(file)

        self.data_columns = self.columns["data_columns"]


    # =====================================================
    # Load Dropdown Data
    # =====================================================

    def load_column_data(self):

        education = []
        city = []
        department = []

        for column in self.data_columns:

            if column.startswith("education_"):

                education.append(
                    column.replace("education_", "")
                )

            elif column.startswith("city_"):

                city.append(
                    column.replace("city_", "")
                )

            elif column.startswith("department_"):

                department.append(
                    column.replace("department_", "")
                )

        return {

            "education": sorted(education),

            "city": sorted(city),

            "department": sorted(department)

        }


    # =====================================================
    # Prepare Input
    # =====================================================

    def prepare_input(self, user_data):

        x = np.zeros(len(self.data_columns))

        x[self.data_columns.index("experience")] = int(
            user_data["experience"]
        )

        x[self.data_columns.index("age")] = int(
            user_data["age"]
        )

        x[self.data_columns.index("skill_score")] = int(
            user_data["skill_score"]
        )

        education = "education_" + user_data["education"]

        if education in self.data_columns:

            x[self.data_columns.index(education)] = 1

        city = "city_" + user_data["city"]

        if city in self.data_columns:

            x[self.data_columns.index(city)] = 1

        department = "department_" + user_data["department"]

        if department in self.data_columns:

            x[self.data_columns.index(department)] = 1

        input_df = pd.DataFrame(

            [x],

            columns=self.data_columns

        )

        return input_df


    # =====================================================
    # Predict Salary
    # =====================================================

    def predict_salary(self, user_data):

        input_df = self.prepare_input(user_data)

        prediction = self.model.predict(input_df)

        return prediction