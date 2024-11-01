# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Given data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)  # Days
y = np.array([23, 23, 24, 22, 21, 19])  # Data points

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Forecast for the next day (day 7)
y_pred = model.predict([[7]])

# Display the results
print(f"Slope (beta_1): {model.coef_[0]}")
print(f"Intercept (beta_0): {model.intercept_}")
print(f"Forecast for day 7: {y_pred[0]}")

# Optional: Plot the data points and the regression line
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Day')
plt.ylabel('Value')
plt.legend()
plt.show()