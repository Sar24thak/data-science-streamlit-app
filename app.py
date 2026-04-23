import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Title
st.title("📊 Student Data Analysis & Prediction")

# ------------------ DATASET ------------------
data = {
    'Name': ['Sarthak', 'Rahul', 'Amit'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

st.subheader("📋 Dataset")
st.dataframe(df)

# ------------------ BASIC ANALYSIS ------------------
st.subheader("📈 Analysis")

st.write("Average Marks:", df['Marks'].mean())
st.write("Maximum Marks:", df['Marks'].max())
st.write("Minimum Marks:", df['Marks'].min())

# ------------------ MACHINE LEARNING ------------------
st.subheader("🤖 Marks Prediction (ML Model)")

# Slider input
hours = st.slider("Select Study Hours", 1, 10, 5)

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([40, 50, 60, 70, 80])

# Model training
model = LinearRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[hours]])

# Output
st.success(f"Predicted Marks for {hours} hours of study: {prediction[0]:.2f}")
