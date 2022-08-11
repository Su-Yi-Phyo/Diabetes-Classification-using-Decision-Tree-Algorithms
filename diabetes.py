import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import pickle

##model = pickle.load(open('Diabetes Classification.sav'),'rb')

st.title("Diabetes Testing System")
st.write("Do you want to test whether you have diabetes or not?")
st.write("Test HERE!")

glucose = st.text_input("Glucose Rate:")
bloodpressure = st.text_input("Blood Pressure:")
skin = st.text_input("Skin Thickness:")
insulin = st.text_input("Insulin:")
predigree = st.text_input("Diabetes Predigree Function:")
age = st.text_input("Age:")
submit = st.button("Submit")

##df=pd.dataframe{glucose,bloodpressure,skin,insulin,predigree,age}

##result=model.predict(df)

##if result==0:
    ##st.write("You don't have diabetes. Congratulations!")
##else:
    ##st.write("You have diabetes. Take care.")