#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(df):
    total = df.shape[0]
    mask = df["Population change from the previous year, %"] > 0
    subset = df[mask].shape[0]

    return subset / total


def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df["Akaa":"Äänekoski"]
    proportion = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {proportion*100:.1f}%")


if __name__ == "__main__":
    main()
