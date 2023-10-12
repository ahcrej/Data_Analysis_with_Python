#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    weekdays = {"ma": "Mon", "ti": "Tue", "ke": "Wed",
                "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    months = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
              "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
              "syys": 9, "loka": 10, "marras": 11, "joulu": 12}

    df_split = df["Päivämäärä"]
    df_split.dropna(how='all', inplace=True)
    df_split = df_split.str.split(expand=True)
    df_split.columns = ["Weekday", "Day", "Month", "Year", "Time"]
    df_split["Time"] = df_split["Time"] + ":00"
    df_split["Weekday"] = df_split["Weekday"].map(weekdays)
    df_split["Month"] = df_split["Month"].map(months)

    df_split = df_split.astype(
        {"Weekday": object, "Day": int, "Year": int})

    return df_split


def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all", axis=0).dropna(how="all", axis=1)
    df2 = split_date(df)
    df2["Timestamp"] = df2["Year"].astype(str) + '-' + df2["Month"].astype(str) + '-' + df2["Day"].astype(str) + ' ' + df2["Time"]
    df["Timestamp"] = pd.to_datetime(df2["Timestamp"])
    df = df.drop(["Päivämäärä"], axis=1).set_index("Timestamp")

    return df


def main():
    print(bicycle_timeseries())


if __name__ == "__main__":
    main()
