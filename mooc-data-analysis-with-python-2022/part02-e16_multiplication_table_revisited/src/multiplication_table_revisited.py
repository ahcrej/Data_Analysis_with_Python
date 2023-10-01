#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    row_indices = np.arange(0, n).reshape(-1, 1)
    col_indices = np.arange(0, n).reshape(1, -1)

    results = row_indices * col_indices

    return results

def main():

    print(multiplication_table(4))

if __name__ == "__main__":
    main()
