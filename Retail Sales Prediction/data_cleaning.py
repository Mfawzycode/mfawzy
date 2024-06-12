import pandas as pd

# Load the dataset
df = pd.read_csv('retail_sales_data.csv')

# Handle missing values
df.dropna(inplace=True)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Display cleaned data
print(df.head())
