# Project-1-Python-ML-Flask
Classifier development using Python &amp; deployment using Flask
# Electricity Load Type Prediction

This project involves predicting the load type in a steel factory using a machine learning model. The model is deployed as a web application using Flask.

## Project Structure

- `app.py`: The Flask application file.
- `templates/index.html`: The main HTML file for the web interface.
- `static/`: Contains the CSS and JavaScript files for styling and functionality.
- `model/`: Contains the trained model file (`e.g. model.joblib`).

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Required Python libraries listed in `requirements.txt`

### Setup

1. **Clone the repository or copy the project directory:**
This step is needed if you have the Project hosted remotely (like GitHub) and wish to copy it to your local device for using the application/changing it.
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

    Alternatively, you can copy the project folder directly to your desired location.

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask application:**

    ```bash
    python app.py
    ```

2. **Open a web browser and navigate to:**

    ```
    http://127.0.0.1:5000
    ```

3. **Using the Web App:**
    - The home page includes sections like Home, About Us, and Model.
    - Click on the "Model" section to scroll down to the form where you can input values for the predictors.
    - Enter the values and click "Predict" to see the predicted load type.
    - Use the "Reset" button to clear the input fields.

### Note

Ensure that the `model.joblib` file is in the `model/` directory. This file contains the trained machine learning model used for predictions.

## Acknowledgments

- This project uses a template from [BootstrapMade](https://bootstrapmade.com/onepage-multipurpose-bootstrap-template/).
