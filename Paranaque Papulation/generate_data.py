import numpy as np
import json

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

# =========================================
# 1. ACTUAL DATA
# =========================================

years = np.array([
    1990,
    2000,
    2010,
    2015,
    2020,
    2024
]).reshape(-1, 1)

population = np.array([
    308236,
    449811,
    588126,
    665822,
    689992,
    703245
])

# =========================================
# 2. LINEAR REGRESSION
# =========================================

linear_model = LinearRegression()

linear_model.fit(
    years,
    population
)

linear_pred_train = linear_model.predict(years)

# =========================================
# 3. POLYNOMIAL REGRESSION
# =========================================

degree = 2

poly_model = make_pipeline(
    PolynomialFeatures(degree),
    LinearRegression()
)

poly_model.fit(
    years,
    population
)

# =========================================
# 4. SMOOTH CURVE
# =========================================

x_range = np.linspace(
    1990,
    2030,
    100
).reshape(-1, 1)

poly_curve = poly_model.predict(x_range)

# =========================================
# 5. FUTURE PREDICTION
# =========================================

future_year = np.array([[2029]])

linear_prediction = linear_model.predict(
    future_year
)

poly_prediction = poly_model.predict(
    future_year
)

# =========================================
# 6. MODEL ACCURACY
# =========================================

mse_linear = mean_squared_error(
    population,
    linear_pred_train
)

mse_poly = mean_squared_error(
    population,
    poly_model.predict(years)
)

# =========================================
# 7. SAVE DATA TO JSON
# =========================================

data = {

    "years":
        years.flatten().tolist(),

    "population":
        population.tolist(),

    "linearY":
        linear_pred_train.tolist(),

    "polyX":
        x_range.flatten().tolist(),

    "polyY":
        poly_curve.tolist(),

    "linearPredictionY":
        float(linear_prediction[0]),

    "polyPredictionY":
        float(poly_prediction[0]),

    "mseLinear":
        float(mse_linear),

    "msePoly":
        float(mse_poly)
}

with open(
    "population_data.json",
    "w"
) as file:

    json.dump(
        data,
        file
    )

# =========================================
# 8. PRINT RESULTS
# =========================================

print("\n===== RESULTS =====")

print(
    "Linear Prediction 2029:",
    int(linear_prediction[0])
)

print(
    "Polynomial Prediction 2029:",
    int(poly_prediction[0])
)

print("\n===== MSE =====")

print(
    "Linear MSE:",
    int(mse_linear)
)

print(
    "Polynomial MSE:",
    int(mse_poly)
)

print("\nJSON file created!")