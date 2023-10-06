#!/usr/bin/env python3

import pandas as pd


def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    # Mask DataFrame to only include entries where the month is July (m == 7)
    mask = (df["m"] == 7)
    df = df[mask]

    return df["Air temperature (degC)"].mean()


def main():
    print(f"Average temperature in July: {average_temperature():.1f}")


if __name__ == "__main__":
    main()
