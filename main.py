"""
Mandelbrot set.

Usage:
    main.py [exponent]

Where `exponent` is an integer > 1. If omitted, exponent is set to 2.
"""
import sys

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from collections import defaultdict


# image center for expression exponents
centers = defaultdict(lambda: (0.0, 0.0))
centers[2] = (-0.75, 0.0)
centers[3] = (0.0, 0.0)
centers[4] = (-0.2, 0.0)


if __name__ == '__main__':
    # params
    try:
        exponent = int(sys.argv[1])
        assert exponent >= 2
    except:
        exponent = 2  # z^exponent + c
    print('exponent:', exponent)
    n_iterations = 150
    extent = 3  # area extent for i and q
    n_pixels = 1000  # number of pixels per dimension

    # coords
    center = centers[exponent]
    i_extent = (center[0] - extent / 2, center[0] + extent / 2)
    q_extent = (center[1] - extent / 2, center[1] + extent / 2)
    i_coords = np.linspace(*i_extent, num=n_pixels)
    q_coords = np.linspace(*q_extent, num=n_pixels)
    i, q = np.meshgrid(i_coords, q_coords)
    plane_coords = i + q * 1j

    # computation: z^exponent + c
    c = plane_coords
    z = 0.0
    color = 0
    with np.errstate(all='ignore'):
        for i in tqdm(list(range(n_iterations))):
            z = np.power(z, exponent) + c
            color = np.where(~np.isnan(z), i, color)

    # plot
    plt.imsave(f'mandelbrot_{exponent}.png', color, cmap='twilight_shifted')
