from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('D:/MBA_DSDA_Sem-3_Files/Summer Internship/Guided Projects/GP1_Electricity_Load_Type_Prediction/model/random_forest_model.joblib')

# Mapping of numerical predictions to load types
load_type_mapping = {
    0: "Light Load",
    1: "Medium Load",
    2: "Maximum Load"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    usage = float(data['usage'])
    lagc_rp = float(data['lagc_rp'])
    lagc_pf = float(data['lagc_pf'])
    leadc_pf = float(data['leadc_pf'])
    nsm = float(data['nsm'])
    week_status_0 = float(data['week_status_0'])
    week_status_1 = float(data['week_status_1'])
    
    features = np.array([[usage, lagc_rp, lagc_pf, leadc_pf, nsm, week_status_0, week_status_1]])
    numerical_prediction = model.predict(features)[0]
    load_type_prediction = load_type_mapping[numerical_prediction]
    
    return jsonify({'prediction': load_type_prediction})

if __name__ == '__main__':
    app.run(debug=True)
