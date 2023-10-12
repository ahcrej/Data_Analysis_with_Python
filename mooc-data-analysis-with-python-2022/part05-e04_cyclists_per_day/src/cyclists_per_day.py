#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
# matplotlib.use("TKAgg")


def split_date(df):
    weekdays = {"ma": "Mon", "ti": "Tue", "ke": "Wed",
                "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    months = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
              "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
              "syys": 9, "loka": 10, "marras": 11, "joulu": 12}

    df_split = df["Päivämäärä"]
    df_split = df_split.dropna(how='all')
    df_split = df_split.str.split(expand=True)
    df_split.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df_split["Hour"] = df_split["Hour"].str.split(":").str[0]
    df_split["Weekday"] = df_split["Weekday"].map(weekdays)
    df_split["Month"] = df_split["Month"].map(months)

    df_split = df_split.astype(
        {"Weekday": object, "Day": int, "Year": int, "Hour": int})

    return df_split


def split_date_continues():
    # Read data from .csv
    df1 = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Declare df2 using the 'split_date(df)' function
    df2 = split_date(df1)

    # Drop unnecessary rows and columns
    df1 = df1.dropna(how="all", axis=1).dropna(
        how="all", axis=0).drop("Päivämäärä", axis=1)

    # Join the dataframes side by side by stating 'axis=1'
    joined_df = pd.concat([df2, df1], axis=1)

    return joined_df


def cyclists_per_day():
    df = split_date_continues()
    # Drop unnecesary columns
    df = df.drop(["Hour", "Weekday"], axis=1)
    df = df.groupby(["Year", "Month", "Day"]).sum()

    return df


def main():
    df = cyclists_per_day()
    
    # Select all columns in the August 2017 '[('year', 'month'), :]
    df_counts = df.loc[(2017, 8), :]
    print(df_counts)

    # Plot each column with its corresponding column name as label
    [df_counts[col].plot(label=col) for col in df_counts.columns]

    # Plots a line for each station, representing the number of cyclists each day of August 2017
    plt.plot(df_counts)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
