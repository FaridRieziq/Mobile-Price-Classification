import numpy as np
from flask import Flask, request, render_template, redirect
import joblib

app = Flask(__name__)
model = joblib.load('models/trained_mobile_svm_updated_final.pkl')

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
    features = [np.array(form_data)]
    prediction = model.predict(features)
    return redirect('/result?prediction=' + str(prediction[0]))

if __name__ == '__main__':
    app.run(debug=False)
