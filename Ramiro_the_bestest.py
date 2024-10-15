import streamlit as st
import pandas as pd

# Title of the app
st.title('Peace Engineer Compliment Generator')

# User text input
user_input = st.text_input('Enter your name:')

# Display a custom message based on user input
if user_input:
    st.write(f"{user_input} is an awesome and amazing peace engineer")
