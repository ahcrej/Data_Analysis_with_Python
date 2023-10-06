#!/usr/bin/env python3
import pandas as pd


def create_series(L1, L2):
    s1 = pd.Series(L1, index=list("abc"))
    s2 = pd.Series(L2, index=list("abc"))

    return (s1, s2)


def modify_series(s1, s2):
    s1["d"] = s2.loc["b"]
    del s2["b"]
    return (s1, s2)


def main():
    original = create_series([1, 2, 3], [4, 5, 6])

    print(f"{original}\n")
    new = modify_series(original[0], original[1])

    print(f"{new}\n")
    add = new[0] + new[1]
    
    print(f"{add}\n")


if __name__ == "__main__":
    main()
