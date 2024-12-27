from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
from model import model


app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_value = np.array(data['input_value']).reshape(-1, 1)
    prediction = model.predict(input_value)
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)