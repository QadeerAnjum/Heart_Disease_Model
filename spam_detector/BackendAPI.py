from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

model = None

@app.route('/')
def hello_world():
    return render_template("index.html")

def load_model():
    global model
    try:
        with open('model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        logging.info("Model loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to load model: {e}")

# Call load_model function to load the model
load_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Expect JSON input
        data = request.get_json()
        if not data or 'sms' not in data:
            logging.error("Invalid input received.")
            return "Invalid input", 400

        # Prepare the features for the model
        sms = data['sms']
        features = np.array([sms])

        # Make the prediction
        prediction = model.predict(features)[0]
        
        # Return the prediction result
        result = "SMS spam" if prediction == 1 else "SMS is a ham"
        logging.info(f"Prediction made successfully: {result}")
        return result
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
