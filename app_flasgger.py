#!/usr/bin/env python3.6
__author__ = 'Anjul Rajensdra Sharma'

from flask import Flask, request
import pickle
import pandas as pd
from flasgger import Swagger
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

streamHandlerFormatter = logging.Formatter('[ %(asctime)s - %(funcName)s():%(module)s.py:%(lineno)d - %(levelname)5s ] : %(message)s ', datefmt='%m/%d/%Y %I:%M:%S')
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(streamHandlerFormatter)
logger.addHandler(stream_handler)

app = Flask('__name__')
Swagger(app)

@app.route('/', methods=['GET'])
# welcome msz
def home():
    logger.info('Welcome.')
    return ("Welome to Anjul's first flask app.")

@app.route('/predict_class', methods=['GET'])
# return predicted class
def predict_class():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    # input values to predict the note authenticity
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    logger.info('variance:{} skewness:{} curtosis:{} entropy:{}'.format(variance, skewness, curtosis, entropy))
    prediction = model.predict([[variance, skewness, curtosis, entropy]])[0]

    if int(prediction) == int(0):
        result = "Anjul's model predicted this note is Fake."
    elif int(prediction) == int(1):
        result = "Anjul's model predicted this note is Real."
    else:
        result = "Anjul's model not able to predict, got value: {}".format(prediction)

    logger.info('RESULT: {}'.format(result))
    return result

@app.route('/predict_prob', methods=['GET'])
# return predicted class
def predict_prob():
    # input values to predict the note authenticity
    """Let's Authenticate the Banks Note
    It's gives the prob of being Fake or Real.
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    logger.info('variance:{} skewness:{} curtosis:{} entropy:{}'.format(variance, skewness, curtosis, entropy))
    prediction = model.predict_proba([[variance, skewness, curtosis, entropy]])[0]
    result = "Anjul's model predictions:- Fake:{} Real:{}".format(prediction[0], prediction[1])
    logger.info('RESULT: {}'.format(result))
    return result

@app.route('/predict_file', methods=['POST'])
# return predicted class
def predict_file():
    # input file to predict the note authenticity
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    testfile = request.files.get("file")
    logger.info('input file:{}'.format(testfile))

    test = pd.read_csv(testfile)
    prediction = model.predict(test)
    result = "Anjul's model predictions: {}".format(prediction)
    logger.info('RESULT: {}'.format(result))
    return result

if __name__ == '__main__':
    r'''
    # for testing
    # start run flasgger_app.py
    # and check http://0.0.0.0:8000/apidocs/'''

    PORT = 8000
    IP = '127.0.0.1'
    DEBUG = False

    logger.info('Loading ML model: model/authentication_classifier.pkl ')
    model = pickle.load(open('model/authentication_classifier.pkl', 'rb'))

    logger.info('Server Started at {}:{} '.format(IP, PORT))
    app.run(host=IP , port=PORT, debug=DEBUG)