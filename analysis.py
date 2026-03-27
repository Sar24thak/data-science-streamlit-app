import pandas as pd

# Sample dataset
data = {
    'Name': ['Sarthak', 'Rahul', 'Amit'],
    'Marks': [85, 90, 78]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Dataset:\n", df)

# Basic analysis
print("\nAverage Marks:", df['Marks'].mean())
print("Maximum Marks:", df['Marks'].max())
print("Minimum Marks:", df['Marks'].min())