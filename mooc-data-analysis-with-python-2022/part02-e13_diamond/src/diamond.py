#!/usr/bin/env python3

import numpy as np


def diamond(n):
    # Create an identity matrix of size 'n'
    # This identity matrix will have ones on the main diagonal and zeros elsewhere
    a = np.eye(n, dtype=int)
    # Mirror the original identity matrix
    b = np.flip(a, 0)
    # Create the top half of the diamond by merging a and b
    diamond = np.concatenate((a, b), axis=1)
    # Join the top half of the diamond with a flipped version
    diamond = np.concatenate((np.flip(diamond, 0), diamond))
    # Delete the additional column
    diamond = np.delete(diamond, n, 1)
    # Delete the additional row
    diamond = np.delete(diamond, n, 0)

    return diamond


def main():
    print(diamond(4))
    print(diamond(1))


if __name__ == "__main__":
    main()
