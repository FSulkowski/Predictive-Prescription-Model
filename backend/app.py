from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from sqlalchemy import create_engine
import os

app = Flask(__name__)

# Simple CORS configuration that allows all origins
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["OPTIONS", "GET", "POST"],
        "allow_headers": ["Content-Type"],
    }
})

# Load your trained ML model
model_path = os.path.join(os.path.dirname(__file__), 'ozempic_model.pkl')
model = joblib.load(model_path)

# Database connection
db_url = 'postgresql://francis:1234@localhost/Ozempic_ML'
engine = create_engine(db_url)

@app.route('/predict', methods=['OPTIONS', 'POST'])
def predict():
    # Handle preflight request
    if request.method == 'OPTIONS':
        return '', 200
        
    try:
        if not request.json:
            return jsonify({'error': 'No data provided'}), 400
            
        data = request.json
        print(data)
        features = pd.DataFrame([data])
        
        required_fields = ['gluc', 'cholesterol', 'BMI', 'weight', 'height']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400
            
        prediction = model.predict(features)
        
        try:
            save_to_db(features)
        except Exception as db_error:
            print(f"Database error: {str(db_error)}")
            
        result = 'Qualifies for Ozempic' if prediction[0] == 1 else 'Does not qualify for Ozempic'
        return jsonify({'result': result})
        
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

def save_to_db(data):
    data.to_sql('new_data', engine, if_exists='append', index=False)

@app.route('/dummy')
def dummy():
    return jsonify({'dummy': 'This is a dummy endpoint'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)