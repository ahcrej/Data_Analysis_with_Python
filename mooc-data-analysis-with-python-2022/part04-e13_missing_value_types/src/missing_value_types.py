#!/usr/bin/env python3

import pandas as pd
import numpy as np


def missing_value_types():
    data = {"State": ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"],
            "Year of independence": ["-", 1917, 1776, 1523, "-", 1992],
            "President": ["-", "Niinistö", "Trump", "-", "Steinmeier", "Putin"]}
    df = pd.DataFrame(data).set_index("State")
    df.replace("-", np.nan, inplace=True)

    # Use the set_index method with the "State" column as the argument and
    # set 'inplace=True' to modify the DataFrame in place.
    # df.set_index("State", inplace=True)

    # Fill missing values in column 'A' with a specific value (e.g., 0)
    # df["President"].fillna(0, inplace=True)

    return df


def main():
    print(missing_value_types())


if __name__ == "__main__":
    main()
