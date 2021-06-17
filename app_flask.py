#!/usr/bin/env python3.6
__author__ = 'Anjul Rajensdra Sharma'

from flask import Flask, request
import pickle
import pandas as pd

app = Flask('__name__')

@app.route('/', methods=['GET'])
# welcome msz
def welcome():
    return ("Welome to Anjul's first flask app.")

@app.route('/predict_class', methods=['GET'])
# return predicted class
def predict_class():
    # input values to predict the note authenticity
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    prediction = model.predict([[variance, skewness, curtosis, entropy]])[0]

    if prediction == 0:
        return "Anjul's model predict this note is Fake."
    if prediction == 1:
        return "Anjul's model predict this note is Real."
    else:
        return "Anjul's model not able to predict, got value: {}".format(prediction)

@app.route('/predict_prob', methods=['GET'])
# return predicted class
def predict_prob():
    # input values to predict the note authenticity
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    prediction = model.predict_proba([[variance, skewness, curtosis, entropy]])[0]
    
    return "Anjul's model predictions:\nprob of being Fake note:{}\nprob of being Real note:{}".format(prediction[0], prediction[1])

@app.route('/predict_file', methods=['POST'])
# return predicted class
def predict_file():
    # input file to predict the note authenticity
    testfile = request.files.get("file")
    test = pd.read_csv(testfile)
    prediction = model.predict(test)
    return "Anjul's model predictions: {}".format(prediction)

if __name__ == '__main__':
    model = pickle.load(open('model/authentication_classifier.pkl', 'rb'))
    app.run()