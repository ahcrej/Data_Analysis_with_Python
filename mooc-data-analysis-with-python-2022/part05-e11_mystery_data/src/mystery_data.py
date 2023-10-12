#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


def mystery_data():
    # Read data from a TSV file and store it in a DataFrame.
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")

    # Select predictor variables X1 to X5 from the DataFrame and store them in 'x'.
    x = df.loc[:, "X1":"X5"]

    # Select the target variable 'Y' from the DataFrame and store it in 'y'.
    y = df.loc[:, "Y"]

     # Create a LinearRegression model with no intercept term.
    model = LinearRegression(fit_intercept=False)
    
    # Fit the model to the predictor variables 'x' and the target variable 'y.'
    model.fit(x, y)

    return model.coef_


def main():
    coefficients = mystery_data()
    [print(f"Coefficient of X{i+1} is {coeff}")for i, coeff in enumerate(coefficients)]


if __name__ == "__main__":
    main()
