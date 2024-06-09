from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")
model = None
def load_model():
    with open('model.pkl', 'rb') as model_file:
        return pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            age = int(request.form.get('age'))
            gender = int(request.form.get('gender'))
            cp = int(request.form.get('cp'))
            trestbps = int(request.form.get('trestbps'))
            cholestrol = int(request.form.get('cholestrol'))
            fbs = int(request.form.get('fbs'))
            resting_ECG = int(request.form.get('resting_ECG'))
            thalach = int(request.form.get('thalach'))
            exang = int(request.form.get('exang'))
            oldPeakHistory = float(request.form.get('oldPeakHistory'))
            Slope_levels = int(request.form.get('Slope_levels'))
            CA_levels = int(request.form.get('CA_levels'))
            thal = int(request.form.get('thal'))

            # Create a list to store the input features
            input_features = [
                age,
                gender,
                cp,
                trestbps,
                cholestrol,
                fbs,
                resting_ECG,
                thalach,
                exang,
                oldPeakHistory,
                Slope_levels,
                CA_levels,
                thal
            ]

            # Convert the list to a NumPy array
            features = np.array(input_features).reshape(1, -1)
            model = load_model()  # Load the model only once

            prediction = model.predict(features)[0]

            if prediction == 1:
                result = "Patient has heart disease"
            elif prediction == 0:
                result = "Patient does not have heart disease"
            else:
                result = "Unknown prediction"
            return render_template("predict.html", result=result)

        except Exception as e:
            return str(e), 500
    else:
        return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)