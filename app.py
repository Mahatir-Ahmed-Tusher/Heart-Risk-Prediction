from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

# Define the expected feature order
FEATURES = [
    'pain_arms_jaw_back', 'age', 'cold_sweats_nausea', 'chest_pain', 
    'fatigue', 'dizziness', 'swelling', 'shortness_of_breath', 
    'palpitations', 'sedentary_lifestyle'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data based on the expected feature order
        input_data = [float(request.form[feature]) for feature in FEATURES]
        final_features = np.array([input_data])

        # Make prediction
        prediction = model.predict(final_features)
        output = 'At Risk' if prediction[0] == 1 else 'Not at Risk'

        return render_template('index.html', prediction_text=f'Heart Risk Prediction: {output}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
