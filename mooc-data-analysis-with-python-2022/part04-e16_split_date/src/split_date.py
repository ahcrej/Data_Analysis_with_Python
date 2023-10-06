#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    weekdays = {"ma": "Mon", "ti": "Tue", "ke": "Wed",
                "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    months = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
                  "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
                  "syys": 9, "loka": 10, "marras": 11, "joulu": 12}
    
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df["Päivämäärä"]
    df = df.dropna(how='all')
    df = df.str.split(expand=True)
    df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    # df.rename(columns={0: "Weekday", 1: "Day", 2: "Month", 3: "Year", 4: "Hour"}, inplace=True)
    df["Hour"] = df["Hour"].str.split(":").str[0]
    # df["Hour"] = df["Hour"].str[0]
    # Alternatively, you can use 'df["Hour"] = df["Hour"].str.get(0)' to set each value in 'Hour' to the first value in the list '[00:00]'

    # Each value in the column 'Weekday' is used as a key to the 'weekdays' dict
    # When given this key, the corresponding value in 'weekdays' is used to replace the original value
    df["Weekday"] = df["Weekday"].map(weekdays)
    df["Month"] = df["Month"].map(months) # These values are already cast to ints due to the value dtype in the 'months' dict

    # Cast the remaining columns their desired dtypes
    df = df.astype({"Weekday": object, "Day": int, "Year": int, "Hour": int})
    # df["Hour"] = df["Hour"].astype(int)
    # df["Day"] = df["Day"].astype(int)
    # df["Year"] = df["Year"].astype(int)
    

    return df

def main():
    print(split_date())
       
if __name__ == "__main__":
    main()
