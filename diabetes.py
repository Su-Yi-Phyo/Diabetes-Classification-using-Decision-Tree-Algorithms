import streamlit as st
import pandas as pd
import numpy as np
import joblib 

model = joblib.load('Diabetes Classification.sav')

st.markdown(
  f"""
    <style>
     .stApp {{
        background-image: url("https://img.freepik.com/premium-photo/background-diabetic-disease-concept-with-copy-space-world-diabetes-day-banner_132254-879.jpg?w=2000");
        background-attachment: fixed;
        background-size: cover}}
     </style>
  """,
unsafe_allow_html=True)

st.title("Diabetes Testing System")
st.write("Do you want to test whether you have diabetes or not?")
st.write("Test HERE!")

pregnant=st.number_input("Number of times preganant:")
glucose = st.number_input("Glucose Rate:")
bloodpressure = st.number_input("Blood Pressure:")
skin = st.number_input("Skin Thickness:")
insulin = st.number_input("Insulin:")
bmi = st.number_input("BMI:")
predigree = st.number_input("Diabetes Predigree Function:")
age = st.number_input("Age:")
submit = st.button("Submit")

df=pd.DataFrame({'Pregnancies': pregnant, 'Glucose': glucose, 'BloodPressure': bloodpressure, 'SkinThickness': skin, 'Insulin': insulin, 'BMI': bmi, 'DiabetesPedigreeFunction': predigree, 'Age': age}, index=[0])

result=model.predict(df)

if result == [0]:
  st.markdown(f'<h1 style="color:green;font-size:24px;">You do not have diabetes. Congratulations!</h1>', unsafe_allow_html=True)
elif result == [1]:
  st.markdown(f'<h1 style="color:green;font-size:24px;">You have diabetes. Take care!</h1>', unsafe_allow_html=True)
else:
  st.markdown(f'<h1 style="color:green;font-size:24px;">Cannot define</h1>', unsafe_allow_html=True)
