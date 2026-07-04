# import os


# class Config:

#     # Flask Secret Key
#     SECRET_KEY = "salary_prediction_secret_key"

#     # JWT Secret Key
#     JWT_SECRET_KEY = "salary_prediction_jwt_secret_key"

#     # Local MongoDB
#     # MONGO_URI = "mongodb://localhost:27017"

#     # Azure Cosmos (Later)
#     MONGO_URI = "mongodb+srv://rashi1999:R1a9s9h9i9@docdb-cluster-20260704-0437.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"

#     DATABASE_NAME = "EmployeeSalaryDB"

#     # Azure deployment settings
#     HOST = os.getenv("HOST", "0.0.0.0")
#     PORT = int(os.getenv("PORT", os.getenv("WEBSITES_PORT", "8000")))
#     DEBUG = os.getenv("DEBUG", "False").lower() == "true"

#     MODEL_PATH = os.path.join(
#         os.getcwd(),
#         "model",
#         "salary_model.pkl"
#     )

#     COLUMN_PATH = os.path.join(
#         os.getcwd(),
#         "model",
#         "columns.json"
#     )

import os
from dotenv import load_dotenv


load_dotenv()
class Config:
    # Flask Secret Key
    SECRET_KEY = os.getenv("SECRET_KEY", "salary_prediction_secret_key")

    # JWT Secret Key
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "salary_prediction_jwt_secret_key")

    # MongoDB URI
    MONGO_URI = os.getenv("MONGO_URI")
    print(MONGO_URI)
    DATABASE_NAME = os.getenv("DATABASE_NAME", "EmployeeSalaryDB")
    print(DATABASE_NAME)
    print("Exists:", os.path.exists(".env"))
    print("URI:", os.getenv("MONGO_URI"))
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", os.getenv("WEBSITES_PORT", "8000")))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    MODEL_PATH = os.path.join(os.getcwd(), "model", "salary_model.pkl")
    COLUMN_PATH = os.path.join(os.getcwd(), "model", "columns.json")