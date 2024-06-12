# Create new features
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Month'] = df['Date'].dt.month

# Encode categorical variables
df['Promotion'] = df['Promotion'].map({'Yes': 1, 'No': 0})

# Drop unnecessary columns
df.drop(['Date', 'Product'], axis=1, inplace=True)

# Display updated data
print(df.head())
