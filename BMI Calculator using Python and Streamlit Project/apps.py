import streamlit as st
import pandas as pd

st.title('BMI Calculator')

# Weight & height input
height = st.slider('Enter your height (in cm)' , 100, 250, 170)
weight = st.slider('Enter your weight (in kgs)' , 40, 150, 70)

# Calculate BMI
bmi = weight / ((height/100)**2)

# Display BMI
st.write(f"Your BMI is {bmi:.2f}")

# Categorize BMI
if bmi < 18.5:
    st.write('You are underweight')
elif bmi >= 18.5 and bmi < 25:
    st.write('You are normal weight')
elif bmi >= 25 and bmi < 30:
    st.write('You are overweight')
elif bmi >= 30:
    st.write("You are obeslity")
