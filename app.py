# import os
# import json
# import pickle
# import numpy as np
# import pandas as pd

# from flask import (
#     Flask,
#     render_template,
#     request,
#     redirect,
#     url_for,
#     session,
#     jsonify,
#     make_response,
#     flash
# )

# from flask_jwt_extended import (
#     JWTManager,
#     create_access_token,
#     jwt_required,
#     get_jwt_identity,
#     verify_jwt_in_request
# )

# password hashing removed for demo (plain-text passwords are used)

# import pymongo
# import config


# # ==========================================================
# # Flask App
# # ==========================================================

# app = Flask(__name__)

# app.secret_key = config.Config.SECRET_KEY

# app.config["JWT_SECRET_KEY"] = config.Config.JWT_SECRET_KEY

# jwt = JWTManager(app)


# # ==========================================================
# # MongoDB Connection
# # ==========================================================

# client = pymongo.MongoClient(config.Config.MONGO_URI)

# db = client[config.Config.DATABASE_NAME]

# users_collection = db["users"]

# prediction_collection = db["prediction_history"]


# # ==========================================================
# # Load ML Model
# # ==========================================================

# with open(config.Config.MODEL_PATH, "rb") as f:

#     model = pickle.load(f)


# # ==========================================================
# # Load Columns
# # ==========================================================

# with open(config.Config.COLUMN_PATH, "r") as f:

#     data_columns = json.load(f)["data_columns"]


# # ==========================================================
# # Home
# # ==========================================================

# @app.route("/")
# def home():

#     if session.get("user"):

#         return redirect(url_for("dashboard"))

#     return redirect(url_for("login"))


# # ==========================================================
# # Register
# # ==========================================================

# @app.route("/register", methods=["GET", "POST"])
# def register():

#     if request.method == "POST":

#         name = request.form["name"]

#         email = request.form["email"]

#         password = request.form["password"]

#         user = users_collection.find_one({

#             "email": email

#         })

#         if user:

#             flash("Email already exists.")

#             return redirect(url_for("register"))

#         users_collection.insert_one({

#             "name": name,

#             "email": email,

#             "password": hashed_password

#         })

#         flash("Registration Successful")

#         return redirect(url_for("login"))

#     return render_template("register.html")


# # ==========================================================
# # Login
# # ==========================================================

# @app.route("/login", methods=["GET", "POST"])
# def login():

#     if request.method == "POST":

#         email = request.form["email"]

#         password = request.form["password"]

#         user = users_collection.find_one({

#             "email": email

#         })

#         if not user:

#             flash("Invalid Email")

#             return redirect(url_for("login"))

#         if not user:
    
    

#         access_token = create_access_token(

#             identity=email

#         )

#         session["user"] = user["name"]

#         session["email"] = email

#         response = make_response(

#             redirect(url_for("dashboard"))

#         )

#         response.set_cookie(

#             "access_token",

#             access_token,

#             httponly=True

#         )

#         return response

#     return render_template("login.html")

# ==========================================================
# Dashboard
# ==========================================================


# # ==========================================================
# # Prepare Input For Prediction
# # ==========================================================

# def prepare_input(form_data):

#     x = np.zeros(len(data_columns))

#     # Numerical Features
#     x[data_columns.index("experience")] = int(form_data["experience"])
#     x[data_columns.index("age")] = int(form_data["age"])
#     x[data_columns.index("skill_score")] = int(form_data["skill_score"])

#     # Education
#     education = "education_" + form_data["education"]

#     if education in data_columns:
#         x[data_columns.index(education)] = 1

#     # City
#     city = "city_" + form_data["city"]

#     if city in data_columns:
#         x[data_columns.index(city)] = 1

#     # Department
#     department = "department_" + form_data["department"]

#     if department in data_columns:
#         x[data_columns.index(department)] = 1

#     return pd.DataFrame(
#         [x],
#         columns=data_columns
#     )


# # ==========================================================
# # Salary Prediction
# # ==========================================================

# @app.route("/prediction", methods=["GET", "POST"])
# def prediction():

#     if "user" not in session:

#         return redirect(url_for("login"))

#     predicted_salary = None

#     if request.method == "POST":

#         input_df = prepare_input(request.form)

#         predicted_salary = round(

#             model.predict(input_df)[0],

#             2

#         )

#         prediction_collection.insert_one({

#             "user_name": session["user"],

#             "email": session["email"],

#             "experience": request.form["experience"],

#             "age": request.form["age"],

#             "education": request.form["education"],

#             "city": request.form["city"],

#             "department": request.form["department"],

#             "skill_score": request.form["skill_score"],

#             "predicted_salary": predicted_salary

#         })

#     return render_template(

#         "prediction.html",

#         salary=predicted_salary

#     )


# # ==========================================================
# # Logout
# # ==========================================================

# @app.route("/logout")
# def logout():

#     session.clear()

#     response = make_response(

#         redirect(url_for("login"))

#     )

#     response.delete_cookie("access_token")

#     return response


#     # ==========================================================
# # Prediction History
# # ==========================================================

# @app.route("/history")
# def history():

