# Employee Salary Prediction

A Flask-based web application that predicts an employee's salary using a machine learning regression model. The project combines a simple web interface, MongoDB-backed prediction history, and a training pipeline for generating the model.

## Project Overview

This application is designed to:
- collect employee-related inputs such as experience, age, skill score, education, city, and department;
- predict salary using a trained Linear Regression model;
- store prediction history in MongoDB;
- provide a basic web UI for login, registration, prediction, and history views.

## Tech Stack

- Python
- Flask
- pandas
- numpy
- scikit-learn
- MongoDB with PyMongo
- Jinja2 templates
- Bootstrap

## Project Structure

```text
Employee_Salary_Prediction/
├── app.py                 # Main Flask app entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── database/              # MongoDB connection helpers
├── dataset/               # Dataset files
├── model/                 # Trained model and feature columns
├── routes/                # Route modules for auth/prediction
├── static/                # CSS and static assets
├── templates/             # HTML templates
├── utils/                 # Salary prediction utility logic
```

## Features

- User registration and login flow
- Salary prediction form
- Prediction history storage
- Model training script
- Saved model artifacts for reuse

## Prerequisites

Before running the project, ensure you have:
- Python 3.8+
- MongoDB installed and running locally
- The dataset file available in the dataset folder

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Employee_Salary_Prediction
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> If you already installed the dependencies successfully, you can skip this step and proceed directly to running the app.


## Running the Application

1. Start MongoDB locally.
2. If the model files are missing or you want to retrain the model, run:
   ```bash
   python model/train_model.py
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open the app in your browser:
   ```text
   http://127.0.0.1:5000
   ```

> The project currently expects the required Python packages to be installed and a local MongoDB instance to be available.


## Model Training

The model is trained using the script in [model/train_model.py](model/train_model.py). It:
- loads the employee salary dataset;
- converts categorical features such as education, city, and department into dummy variables;
- splits the data into train and test sets;
- trains a Linear Regression model;
- saves the trained model as [model/salary_model.pkl](model/salary_model.pkl) and the feature columns as [model/columns.json](model/columns.json).

## Notes

- The application expects a local MongoDB instance at the URI defined in [config.py](config.py).
- The repository includes the trained model files in [model](model) so you can run the app without retraining immediately.
- If your dataset file name or path differs, update it in [model/train_model.py](model/train_model.py).
- If the app fails to start, verify that MongoDB is running and that the required packages are installed in the active Python environment.

## License

This project is for educational and demonstration purposes.
