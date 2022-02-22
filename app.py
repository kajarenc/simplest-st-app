import streamlit as st

st.title("Hello World")

x = st.slider("input x value", 0, 100)

st.write(x ** 2)


st.write(st.secrets)