#     if "user" not in session:
#         return redirect(url_for("login"))

#     history_data = prediction_collection.find({

#         "email": session["email"]

#     })

#     return render_template(

#         "history.html",

#         history=history_data

#     )


# # ==========================================================
# # JWT Protected API
# # ==========================================================

# @app.route("/api/profile", methods=["GET"])
# @jwt_required()
# def profile():

#     current_user = get_jwt_identity()

#     return jsonify({

#         "message": "Token Verified Successfully",

#         "email": current_user

#     })


# # ==========================================================
# # Health Check
# # ==========================================================

# @app.route("/health")
# def health():

#     return jsonify({

#         "status": "Running",

#         "application": "Employee Salary Prediction System"

#     })


# # ==========================================================
# # Error Handling
# # ==========================================================

# @app.errorhandler(404)
# def page_not_found(error):

#     return render_template("404.html"), 404


# @app.errorhandler(500)
# def internal_server_error(error):

#     return render_template("500.html"), 500


# # ==========================================================
# # Run Application
# # ==========================================================

# if __name__ == "__main__":

#     app.run(

#         debug=True,

#         host="0.0.0.0",

#         port=5000

#     )

from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    decode_token
)

import pymongo
import config
import datetime

# Import from local `utils` package
from utils.salary_prediction import SalaryPrediction


# ==========================================================
# Salary Prediction Object
# ==========================================================

salary_prediction_obj = SalaryPrediction()


# ==========================================================
# Flask App
# ==========================================================

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = config.Config.JWT_SECRET_KEY
app.config["SECRET_KEY"] = config.Config.SECRET_KEY

jwt = JWTManager(app)


# ==========================================================
# MongoDB Connection
# ==========================================================


@app.route("/dashboard")
def dashboard():
    # Try to get token from Authorization header or cookie
    token = request.headers.get("Authorization") or request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        token = token.split(None, 1)[1]

    username = None
    if token:
        try:
            decoded = decode_token(token)
            username = decoded.get("sub") or decoded.get("identity")
        except Exception:
            username = None

    if not username:
        return redirect(url_for("login"))

    return render_template("home.html", username=username, token=token)


mongo_client = pymongo.MongoClient(config.Config.MONGO_URI)

db = mongo_client[config.Config.DATABASE_NAME]

user_collection = db["users"]

prediction_collection = db["prediction_history"]


# ==========================================================
# Home
# ==========================================================

@app.route("/")
def home():

    return redirect(url_for("login"))


# ==========================================================
# Register Page
# ==========================================================

@app.route("/register_page")
def register_page():

    return render_template("register.html")


# ==========================================================
# Login Page
# ==========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    # Accept JSON or form
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    user_name = data.get("user_name") or data.get("email")
    password = data.get("password")

    if not user_name or not password:
        if request.is_json:
            return jsonify({"status": "failure", "message": "Missing credentials"}), 400
        else:
            from flask import flash
            flash("Please enter username and password")
            return redirect(url_for("login"))

    response = user_collection.find_one({"user_name": user_name, "password": password})

    if response:
        access_token = create_access_token(identity=user_name, expires_delta=datetime.timedelta(minutes=30))

        if request.is_json:
            return jsonify({"status": "success", "message": "Login Successful", "access_token": access_token})
        else:
            response = make_response(redirect(url_for("dashboard")))
            response.set_cookie("access_token", access_token, httponly=True)
            return response

    else:
        if request.is_json:
            return jsonify({"status": "failure", "message": "Invalid Credentials"}), 401
        else:
            from flask import flash
            flash("Invalid username or password")
            return redirect(url_for("login"))


# ==========================================================
# Prediction Page
# ==========================================================

@app.route("/prediction_page")
def prediction_page():
    return render_template("prediction.html")


@app.route("/prediction")
def prediction_redirect():
    # keep compatibility with templates that link to /prediction
    return redirect(url_for("prediction_page"))


# ==========================================================
# History Page
# ==========================================================

@app.route("/history_page")
def history_page():

    token = request.headers.get("Authorization") or request.cookies.get("access_token")
    current_user = None
    show_recent = bool(request.args.get("recent", ""))

    if token:
        if token.startswith("Bearer "):
            token = token.split(None, 1)[1]
        try:
            decoded = decode_token(token)
            current_user = decoded.get("sub") or decoded.get("identity")
        except Exception:
            current_user = None

    if not current_user:
        return redirect(url_for("login"))

    history_query = prediction_collection.find(
        {"user_name": current_user},
        {"_id": 0}
    ).sort("created_at", pymongo.DESCENDING)

    if show_recent:
        history_query = history_query.limit(1)

    history_list = [record for record in history_query]

    return render_template(
        "history.html",
        token=token,
        history=history_list,
        recent=show_recent
    )


@app.route("/history_recent")
def history_recent():
    return redirect(url_for("history_page", recent=1))


@app.route("/history")
def history_redirect():
    return redirect(url_for("history_page"))


