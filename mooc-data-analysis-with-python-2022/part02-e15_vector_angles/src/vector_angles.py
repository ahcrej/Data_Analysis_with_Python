#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X, Y):
    # Calculate the dot products of rows in X and Y
    dot_prod = np.sum(X*Y, axis=1)

    # Calculate the magnitude of rows in X
    mag_x = scipy.linalg.norm(X, axis=1)

    # Calculate the magnitude of rows in Y
    mag_y = scipy.linalg.norm(Y, axis=1)

    # Calculate the cos(theta)
    cos_angles = dot_prod/(mag_x * mag_y)

    # Clip the cos(theta) values to be within [-1, 1]
    cos_angles = np.clip(cos_angles, -1.0, 1.0)

    # Calculate theta in radians
    angles_rad = np.arccos(cos_angles)

    # Calculate theta in degrees
    angles_deg = np.degrees(angles_rad)

    return angles_deg


def main():
    a = np.arange(6).reshape(2, 3)
    b = np.arange(6, 12).reshape(2, 3)
    print(a)
    print(b)
    print(vector_angles(a, b))


if __name__ == "__main__":
    main()
