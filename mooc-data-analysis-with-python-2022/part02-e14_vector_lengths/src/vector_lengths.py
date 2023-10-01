#!/usr/bin/env python3

import numpy as np
# import scipy.linalg


def vector_lengths(a):
    lengths = np.sqrt(np.sum(a**2, axis=1))

    return lengths


def main():
    a = np.arange(12).reshape(3, 4)
    print(a)
    lengths = vector_lengths(a)
    print(lengths)


if __name__ == "__main__":
    main()
