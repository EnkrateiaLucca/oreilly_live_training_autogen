# filename: plot_chart.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Replace 'housing_prices_lisbon.csv' with the path to your CSV file
file_path = 'housing_prices_lisbon.csv'

# Load the data from a CSV file
data = pd.read_csv(file_path)

# Assume that the CSV file has two columns: 'Year' and 'Price'
X = data['Year'].values.reshape(-1, 1)
y = data['Price'].values

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict the price for 2023
X_2023 = np.array([2023]).reshape(-1, 1)
y_2023 = model.predict(X_2023)

# Plot the historical data
plt.bar(data['Year'], data['Price'], color='blue')

# Plot the predicted price for 2023
plt.bar(X_2023, y_2023, color='red')

plt.title('Housing Prices in Lisbon, Portugal')
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()