#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    scores = []

    # Read data from a TSV file and store it in a DataFrame.
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    # Select predictor variables X1 to X5 from the DataFrame and store them in 'x'.
    x = df.loc[:, "X1":"X5"]
    # Select the target variable 'Y' from the DataFrame and store it in 'y'.
    y = df.loc[:, "Y"]

    # Train linear regression model, including the intercept, when using all features (X1 to X5).
    model = linear_model.LinearRegression(fit_intercept=True).fit(x, y)
    # Append coefficient of determination when using all features (X1 to X5).
    scores.append(model.score(x, y))

    # Extract the names of predictor variables (features) except the last one (Y).
    features = df.columns[:-1]

    # Iterate through each feature and calculate the coefficient of determination for each feature.
    for f in features:
        # Create a DataFrame 'x' containing the current single feature.
        # Double square brackets are used to ensure that 'x' remains a DataFrame, not a Series.
        x = df[[f]] # or 'x = df[f].values.reshape(-1, 1)'
        model = linear_model.LinearRegression(fit_intercept=True).fit(x, y)
        scores.append(model.score(x, y))

    return scores


def main():
    scores = coefficient_of_determination()
    titles = "X X1 X2 X3 X4 X5".split()
    [print(f"R2-score with feature(s) {title}: {score:.2f}") for title, score in zip(titles, scores)]


if __name__ == "__main__":
    main()
