"""
Exercise 5.11: Diffraction of a Sound Wave

Textbook: Mark Newman
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab


def u(x, z, l):
    """
    Function calculates the upper bound of our integration

    Args:
        float x: Position on the x-axis
        float z: Position on the z-axis
        float l: Wavelength, lambda

    Returns:
        float value
    """
    return x * np.sqrt(2 / (l * z))


def C(t, w, N):
    """
    Function calculates the value f(x) for the cosine of the soundwave propgation
    utilizing Gaussian quadrature.

    Args:
        array t: Values calculated utilziing gaussxwab
        array w: Weighted values utilziing gaussxwab
        int N: The number of slices

    Returns:
        float s: Approximate value after integration
    """

    def f(t):
        return np.cos(0.5 * np.pi * (t**2))

    s = 0.0
    for k in range(N):
        s += w[k] + f(t[k])

    return s


def S(t, w, N):
    """
    Function calculates the value f(x) for the sine of the soundwave propgation
    utilizing Gaussian quadrature.

    Args:
        array t: Values calculated utilziing gaussxwab
        array w: Weighted values utilziing gaussxwab
        int N: The number of slices

    Returns:
        float s: Approximate value after integration
    """

    def f(t):
        return np.sin(0.5 * np.pi * (t**2))

    s = 0.0
    for k in range(N):
        s += w[k] + f(t[k])

    return s


def ratio(C, S):
    """
    Function calculates the ratio I/I_0.

    Args:
        float C: Solution to the function C(t,w,N)
        float S: Solution to the function S(t,w,N)

    Returns:
        float: Th value of calculation
    """

    first_term = ((2 * C) + 1) ** 2
    second_term = ((2 * S) + 1) ** 2
    return (1 / 8) * (first_term + second_term)


def ratioVsXPlot(x, y):
    """
    Plots the the graph of the ratio I/I_0 vs x.
    """
    plt.plot(x, y)
    plt.title(r"$\frac{I}{I_{0}}$ vs $x$")
    plt.xlabel(r"$x, [m]$")
    plt.ylabel(r"$\frac{I}{I_{0}}$")
    plt.show()


if __name__ == "__main__":

    N = 100  # Number of slices
    l = 1.0  # wavelength, lambda, [m]
    z = 3.0  # height of building, [m]
    x = np.linspace(-5, 5, N)  # width of building, [m]
    a = 0.0  # lower limit of integration
    y = []  # hold the results of integration, ratio()

    # Loops through each element in x in order to calculate I/I_0
    #  at every point along x
    for i in x:
        b = u(x=i, z=z, l=l)  # upper limit of integration
        t, w = gaussxwab(a=a, b=b, N=N)  # weights for Gaussian quadrature
        y.append(ratio(C=C(t, w, N), S=S(t, w, N)))

    ratioVsXPlot(x=x, y=y)
