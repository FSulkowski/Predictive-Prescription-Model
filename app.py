from flask import Flask, request, render_template
import pickle
import pandas as pd



app = Flask(__name__)

# Load the model
with open('optimized_model.pkl', 'rb') as file:
    model = pickle.load(file)



# List of columns used during training (updated columns after feature engineering)
model_columns = [
    'gender', 'ap_hi', 'ap_lo', 'cholesterol', 'smoke', 'alco', 'active', 
    'BMI', 'bp_range', 'age_years', 'risk_score', 'comorbidity_flag', 
    'chol_gluc_interaction', 'smoke_alco_interaction', 'bmi_category_Normal', 
    'bmi_category_Overweight', 'bmi_category_Obese', 'bp_category_Normal', 
    'bp_category_Elevated', 'bp_category_Hypertensive', 'age_group_Adult', 
    'age_group_Middle-aged', 'age_group_Senior'
]

@app.route('/')
def index():
    return render_template('index.html', result=None)

# Route to handle prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])  
        ap_hi = int(request.form['ap_hi'])
        ap_lo = int(request.form['ap_lo'])
        cholesterol = int(request.form['cholesterol'])
        gluc = int(request.form['gluc'])
        smoke = int(request.form['smoke'])
        alco = int(request.form['alco'])
        active = int(request.form['active'])
        cardio = int(request.form['cardio'])


        input_data = pd.DataFrame({
            'weight': [weight],
            'height': [height],
            'age': [age],
            'ap_hi': [ap_hi],
            'ap_lo': [ap_lo],
            'cholesterol': [cholesterol],
            'gluc': [gluc],
            'smoke': [smoke],
            'alco': [alco],
            'active': [active],
            'cardio': [cardio]
        })

        # Feature engineering
        input_data['BMI'] = input_data['weight'] / (input_data['height'] ** 2) * 703
        input_data['bp_range'] = input_data['ap_hi'] - input_data['ap_lo']
        input_data['age_years'] = input_data['age']  

        input_data['bmi_category'] = pd.cut(input_data['BMI'], 
                                             bins=[0, 18.5, 24.9, 29.9, float('inf')], 
                                             labels=['Underweight', 'Normal', 'Overweight', 'Obese'])
        input_data['bp_category'] = pd.cut(input_data['bp_range'], 
                                            bins=[-float('inf'), 40, 60, 80, float('inf')], 
                                            labels=['Low', 'Normal', 'Elevated', 'Hypertensive'])
        input_data['age_group'] = pd.cut(input_data['age_years'], 
                                          bins=[0, 18, 45, 60, float('inf')], 
                                          labels=['Child', 'Adult', 'Middle-aged', 'Senior'])

        input_data['risk_score'] = (
            (input_data['BMI'] * 0.4) + 
            (input_data['cholesterol'] * 0.3) + 
            (input_data['gluc'] * 0.3) + 
            (input_data['smoke'] * 0.2) + 
            (input_data['alco'] * 0.2) + 
            (input_data['active'] * -0.2) + 
            (input_data['cardio'] * 0.5) +
            (input_data['ap_hi'] * 0.1) + 
            (input_data['ap_lo'] * 0.1) + 
            (input_data['age_years'] * 0.1)
        )

        # Drop and encode
        input_data.drop(columns=['weight', 'height', 'age'], inplace=True)
        input_data = pd.get_dummies(input_data, drop_first=True)
        input_data = input_data.reindex(columns=model_columns, fill_value=0)

        # Predictions
        prediction = model.predict(input_data)
        prediction_prob = model.predict_proba(input_data)
        qualifies_prob = prediction_prob[0][1]
        does_not_qualify_prob = prediction_prob[0][0]
        qualifies_prob_percent = f"{qualifies_prob * 100:.2f}%"
        does_not_qualify_prob_percent = f"{does_not_qualify_prob * 100:.2f}%"

        
        bmi_value = round(input_data['BMI'].iloc[0], 2)
        risk_score_value = round(input_data['risk_score'].iloc[0], 2)

        # Check qualifications
        if bmi_value >= 30:
            result = (
                f"This person qualifies for Ozempic with a BMI of {bmi_value:.2f}. "
                "This person has a BMI over 30, which is a primary qualification criterion."
            )
        elif bmi_value >= 27 and risk_score_value > 45:
            result = (
                f"This person qualifies for Ozempic with a BMI of {bmi_value:.2f}. "
                "This person has a BMI between 27 and 30, which is classified as overweight, "
                "and has a risk score of 45 or higher. The risk score takes into account factors such as "
                "age, blood pressure, cholesterol levels, smoking, alcohol consumption, and activity "
                "levels. A high risk score indicates a higher likelihood of developing obesity-related "
                "complications, which Ozempic can help manage. "
                "Consult a healthcare provider for further assessment and treatment options."
            )
        else:
            result = (
                f"This person does not qualify for Ozempic with a BMI of {bmi_value:.2f}. "
                "BMI must be 27 or higher with a risk score of 45 or higher, or 30 and above."
            )

        
        return render_template('index.html', result=result, bmi=bmi_value, risk_score=risk_score_value)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")


