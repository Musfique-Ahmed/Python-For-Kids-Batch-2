import streamlit as st

st.title("Simple Input Display App")
user_input = st.text_input("Enter something:")
if user_input:
    st.write("You entered:", user_input)