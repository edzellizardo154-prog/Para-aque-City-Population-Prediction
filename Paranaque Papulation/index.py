# population_prediction.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Example historical population data (Year, Population in thousands)
# Replace this with your actual data
years = np.array([2000, 2005, 2010, 2015, 2020]).reshape(-1, 1)
population = np.array([50, 55, 65, 70, 80])  # in thousands

# 1. Linear Regression (Least Squares Method)
linear_model = LinearRegression()
linear_model.fit(years, population)

# Predict population in 5 years from last year (2025)
future_year = np.array([[2025]])
linear_prediction = linear_model.predict(future_year)
print(f"Linear Regression Prediction for 2025: {linear_prediction[0]:.2f} thousand people")

# 2. Polynomial Regression (Curve Fitting)
degree = 2  # You can change degree for more complex curves
poly_features = PolynomialFeatures(degree=degree)
years_poly = poly_features.fit_transform(years)

poly_model = LinearRegression()
poly_model.fit(years_poly, population)

# Predict population in 5 years using polynomial model
future_year_poly = poly_features.transform(future_year)
poly_prediction = poly_model.predict(future_year_poly)
print(f"Polynomial Regression Prediction for 2025: {poly_prediction[0]:.2f} thousand people")

# 3. Plotting the results
plt.scatter(years, population, color='blue', label='Actual Data')

# Linear regression line
plt.plot(years, linear_model.predict(years), color='green', label='Linear Regression')

# Polynomial regression curve
years_range = np.arange(2000, 2030).reshape(-1, 1)
plt.plot(years_range, poly_model.predict(poly_features.transform(years_range)), color='red', label='Polynomial Regression')

plt.scatter(future_year, linear_prediction, color='green', marker='x', s=100, label='Linear Prediction 2025')
plt.scatter(future_year, poly_prediction, color='red', marker='x', s=100, label='Polynomial Prediction 2025')

plt.xlabel('Year')
plt.ylabel('Population (thousands)')
plt.title('City Population Prediction')
plt.legend()
plt.grid(True)
plt.show()