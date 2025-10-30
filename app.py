import streamlit as st

st.title("Welcome to Your Streamlit App!")
name = st.text_input("Enter your name:")
if st.button("Say Hello"):
    if name:
        st.success(f"Hello, {name}! Welcome to the Streamlit app.")
    else:
        st.warning("Please enter your name above.")
