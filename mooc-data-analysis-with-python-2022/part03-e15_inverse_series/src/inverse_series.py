#!/usr/bin/env python3

import pandas as pd


def inverse_series(s):
    # values = []
    # indices = []

    # for index, value in s.items():
    #     values.append(index)
    #     indices.append(value)
    # new_ser = pd.Series(values, index=indices)

    # return new_ser

    return pd.Series(s.index, s.values)


def main():
    ser = pd.Series([1, 2, 3], index=list("abc"))
    print(inverse_series(ser))


if __name__ == "__main__":
    main()
