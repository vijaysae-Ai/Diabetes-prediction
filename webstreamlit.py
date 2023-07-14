# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:16:19 2023

@author: vijay
"""

import numpy as np
import pickle 
import streamlit as st

load_model=pickle.load(open('C:/Users/vijay/Videos/deploy/model.sav','rb'))

def diabeties_prediction(data):
    array_data=np.asarray(data)
    reshape_data=array_data.reshape(1,-1)
    predii=load_model.predict(reshape_data)
    if predii[0]==1:
        return 'has diabetes'
    else:
        return 'no diabetest'
    
def main():
    st.title('Diabetes prediction')
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('BloodPressure value')
    SkinThickness=st.text_input('SkinThickness')
    Insulin=st.text_input('Insulin value')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('DihealthyPedigreeFunction')
    Age=st.text_input('Person Age')
    
    diagnosis=''
    if st.button('Diabetes Test Results'):
        diagnosis=diabeties_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age ])
        
    st.success(diagnosis)
    
    
    
if __name__=='__main__':
    main()