# save this as app.py

import streamlit as st

# Title
st.title('NBA Win Prediction')

# Header
st.header('NBA Win Prediction')

# Text
st.write("This is a simple Streamlit app to get you started.")

# Text input
name = st.text_input("What's your name?")

# Search for Columns in Data
st.write("This is a simple Streamlit app to get you started.")
search = st.text_input('Enter  Here')

# Button
if st.button('Greet Me'):
    st.success(f"Hello, {name}! 👋")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.info("You can add more pages here later!")

# Simple Chart
st.subheader('Simple Chart')
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [5, 10, 15, 20, 25]
}
st.line_chart(data)
