import streamlit as st

st.title("This is my 1st streamlit app")
st.write("Hi this is Musfique!")

st.write("this is a test")

name = st.text_input("ENter your name: ")
color = st.text_input("ENter your fav color: ")
st.write(f"hello {name}, your fav color is {color}")

st.number_input("enter number")
st.text_area("enter paragraph")
st.selectbox("chose", ['a', 'b', 'c'])

st.checkbox("check this")

st.button("click me")
st.radio("Selecct", ["a", "b", "c"])

st.file_uploader("Upload file")

st.image("image.png")