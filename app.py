import streamlit as st
import pandas as pd

st.title("Student Data Analysis")

data = {
    'Name': ['Sarthak', 'Rahul', 'Amit'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

st.write("Dataset:")
st.write(df)

st.write("Average Marks:", df['Marks'].mean())
st.write("Maximum Marks:", df['Marks'].max())
st.write("Minimum Marks:", df['Marks'].min())