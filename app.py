import numpy as np
from flask import Flask, request, render_template, redirect
import joblib

app = Flask(__name__)

# Load models
svm_model = joblib.load('models/trained_mobile_svm_updated_final.pkl')
decision_tree_model = joblib.load('models/decisionTreeClassifier.pkl')
lgr_model = joblib.load('models/trained_mobile_logisticRegressor.pkl')
random_forest_model = joblib.load('models/randomForest.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    prediction = request.args.get('prediction')
    return render_template('result.html', prediction=prediction)

@app.route('/predict', methods=['POST'])
def predict():
    form_data = [x for x in request.form.values()]
    features = [np.array(form_data[:-1])]  # Exclude the algorithm selection from features
    algorithm = form_data[-1]  # Get the selected algorithm
    if algorithm == 'svm':
        model = svm_model
    elif algorithm == 'decision_tree':
        model = decision_tree_model
    elif algorithm == 'random_forest':
        model = random_forest_model
    else:
        return redirect('/result?prediction=Invalid algorithm')

    prediction = model.predict(features)
    return redirect('/result?prediction=' + str(prediction[0]))

if __name__ == '__main__':
    app.run(debug=False)
