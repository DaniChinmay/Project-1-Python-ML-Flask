from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__, static_folder='assets')

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
    try:
        data = request.json
        usage = float(data['usage'])
        lagc_rp = float(data['lagc_rp'])
        lagc_pf = float(data['lagc_pf'])
        leadc_pf = float(data['leadc_pf'])
        nsm = float(data['nsm'])
        week_status_0 = float(data['week_status_0'])
        week_status_1 = float(data['week_status_1'])
    
        features = np.array([[usage, lagc_rp, lagc_pf, leadc_pf, nsm, week_status_0, week_status_1]])
        numerical_prediction = model(features)[0]
        load_type_prediction = load_type_mapping[numerical_prediction]
    
        return jsonify(prediction=load_type_prediction)
    except Exception as e:
       # Log the error and return a JSON response
        app.logger.error(f"Error processing prediction: {e}")
        return jsonify(error=str(e)), 500

@app.route('/results', methods=['POST','GET'])
def results():
    usage = request.args.get('usage')
    lagc_rp = request.args.get('lagc_rp')
    lagc_pf = request.args.get('lagc_pf')
    leadc_pf = request.args.get('leadc_pf')
    nsm = request.args.get('nsm')
    week_status_0 = request.args.get('week_status_0')
    week_status_1 = request.args.get('week_status_1')
    prediction = request.args.get('prediction')
    
    return render_template('results.html', 
                           usage=usage, 
                           lagc_rp=lagc_rp, 
                           lagc_pf=lagc_pf, 
                           leadc_pf=leadc_pf, 
                           nsm=nsm, 
                           week_status_0=week_status_0, 
                           week_status_1=week_status_1, 
                           prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
