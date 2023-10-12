#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    weekdays = {"ma": "Mon", "ti": "Tue", "ke": "Wed",
                "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    months = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
              "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
              "syys": 9, "loka": 10, "marras": 11, "joulu": 12}

    split_df = df["Päivämäärä"]
    split_df = split_df.dropna(how='all')
    split_df = split_df.str.split(expand=True)
    split_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    split_df["Hour"] = split_df["Hour"].str.split(":").str[0]
    split_df["Weekday"] = split_df["Weekday"].map(weekdays)
    split_df["Month"] = split_df["Month"].map(months)

    split_df = split_df.astype(
        {"Weekday": object, "Day": int, "Year": int, "Hour": int})

    return split_df


def split_date_continues():
    # Read data from .csv
    df1 = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Declare df2 using the 'split_date(df)' function
    df2 = split_date(df1)

    # Drop unnecessary rows and columns
    df1 = df1.dropna(how="all", axis=1).dropna(how="all", axis=0).drop("Päivämäärä", axis=1)
    # # As per above, methods can be chained instead of writing them line by line
    # # Note: 'inplace=True' hinders method chaining
    # df1.dropna(how="all", axis=1, inplace=True)
    # df1.dropna(how="all", axis=0, inplace=True)
    # df1.drop("Päivämäärä", axis=1, inplace=True)

    # Join the dataframes side by side by stating 'axis=1'
    joined_df = pd.concat([df2, df1], axis=1)

    return joined_df


def cycling_weather():
    cycling = split_date_continues()
    weather = pd.read_csv("src/kumpula-weather-2017.csv")
    merged = pd.merge(cycling, weather, left_on=[
                      "Year", "Month", "Day"], right_on=["Year", "m", "d"])
    merged =  merged.drop(["m", "d", "Time", "Time zone"], axis=1)

    return merged


def main():
    print(cycling_weather())


if __name__ == "__main__":
    main()
