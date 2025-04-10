import streamlit as st
import numpy as np
import pandas as pd

st.title('Hello Streamlit')

df = pd.DataFrame({
    'firstcoloumn':[1,2,3,4],
    'secondcoloumn':[10,20,30,40]
})

st.write("Here is the dataframe")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello, {name}")