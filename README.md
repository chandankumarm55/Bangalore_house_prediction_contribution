# House Price Predictor

This is a web application built using Flask and a machine learning model to predict house prices based on several features such as location, number of bedrooms (BHK), number of bathrooms, and square footage. The model was trained using a Ridge Regression model and predicts house prices based on the inputs provided by users.

## Features

- Select a location from a dropdown menu.
- Enter the number of BHK (Bedrooms, Hall, and Kitchen).
- Enter the number of bathrooms.
- Enter the total square footage.
- Get a predicted house price based on these inputs.

## Demo

After starting the application, open your browser and go to:
http://127.0.0.1:5001


You will be presented with a simple form where you can enter your inputs, and the application will predict the price.

## Technologies Used

- **Flask**: Python micro web framework for serving the application.
- **Pandas**: For data manipulation and loading CSV data.
- **Scikit-learn**: Machine learning library used to build and load the Ridge Regression model.
- **Jinja2**: Flask's templating engine for rendering HTML.

house-price-predictor/
│
├── Cleaned.csv                 # Cleaned data file
├── RidgeModel.pkl              # Trained Ridge Regression model
├── main.py                     # Main Flask app file
├── templates/
│   └── index.html              # HTML template
├── static/                     # Any static files like CSS or images
└── README.md                   # Project README file
