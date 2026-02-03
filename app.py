import streamlit as st
import pandas as pd
import numpy as np
import pickle
import shap
import matplotlib.pyplot as plt

model = pickle.load(open('classifier.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))
transformer = pickle.load(open('transformer.pkl','rb'))
imputer = pickle.load(open('imputer.pickle','rb'))

st.header('Online Exam Cheating Detection System')


st.subheader('Input Features')
uploaded_file = st.file_uploader('Enter co-ordinates of images',type='csv')
if uploaded_file is not None:
   test = pd.read_csv(uploaded_file,header=None)
   test[[21,30]] = imputer.transform(test[[21,30]])
   test = np.array(transformer.transform(test))
   test[:,[11,12,13,14,15,16,17,18,19,20,21,22,
           23,38,39,40,41,42,43]] = scaler.transform(test[:,[11,12,13,14,15,16,17,18,19,20,21,22,
                                                          23,38,39,40,41,42,43]])

st.subheader('Prediction Result')

if st.button('Predict'):
    res = model.predict(test)
    i = 0
    for r in res:
      if r == 0:
         st.markdown(f'### Student {i} No cheating')
         i += 1
         st.divider()
      else:
         st.markdown(f'### Student {i} Cheating')
         i += 1
         st.divider()

