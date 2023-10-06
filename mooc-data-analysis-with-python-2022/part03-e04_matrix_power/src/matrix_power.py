#!/usr/bin/env python3
import numpy as np
from functools import reduce


def matrix_power(a, n):
    rows = a.shape[0]

    if n == 0:
        return np.eye(rows, dtype=int)
    else:
        gen = (a for i in range(abs(n)))
        fun = lambda x,y : x@y
        multiplicated = reduce(fun, gen)
        if n > 0:
            return multiplicated
        else:
            return np.linalg.inv(multiplicated)


def main():
    a = np.array([[1, 3],
                  [2, 2]])
    print(np.linalg.matrix_power(a, 3))
    print(matrix_power(a, 3))
    print(matrix_power(a, 3))


if __name__ == "__main__":
    main()
