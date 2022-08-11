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

preganant=st.number_input("Number of times preganant:")
glucose = st.number_input("Glucose Rate:")
bloodpressure = st.number_input("Blood Pressure:")
skin = st.number_input("Skin Thickness:")
insulin = st.number_input("Insulin:")
predigree = st.number_input("Diabetes Predigree Function:")
age = st.number_input("Age:")
submit = st.button("Submit")

data = [preganant,glucose,bloodpressure,skin,insulin,predigree,age]
df=pd.DataFrame(data)

result=model.predict(df)

if result==0:
    st.write("You don't have diabetes. Congratulations!")
else:
    st.write("You have diabetes. Take care.")
