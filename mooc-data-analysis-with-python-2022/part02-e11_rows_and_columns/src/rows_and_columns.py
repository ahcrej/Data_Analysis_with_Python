#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    return [row for row in a]

def get_columns(a):
    # Flip rows to columns (and columns to rows) using the T method.
    # Append row for row in a.T (new rows were previously columns).
    return [row for row in a.T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
