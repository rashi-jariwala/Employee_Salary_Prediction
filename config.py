import os

class Config:

    # Flask Secret Key
    SECRET_KEY = "salary_prediction_secret_key"

    # JWT Secret Key
    JWT_SECRET_KEY = "salary_prediction_jwt_secret_key"

    # Local MongoDB
    MONGO_URI = "mongodb://localhost:27017"

    # Azure Cosmos (Later)
    # MONGO_URI = "Your Azure Cosmos Mongo URI"

    DATABASE_NAME = "EmployeeSalaryDB"

    MODEL_PATH = os.path.join(
        os.getcwd(),
        "model",
        "salary_model.pkl"
    )

    COLUMN_PATH = os.path.join(
        os.getcwd(),
        "model",
        "columns.json"
    )