from flask import Flask, jsonify, request
import tensorflow as tf
import tensorflow_text as text

app = Flask(__name__)
model = tf.keras.models.load_model('./SMSSpamModel.H5')

@app.route('/check_spam', methods = ['POST'])
def check_spam():
    predict = model.predict(request.get_json())
    return jsonify(predict.flatten().tolist())

if __name__ == '__main__':
    app.run(debug = True)