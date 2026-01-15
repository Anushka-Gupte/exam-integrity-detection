import streamlit as st
import pandas as pd
import numpy as np
import pickle
import shap
import matplotlib.pyplot as plt

model = pickle.load(open('exam-integrity-detection.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

st.header('Online Exam Cheating Detection System')

st.subheader('Global Feature Importance')

from sklearn.model_selection import train_test_split
dataset = pd.read_csv('./data/online_exam_cheating.csv')
X = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1].values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
explainer = shap.Explainer(model,X_train)
shap_values = explainer(X_train)
fig, ax = plt.subplots()
shap.plots.bar(shap_values[:,:,1],max_display=10,show=False)
st.pyplot(fig)
st.write("""
        This plot shows which features strongly influence the model's prediction overall for predicting cheating.
         Larger mean SHAP values indicate features like Answer change rate and fast answer ratio are the most important drivers
         influencing prediction of Cheating in an online exam. 
        """)

st.subheader('Input Features')
avg = st.number_input('Average seconds spent per question',value=10.0,step=0.1)
acc = st.number_input('Overall exam accuracy',value=0.1,step=0.1)
fastans = st.number_input('Questions answered too fast',value=0.1,step=0.1)
changeans = st.number_input('Average answer changes per question',value=0,step=1)

st.subheader('Prediction Result')

if st.button('Predict'):
    X_inp = np.array([[avg,acc,fastans,changeans]])
    X_inp[:,:1] = scaler.transform(X_inp[:,:1])
    res = model.predict(X_inp)
    if res == 0:
       st.subheader('No cheating')
    else:
       st.subheader('Cheating')

