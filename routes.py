from flask import Blueprint, render_template, request
import joblib
import numpy as np
import os

main = Blueprint('main', __name__)

# Load anemia model
ANEMIA_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'anemia_model_1.7.pkl')
print(f"Trying to load anemia model from: {ANEMIA_MODEL_PATH}")
try:
    if not os.path.exists(ANEMIA_MODEL_PATH):
        print(f"Model file does not exist at: {ANEMIA_MODEL_PATH}")
        raise FileNotFoundError(f"Model file not found at {ANEMIA_MODEL_PATH}")
    anemia_model = joblib.load(ANEMIA_MODEL_PATH)
    print("Anemia model loaded successfully!")
except Exception as e:
    print(f"Anemia model load error: {e}")
    anemia_model = None

# Load liver model
LIVER_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'liver_model.pkl')
print(f"Trying to load liver model from: {LIVER_MODEL_PATH}")
try:
    if not os.path.exists(LIVER_MODEL_PATH):
        print(f"Model file does not exist at: {LIVER_MODEL_PATH}")
        raise FileNotFoundError(f"Model file not found at {LIVER_MODEL_PATH}")
    liver_model = joblib.load(LIVER_MODEL_PATH)
    print("Liver model loaded successfully!")
except Exception as e:
    print(f"Liver model load error: {e}")
    liver_model = None

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/home.html')
def home_html():
    return render_template('home.html')

@main.route('/login.html')
def login():
    return render_template('login.html')

@main.route('/form.html', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if anemia_model is None:
            return "Model not found or failed to load.", 500
        try:
            age = float(request.form.get('age', 0))
            gender = request.form.get('gender', 'Male')
            hb = float(request.form.get('hb', 0))
            wbc = float(request.form.get('wbc', 0))
            platelets = float(request.form.get('platelets', 0))
            gender_val = 1 if gender.lower() == 'male' else 0
            X = np.array([[age, gender_val, hb, wbc, platelets]])
            pred = anemia_model.predict(X)[0]
            result = "Anemia Detected" if pred == 1 else "No Anemia Detected"
            return render_template('result.html', result=result)
        except Exception as ex:
            return f"Error in prediction: {ex}", 400
    return render_template('form.html')

@main.route('/liver.html', methods=['GET', 'POST'])
def liver():
    if request.method == 'POST':
        if liver_model is None:
            return "Liver model not found or failed to load.", 500
        try:
            # Extract only the fields needed for liver prediction
            age = float(request.form.get('age', 0))
            gender = request.form.get('gender', 'Male')
            ast = float(request.form.get('ast', 0))
            alt = float(request.form.get('alt', 0))
            alp = float(request.form.get('alp', 0))
            total_bilirubin = float(request.form.get('total_bilirubin', 0))
            direct_bilirubin = float(request.form.get('direct_bilirubin', 0))
            albumin = float(request.form.get('albumin', 0))
            gender_val = 1 if gender.lower() == 'male' else 0
            # Adjust the order and features as per your liver model's training
            X = np.array([[age, gender_val, ast, alt, alp, total_bilirubin, direct_bilirubin, albumin]])
            pred = liver_model.predict(X)[0]
            result = "Liver Disease Detected" if pred == 1 else "No Liver Disease Detected"
            return render_template('result.html', result=result)
        except Exception as ex:
            return f"Error in liver prediction: {ex}", 400
    return render_template('form.html')
