#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():
    # Read the suicide data from a CSV file into a Pandas DataFrame.
    df = pd.read_csv("src/who_suicide_statistics.csv")

    # Remove unecessary columns from the DataFrame.
    df = df.drop(["year", "sex", "age"], axis=1)

    # Add and calculate the 'suicide_ratio' column by dividing the 'suicides_no' by the 'population' for each row.
    df["suicide_ratio"] = df["suicides_no"] / df["population"]

    # Group the data in 'df' by the 'country' column.
    results = df.groupby("country")

    # Calculate the mean of the 'suicide_ratio' for each country.
    return results["suicide_ratio"].mean()


def main():
    print(suicide_fractions())


if __name__ == "__main__":
    main()
