#!/usr/bin/env python3

import pandas as pd


def powers_of_series(s, k):
    df = pd.DataFrame(s, columns=[1])
    # df.insert(loc, column, value)
    [df.insert(i, i + 1, s**(i + 1)) for i in range(1, k)]

    return df


def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 3))


if __name__ == "__main__":
    main()
