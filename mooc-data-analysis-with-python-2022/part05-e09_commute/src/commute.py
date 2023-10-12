#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use("Agg")
matplotlib.use("TkAgg")


def split_date(df):
    weekdays = {"ma": "Mon", "ti": "Tue", "ke": "Wed",
                "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    months = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
              "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
              "syys": 9, "loka": 10, "marras": 11, "joulu": 12}

    df_split = df["Päivämäärä"]
    df_split.dropna(how='all', inplace=True)
    df_split = df_split.str.split(expand=True)
    df_split.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df_split["Hour"] = df_split["Hour"].str.split(":").str[0]
    df_split["Weekday"] = df_split["Weekday"].map(weekdays)
    df_split["Month"] = df_split["Month"].map(months)

    df_split = df_split.astype({"Weekday": object, "Day": int, "Year": int, "Hour": int})

    return df_split


def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all", axis=0).dropna(how="all", axis=1)
    df2 = split_date(df)
    df["Timestamp"] = pd.to_datetime(df2[["Year", "Month", "Day", "Hour"]])
    df = df.drop("Päivämäärä", axis=1).set_index("Timestamp")

    return df


def commute():
    # Assign DataFrame from 'bicycle_timeseries()'.
    df = bicycle_timeseries()

    # Slice the DataFrame to include data only for August 2017.
    df = df["2017-08-01":"2017-08-31"]

    # Add a 'Weekday' column based on the day of the week (Monday is 1).
    # By default, '.weekday' is indexed from Monday=0 to Sunday=6.
    df["Weekday"] = df.index.weekday + 1

    # Set the "Weekday" column as the new index.
    df = df.set_index("Weekday")

    # Group the DataFrame by weekday and calculate the sum of values.
    df = df.groupby("Weekday").sum()

    return df


def main():
    # Call the 'commute()' function and get the DataFrame.
    df = commute()

    # Plot the DataFrame.
    df.plot()

    # Define a list of weekdays and set it as the x-axis labels.
    weekdays = "x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)

    # Display the plot.
    plt.show()


if __name__ == "__main__":
    main()
