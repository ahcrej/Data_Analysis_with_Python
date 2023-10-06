#!/usr/bin/env python3

import numpy as np


def first_half_second_half(a):
    cols = a.shape[1]
    
    # Use '//' (floor division) which results in an integer, discarding the fractional part
    mid_point = cols // 2
    mask = np.sum(a[:, :mid_point], axis=1) > np.sum(a[:, mid_point:], axis=1)
    results = a[mask]

    return results


def main():
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2]])
    print(a)
    print(first_half_second_half(a))


if __name__ == "__main__":
    main()
