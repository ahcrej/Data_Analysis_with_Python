#!/usr/bin/env python3

import numpy as np


def column_comparison(a):
    # Compares the entire second column '[9, 5, 7, 8, 1]' with the second last column '[8, 9, 0, 6, 5]'.
    # Returns a boolean array 'mask' where each element is true if the corresponding element in the
    # second column is greater than the corresponding element in the second last column.
    mask = a[:, 1] > a[:, -2]

    # 'a[b]' selects the rows of 'a' where 'mask' is 'True'
    # 'a[~b]' selects the rows of 'a' where 'mask' is 'False'
    # The '~' operator negates the condition of 'mask', selecting the elements that do not satisfy the condition.
    results = a[mask]

    return results


def main():
    arr = np.array([[8, 9, 3, 8, 8],
                    [0, 5, 3, 9, 9],
                    [5, 7, 6, 0, 4],
                    [7, 8, 1, 6, 2],
                    [2, 1, 3, 5, 8]])
    print(arr)
    print(column_comparison(arr))


if __name__ == "__main__":
    main()
