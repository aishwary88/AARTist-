from flask import Blueprint, render_template, request
import joblib
import numpy as np

main = Blueprint('main', __name__)

# Load your trained anemia model (update path as needed)
model = joblib.load('anemia_model.pkl')

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login.html')
def login():
    return render_template('login.html')

@main.route('/form.html', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Extract required features for anemia prediction
        age = float(request.form.get('age', 0))
        gender = request.form.get('gender', 'Male')
        hb = float(request.form.get('hb', 0))
        wbc = float(request.form.get('wbc', 0))
        platelets = float(request.form.get('platelets', 0))
        # Add more features if your model needs them

        # Example: encode gender (adjust as per your model)
        gender_val = 1 if gender.lower() == 'male' else 0

        # Prepare input for model (order must match training)
        X = np.array([[age, gender_val, hb, wbc, platelets]])

        pred = model.predict(X)[0]
        result = "Anemia Detected" if pred == 1 else "No Anemia Detected"

        return render_template('result.html', result=result)
    return render_template('form.html')
