#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use("Agg")
matplotlib.use("TkAgg")


def fit_line(x, y):
    # Create a LinearRegression model with an intercept and fit it to the input data (x, y).
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)

    # Create a range of x-values from 0 to 10 with 20 evenly spaced points.
    xfit = np.linspace(0, 10, 20)
    # Calculate the corresponding y-values by using the trained model to make predictions with the xfit values.
    yfit = model.predict(xfit[:, np.newaxis])

    return model.coef_[0], model.intercept_


def main():
    n = 20
    x = np.linspace(0, 10, n)  # Generate an array of x-values.
    y = x*2 + 2 * np.random.randn(n)  # Generate y-values with noise.

    # 'fit_line(x, y)' gets its slope and intercept.
    coefficient, intercept = fit_line(x, y)

    print(f"Slope: {coefficient}")
    print(f"Intercept: {intercept}")

    # Calculate y-values of the linear regression model.
    yfit = coefficient*x + intercept

    # Create a scatter plot of data points using circular markers ('o')
    plt.plot(x, y, 'o')
    # Plot the linear regression model.
    plt.plot(x, yfit, color="black")

    # # The following will draw as many line segments as there are columns in matrices x and y
    # plt.plot(np.vstack([x, x]), np.vstack([y, yfit]), color="red")
    
    plt.show()


if __name__ == "__main__":
    main()
