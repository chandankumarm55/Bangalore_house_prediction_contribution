# House Price Predictor

This is a web application built using Flask and machine learning to predict house prices in Bangalore based on features like location, number of bedrooms (BHK), bathrooms, and square footage. The model uses Ridge Regression to provide accurate price predictions based on user inputs.

🌐 **Live Demo:** [Bangalore House Price Predictor](https://bangalore-house-prediction-contribution.onrender.com/)

> ⚠️ **Note:** The website may take a few minutes to load initially as it's hosted on a free-tier server.

## Features

- Interactive web interface for house price prediction
- Location selection from a comprehensive dropdown menu
- Input fields for:
  - BHK (Bedrooms, Hall, Kitchen)
  - Number of bathrooms
  - Total square footage
- Instant price predictions based on provided inputs

## Tech Stack

- **Backend:**
  - Flask (Python web framework)
  - Scikit-learn (Machine learning)
  - Pandas (Data manipulation)
  - NumPy (Numerical computations)
- **Frontend:**

  - HTML
  - CSS
  - Jinja2 (Template engine)

- **Machine Learning:**
  - Ridge Regression model
  - Feature engineering
  - Data preprocessing

## Installation

### Method 1: Using requirements.txt

```bash
# Clone the repository
git clone https://github.com/chandankumarm55/Bangalore_house_prediction_contribution.git

# Navigate to project directory
cd Bangalore_house_prediction_contribution

# Install dependencies
pip install -r requirements.txt
```

### Method 2: Manual Installation

Install the following dependencies individually:

```bash
pip install Flask==2.0.2
pip install Werkzeug==2.0.3
pip install pandas==2.0.3
pip install numpy==1.25.2
pip install scikit-learn==1.5.2
pip install gunicorn==20.1.0
```

## Running the Application

1. After installation, run the Flask application:

```bash
python main.py
```

2. Open your web browser and navigate to:

```
http://127.0.0.1:5001
```

## Project Structure

### Key Files

- `ridgemodel.pkl`: Contains the trained Ridge Regression model used for price predictions
- `Bangalore House Prediction.ipynb`: Jupyter notebook containing:
  - Data preprocessing steps
  - Model training process
  - Feature engineering
  - Model evaluation
    > Note: This notebook can be opened using Google Colab or Jupyter Notebook

### Directories

```
house-price-predictor/
├── main.py              # Flask application
├── ridgemodel.pkl      # Trained model
├── requirements.txt    # Dependencies
├── templates/          # HTML templates
├── static/            # CSS and static files
└── .ipynb_checkpoints/         # Jupyter notebooks
    └── Bangalore House Prediction-checkpoint.ipynb/

```

## Model Information

The price prediction is powered by a Ridge Regression model that has been trained on Bangalore housing data. The model takes into account various features such as:

- Location (with locality-based price variations)
- Property size (square footage)
- Number of bedrooms (BHK)
- Number of bathrooms

The model is serialized and stored in `ridgemodel.pkl`, which is loaded by the Flask application to make real-time predictions.

## Contributing

Feel free to open issues or submit pull requests if you'd like to improve the project. All contributions are welcome!
