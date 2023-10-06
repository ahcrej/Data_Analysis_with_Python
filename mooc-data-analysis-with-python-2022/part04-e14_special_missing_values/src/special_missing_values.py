#!/usr/bin/env python3

import pandas as pd
import numpy as np


def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df.replace(["New", "Re"], np.nan, inplace=True)
    
    # Cast all values in the "LW" column to a numeric, to allow the 'mask' line to operate
    # df["LW"] = pd.to_numeric(df["LW"])
    df["LW"] = pd.to_numeric(df["LW"], errors="coerce").fillna(-999).astype(int) # Replace NaN values with -999
    mask = (df["Pos"] > df["LW"]) & (df["LW"] != -999) # Filter out values that were previously NaN too

    return df[mask]


def main():
    print(special_missing_values())


if __name__ == "__main__":
    main()
