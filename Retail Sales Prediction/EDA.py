import matplotlib.pyplot as plt
import seaborn as sns

# Sales trend over time
plt.figure(figsize=(10, 5))
df.groupby('Date')['Sales'].sum().plot()
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Sales distribution by store
plt.figure(figsize=(10, 5))
sns.boxplot(x='Store', y='Sales', data=df)
plt.title('Sales Distribution by Store')
plt.xlabel('Store')
plt.ylabel('Sales')
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