# ==========================================================
# Register
# ==========================================================

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    # Accept either JSON (API) or form (browser)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    user_name = data.get("user_name") or data.get("name")
    password = data.get("password")
    email_id = data.get("email_id") or data.get("email")
    experience = data.get("experience", "0")

    if not user_name or not password or not email_id:
        if request.is_json:
            return jsonify({"status": "failure", "message": "Missing required fields"}), 400
        else:
            from flask import flash
            flash("Please provide name, email and password")
            return redirect(url_for("register_page"))

    response = user_collection.find_one({"email_id": email_id})

    if not response:
        user_collection.insert_one({
            "user_name": user_name,
            "password": password,
            "email_id": email_id,
            "experience": experience,
            "created_at": datetime.datetime.now()
        })

        if request.is_json:
            return jsonify({"status": "success", "message": "User Registered Successfully"})
        else:
            from flask import flash
            flash("Registration successful. Please login.")
            return redirect(url_for("login"))

    else:
        if request.is_json:
            return jsonify({"status": "exists", "message": "User Already Exists"}), 409
        else:
            from flask import flash
            flash("User already exists")
            return redirect(url_for("register_page"))


# ==========================================================
# Forget Password
# ==========================================================

@app.route("/forget_password", methods=["POST"])
def forget_password():

    user_data = request.form

    user_name = user_data["user_name"]

    email_id = user_data["email_id"]

    new_password = user_data["new_password"]

    response = user_collection.find_one({

        "user_name": user_name,

        "email_id": email_id

    })

    if response:

        user_collection.update_one(

            {

                "user_name": user_name

            },

            {

                "$set": {

                    "password": new_password

                }

            }

        )

        return jsonify({

            "status": "success",

            "message": "Password Updated Successfully"

        })

    else:

        return jsonify({

            "status": "failure",

            "message": "Invalid User Details"

        })
# ==========================================================
# Education Options
# ==========================================================

@app.route("/education_options")
@jwt_required()
def education_options():

    col_data = salary_prediction_obj.load_column_data()

    education_values = col_data["education"]

    return jsonify(education_values)


# ==========================================================
# City Options
# ==========================================================

@app.route("/city_options")
@jwt_required()
def city_options():

    col_data = salary_prediction_obj.load_column_data()

    city_values = col_data["city"]

    return jsonify(city_values)


# ==========================================================
# Department Options
# ==========================================================

@app.route("/department_options")
@jwt_required()
def department_options():

    col_data = salary_prediction_obj.load_column_data()

    department_values = col_data["department"]

    return jsonify(department_values)


# ==========================================================
# Predict Salary
# ==========================================================

@app.route("/predict_salary", methods=["POST"])
def predict_salary():

    user_input_data = request.form

    # Try to determine current user from token via Authorization header or cookie
    token = request.headers.get("Authorization") or request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        token = token.split(None, 1)[1]

    current_user = None
    if token:
        try:
            decoded = decode_token(token)
            current_user = decoded.get("sub") or decoded.get("identity")
        except Exception:
            current_user = None

    # Fallback user identifier
    if not current_user:
        current_user = user_input_data.get("user_name") or "anonymous"

    prediction = salary_prediction_obj.predict_salary(user_input_data)

    record = {
        "user_name": current_user,
        "experience": user_input_data.get("experience"),
        "age": user_input_data.get("age"),
        "education": user_input_data.get("education"),
        "city": user_input_data.get("city"),
        "department": user_input_data.get("department"),
        "skill_score": user_input_data.get("skill_score"),
        "predicted_salary": float(prediction[0]),
        "created_at": datetime.datetime.now()
    }

    prediction_collection.insert_one(record)

    # If client expects JSON (API), return JSON. Otherwise render the prediction page with result.
    if request.is_json:
        return jsonify({"status": "success", "predicted_salary": record["predicted_salary"]})
    else:
        # Re-render prediction page showing the salary and keep token in context
        return render_template("prediction.html", salary=record["predicted_salary"], token=token)

    # ==========================================================
# Prediction History API
# ==========================================================

@app.route("/prediction_history")
@jwt_required()
def prediction_history():

    current_user = get_jwt_identity()

    history = prediction_collection.find(

        {

            "user_name": current_user

        },

        {

            "_id": 0

        }

    )

    history_list = []

    for record in history:

        history_list.append(record)

    return jsonify(history_list)


# ==========================================================
# User Profile
# ==========================================================

@app.route("/profile")
@jwt_required()
def profile():

    current_user = get_jwt_identity()

    user = user_collection.find_one(

        {

            "user_name": current_user

        },

        {

            "_id": 0,

            "password": 0

        }

    )

    return jsonify(user)


# ==========================================================
# Logout
# ==========================================================

@app.route("/logout")
def logout():
    response = make_response(redirect(url_for("login")))
    response.delete_cookie("access_token")
    return response


# ==========================================================
# Health Check
# ==========================================================

@app.route("/health")
def health():

    return jsonify({

        "status": "Running",

        "application": "Employee Salary Prediction"

    })


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":

    app.run(
        host=getattr(config.Config, "FLASK_HOST", "0.0.0.0"),
        port=getattr(config.Config, "FLASK_PORT", 5000),
        debug=True
    )