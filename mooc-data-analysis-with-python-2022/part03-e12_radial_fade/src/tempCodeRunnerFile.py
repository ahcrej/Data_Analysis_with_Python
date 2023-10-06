#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    rows, cols = a.shape[0] - 1, a.shape[1] - 1
    center_y, center_x = rows/2, cols/2

    return (center_y, center_x)   # note the order: (center_y, center_x)


def radial_distance(a):
    height, width = a.shape[0:2]
    point2 = center(a)
    dist_array = np.zeros((height,width))
    for index, value in np.ndenumerate(dist_array):
        dist_array[index] = np.linalg.norm(np.array(index)-np.array(point2))
        
    return dist_array


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.array([[]])


def radial_mask(a):
    return np.array([[]])


def radial_fade(a):
    return np.array([[]])


def main():
    np.random.seed(0)
    arr = np.random.randint(0, 10, (10, 11))
    print(arr)
    print(radial_distance(arr))
    print(radial_distance(arr).shape)
    print(center(arr))


if __name__ == "__main__":
    main()
