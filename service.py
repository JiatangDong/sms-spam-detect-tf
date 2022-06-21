import os, sys, getopt
from flask import Flask, jsonify, request
import tensorflow as tf
import tensorflow_text as text

app = Flask(__name__)

@app.route('/check_spam', methods = ['POST'])
def check_spam():
    predict = model.predict(request.get_json())
    return jsonify(predict.flatten().tolist())

if __name__ == '__main__':
    modelFile = './SMSSpamModel'
    debug = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:d:", ["model=", "debug="])
    except getopt.GetoptError:
        print('Incorrect command')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-m', '--model'):
            modelFile = arg
        if opt in ('-d', '--debug'):
            debug = bool(arg)

    model = tf.keras.models.load_model(modelFile)
    app.run(debug = debug)