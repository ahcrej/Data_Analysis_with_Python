#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    # # Mask DataFrame to only include entries where the month is July (m == 7)
    # mask = (df["Air temperature (degC)"] < 0)
    # df = df[mask]

    # return df["d"].count()

    return sum(df["Air temperature (degC)"] < 0.0)

def main():
    print(f"Number of days below zero: {below_zero()}")
    
if __name__ == "__main__":
    main()
