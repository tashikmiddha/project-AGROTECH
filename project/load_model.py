# load_model.py
import joblib
import os

model = joblib.load('/Users/tashikmiddha/Desktop/practice/AGROTECH/myenv/yield/project/model.pkl')
model2=joblib.load('/Users/tashikmiddha/Desktop/practice/AGROTECH/myenv/yield/project/model2.pkl')
model3=joblib.load('/Users/tashikmiddha/Desktop/practice/AGROTECH/myenv/yield/project/model3.pkl')
def predict_crop(data):
    prediction = model.predict([data])
    return prediction[0]

def predict_watering(data):
    prediction=model2.predict([data])
    return prediction[0]

def predict_fertilizer(data):
    prediction=model3.predict([data])
    return prediction[0]
