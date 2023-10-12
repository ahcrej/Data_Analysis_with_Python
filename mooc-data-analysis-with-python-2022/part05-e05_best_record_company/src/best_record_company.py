#!/usr/bin/env python3

import pandas as pd


def best_record_company():
    # Read the data from a tab-separated value file.
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    # Group the DataFrame by the 'Publisher' column.
    groups = df.groupby("Publisher")

    # Calculate the sum of the 'WoC' (Weeks on Chart) column for each publisher group.
    # Return the index of the 'Publisher' with the maximum sum using '.idxmax()'
    best_publisher = groups["WoC"].sum().idxmax()

    # Create a boolean mask to filter rows in the original DataFrame where the 'Publisher'
    # column matches the 'best_publisher' value.
    mask = (df["Publisher"] == best_publisher)

    # Return the DataFrame containing data for the best record company.
    df_best = df[mask]

    return df_best


def main():
    print(best_record_company())


if __name__ == "__main__":
    main()
