# -*- coding: utf-8 -*-
"""SMS Spam Prediction Using BERT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uB43Fb7M0N-C0JnFKZOFjCtUVnhZS_UW
"""

#!pip3 install --quiet tensorflow
#!pip3 install --quiet tensorflow_text

import os, sys, getopt
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from matplotlib import pyplot as plt
import seaborn as sn

def readData(file='spam.csv'):
    df = pd.read_csv('spam.csv', encoding = "ISO-8859-1")
    df.head(5)

    df.groupby('v1').describe()

    df['v1'].value_counts()

    df_spam = df[df['v1']=='spam']
    df_spam.shape

    df_ham = df[df['v1']=='ham']
    df_ham.shape

    df_ham_downsampled = df_ham.sample(df_spam.shape[0])
    df_ham_downsampled.shape

    df_balanced = pd.concat([df_ham_downsampled, df_spam])
    df_balanced.shape

    df_balanced['v1'].value_counts()

    df_balanced['spam']=df_balanced['v1'].apply(lambda x: 1 if x=='spam' else 0)
    df_balanced.sample(5)


    X_train, X_test, y_train, y_test = train_test_split(df_balanced['v2'],df_balanced['spam'], stratify=df_balanced['spam'])

    X_train.head(5)

    return X_train, X_test, y_train, y_test

def fitModel(X_train, y_train):
    bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
    bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")

    # Bert layers
    text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
    preprocessed_text = bert_preprocess(text_input)
    outputs = bert_encoder(preprocessed_text)

    # Neural network layers
    l = tf.keras.layers.Dropout(0.1, name="dropout")(outputs['pooled_output'])
    l = tf.keras.layers.Dense(1, activation='sigmoid', name="output")(l)

    # Use inputs and outputs to construct a final model
    model = tf.keras.Model(inputs=[text_input], outputs = [l])

    METRICS = [
        tf.keras.metrics.BinaryAccuracy(name='accuracy'),
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall')
    ]

    model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=METRICS)

    model.summary()

    model.fit(X_train, y_train, epochs=10)

    return model

def testModel(model, X_test, y_test):
    model.evaluate(X_test, y_test)

    y_predicted = model.predict(X_test)
    y_predicted = y_predicted.flatten()

    y_predicted = np.where(y_predicted > 0.5, 1, 0)
    y_predicted

    cm = confusion_matrix(y_test, y_predicted)

    sn.heatmap(cm, annot=True, fmt='d')
    plt.xlabel('Predicted')
    plt.ylabel('Truth')

    print(classification_report(y_test, y_predicted))


if __name__ == '__main__':
    train = False
    dataFile = 'spam.csv'
    modelFile = './SMSSpamModel'
    saveModel = True

    try:
        opts, args = getopt.getopt(sys.argv[1:], 
                        "t:r:m:s", 
                        ["train=", "read=", "model=", "--save_model"])
    except getopt.GetoptError:
        print('Incorrect command')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-t', '--train'):
            train = bool(arg)
        if opt in ('-r', '--read'):
            dataFile = arg
        if opt in ('-m', '--model'):
            modelFile = arg
        if opt in ('-s', '--save'):
            saveModel = bool(arg)

    X_train, X_test, y_train, y_test = readData(dataFile)
    if train:
        print("Training data")
        model = fitModel(X_train, y_train)
    else:
        print("Reading Model")
        model = tf.keras.models.load_model(modelFile)
    testModel(model, X_test, y_test)

    reviews = [
        "http://paperok.ml - Professional academic help for you!",
        "You know what the warmer weather means...it's burn season! 🔥 Just ask me to roast one of ur friends. I'll take care of the rest 😎",
        "Your package is waiting for delivery. Please confirm the settlement of $19.99 on the following link: http://aka.ms/adfuyiwy",
        "NHS: we have identified that you are eligible to apply for your vaccine. For more information and apply, follow here: application-ukform.com",
        "Hi, Darya. When I test the iOS telemetry today, I found the same issue with \"New Chat Open\" event. I've ready report a bug for that."
    ]
    print(model.predict(reviews))

    if saveModel:
        model.save(modelFile)


    


