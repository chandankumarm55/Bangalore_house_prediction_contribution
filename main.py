from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load data and model
data = pd.read_csv('Cleaned.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))

@app.route('/')
def index():
    # Retrieve unique locations and pass them to the template
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('sqft')

    # Prepare input DataFrame for prediction
    input_data = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = pipe.predict(input_data)[0] * 1e5  # Convert to correct scale
    return str(np.round(prediction, 2))

if __name__ == '__main__':
    # Use environment variable PORT if available, otherwise default to 5001
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
