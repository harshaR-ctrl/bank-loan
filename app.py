from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model and scaler
model = pickle.load(open('loan_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = request.json
        
        # Extract features in correct order
        features = [
            float(data['age']),
            float(data['income']),
            float(data['loanAmount']),
            float(data['creditScore']),
            float(data['employmentYears']),
            float(data['dependents'])
        ]
        
        # Validate inputs
        if features[0] < 18 or features[0] > 80:
            return jsonify({'error': 'Age must be between 18 and 80'}), 400
        if features[1] < 1200000 or features[1] > 40000000:
            return jsonify({'error': 'Income must be between ₹12 Lakhs and ₹40 Crores'}), 400
        if features[2] < 1500000 or features[2] > 40000000:
            return jsonify({'error': 'Loan amount must be between ₹15 Lakhs and ₹40 Crores'}), 400
        if features[3] < 300 or features[3] > 850:
            return jsonify({'error': 'Credit score must be between 300 and 850'}), 400
        if features[4] < 0 or features[4] > 50:
            return jsonify({'error': 'Employment years must be between 0 and 50'}), 400
        if features[5] < 0 or features[5] > 10:
            return jsonify({'error': 'Number of dependents must be between 0 and 10'}), 400
        
        # Reshape and scale
        features_array = np.array([features])
        features_scaled = scaler.transform(features_array)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        
        approval_probability = probability[1] * 100  # Probability of approval
        
        result = {
            'approved': int(prediction),
            'probability': round(approval_probability, 2),
            'message': 'Loan APPROVED' if prediction == 1 else 'Loan REJECTED',
            'color': 'success' if prediction == 1 else 'danger'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
