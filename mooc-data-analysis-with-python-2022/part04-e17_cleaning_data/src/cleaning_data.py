#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    # Maximum presidential terms is 3 (Roosevelt)
    terms = {"one": 1, "two": 2, "three": 3}

    # Read the .tsv to a df
    df = pd.read_csv("src/presidents.tsv", sep="\t")

    # Replace "-" with NaN
    df.replace("-", np.nan, inplace=True)

    # Use dictionary.get(key, return_value) to check if x is a key, if not return x
    df["Seasons"] = df["Seasons"].map(lambda x: terms.get(x, x))
    df["Start"] = df["Start"].str.split().str[0]

    # Split the 'President' and 'Vice-resident' strings by ',' and join in the reversed list order
    df["President"] = df["President"].str.split(",").apply(
        lambda x: " ".join([name.strip().title() for name in reversed(x)]))
    df["Vice-president"] = df["Vice-president"].str.split(",").apply(
        lambda x: " ".join([name.strip().title() for name in reversed(x)]))

    df = df.astype({"President": object, "Start": int,
                    "Last": float, "Seasons": int, "Vice-president": object})

    return df


def main():
    print(cleaning_data())


if __name__ == "__main__":
    main()
