import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import time

"""
Exercise 5.4 Part a): The diffraction limit of a telescope

Textbook: Computational Physics by Mark Newman
"""


@jit(nopython=True)
def J(m, x):
    """
    Function represents the Bessel function, evaluated for m and x
    utilizing the extended simpson rule for integration.
    """

    def f(m, x, theta):
        """
        Function calculates (1/pi)*cos(m*theta -x*sin(theta))
        """
        return np.cos(m * theta - x * np.sin(theta))

    def ext_simspon_rule(m, x):
        """
        Function performs the extended Simpson rule for approximating integrals
        """
        N = 100000  # Number of slices
        a = 0.0  # Starting point
        b = np.pi  # End point
        h = (b - a) / N  # Width of slices
        c = h / 3.0  # caluclated the constant to reduce computation
        # holds the first term in the Ext Simpson Rule
        I = c * (f(m, x, a) + f(m, x, b))
        odds = 0.0
        evens = 0.0
        # Loops through for the odd and even summations of the Ext Simpson Rule
        for k in range(1, N, 2):
            odds += f(m, x, k * h)
        for k in range(2, N, 2):
            evens += f(m, x, k * h)

        I += c * (4 * odds + 2 * evens)

        return (1 / np.pi) * I

    J = ext_simspon_rule(m, x)
    return J


def plot_bessel_func(xs, values):
    """
    Function plots the values for Bessel functions J_0(x), J_1(x), and J_2(x)
    """
    plt.title("Bessel Functions $J_{0}(x), J_{1}(x), J_{2}(x)$")
    plt.plot(xs, values[0, :], color="b", label="$J_{0}(x)$")
    plt.plot(xs, values[1, :], color="g", label="$J_{1}(x)$")
    plt.plot(xs, values[2, :], color="r", label="$J_{2}(x)$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


if __name__ == "__main__":

    # Holds the  values  for J_m(x)
    xs = range(21)
    ms = range(3)

    # Warm up for jit compiler
    warmup = J(0, 1)

    # The matrix which holds the values for J_m(x)
    values = np.zeros((3, 21))

    # Loops through values of m and x to calculate J_m(x)
    t0 = time.time()
    for m in ms:
        for x in xs:
            values[m, x] = J(m, x)
    tf = time.time()
    print(f"run time for loop: {tf - t0}")

    plot_bessel_func(xs, values)
