#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    # Set all the 'New' and 'Re' values' in 'LW' to NaN
    df.replace(["New", "Re"], np.nan, inplace=True)

    # Drop all the NaN rows in 'LW' as these were not on the chart last week
    df.dropna(axis=0, subset=["LW"], inplace=True)

    # Cast all values in the "LW" column to integers, to allow boolean comparisons
    df["LW"] = df["LW"].astype(int)

    # Create a mask for rows where its 'Peak Pos' was due to its current 'Pos'
    mask = (df["Pos"] == df["Peak Pos"]) & (df["LW"] != df["Peak Pos"])
    df.loc[mask, 'Peak Pos'] = np.nan # Set these values to 'NaN'

    # Create a df for last week, sorted by the 'LW' column from the current week's df
    last_df = df.sort_values(by="LW", axis=0)
    last_df["Pos"] = last_df["LW"] # Transfer values from 'LW' to 'Pos' (as last week is now this week)
    last_df["LW"] = np.nan # Now cast all values in 'LW' to 'NaN'
    last_df["WoC"] -= 1 # Reduce 'Weeks on Chart' by 1 as this is calculating the df for the previous week

    # Iterate through 'Pos' to check for missing rows 
    # (We do not have data for this, so we will insert a NaN row)
    for i in range(1, 41):
        # Check if 'i' is not in the 'Pos' column
        if i not in last_df['Pos'].values:
            new_row = pd.DataFrame({"Pos": [i], "LW": [np.nan], "Title": [np.nan],
                                    "Artist": [np.nan], "Publisher": [np.nan],
                                    "Peak Pos": [np.nan], "WoC": [np.nan]})
            last_df = pd.concat([last_df, new_row], ignore_index=True)

    # Re-sort by 'Pos' as the appended rows are now at the bottom
    last_df.sort_values(by="Pos", axis=0, inplace=True) 

    # Re-set the index as the df is now in the correct order
    last_df.reset_index(drop=True, inplace=True) 

    return last_df


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
