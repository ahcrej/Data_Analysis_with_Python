#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
# matplotlib.use('TkAgg')


def center(a):
    rows, cols = a.shape[0] - 1, a.shape[1] - 1
    center_y, center_x = rows/2, cols/2

    return (center_y, center_x)   # note the order: (center_y, center_x)


def radial_distance(a):
    height, width = a.shape[0], a.shape[1]
    point2 = center(a)
    dist_array = np.zeros((height, width))

    for index, value in np.ndenumerate(dist_array):
        dist_array[index] = np.linalg.norm(np.array(index)-np.array(point2))

    return dist_array


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return (np.interp(a, (a.min(), a.max()), (tmin, tmax)))


def radial_mask(a):
    return scale(1 - radial_distance(a))


def radial_fade(a):
    height, width = a.shape[0], a.shape[1]

    # Reshape 'radial_mask(a)' into a 3D array with dimensions 'height' x 'width' x 1
    mask = radial_mask(a).reshape(height, width, 1)
    # a.shape = (368, 640, 3)
    # radial_mask(a).shape = (368, 640)
    # mask.shape = (368, 640, 1)

    return (a * mask)

def test(a):
    height, width = a.shape[0], a.shape[1]

    # Reshape 'radial_mask(a)' into a 3D array with dimensions 'height' x 'width' x 1
    mask = radial_mask(a).reshape(height, width, 1)

    return mask


def main():
    image = plt.imread('src/painting.png')
    test_arr = test(image)
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()


if __name__ == "__main__":
    main()
