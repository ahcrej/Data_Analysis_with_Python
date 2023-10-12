#!/usr/bin/env python3

import pandas as pd


def top_bands():
    df_top = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df_bands = pd.read_csv("src/bands.tsv", sep="\t")
    # Cast band column to uppercases to all for key matching when calling pd.merge
    df_bands["Band"] = df_bands["Band"].str.upper()
    df_merged = pd.merge(df_top, df_bands, left_on=["Artist"],
                         right_on=["Band"])
    # # Alternatively, instead of calling str.upper() on df_bands, we can use:
    # df_merged = pd.merge(df_top, df_bands, left_on=["Artist"],
    #                      right_on=df_bands["Band"].str.upper())

    return df_merged


def main():
    print(top_bands())


if __name__ == "__main__":
    main()
