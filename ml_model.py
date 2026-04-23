from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([40, 50, 60, 70, 80])

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
hours = np.array([[6]])
prediction = model.predict(hours)

print("Predicted Marks:", prediction[0])
