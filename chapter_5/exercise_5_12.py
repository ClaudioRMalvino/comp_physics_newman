"""
Exercise 5.12: The Stefan-Boltzmann constant

Textbook: Computational Physics by Mark Newman
"""

import numpy as np
from scipy import constants
from gaussxw import gaussxwab

# Constants
kb = constants.Boltzmann
h = constants.hbar
c = constants.speed_of_light
sb = constants.Stefan_Boltzmann


def W(T, N):
    """
    Function calculates the rate of black body radiation per unit area.
    As the function limit of integration is [0, +inf], 
    change of variables will be utilized with Gaussian quadrature,
    to evaluate the integral. 

    Change of variables:

            x = z * (1-z)^-1,      dx = (1-z)^-2

    Args:
        int N: Number of slices

    Returns:
        float result: The evaluated integral
    """

    def f(z):
        """
        Function describes the integrand after implementing change of variables.

        Original function:

            (x^3) * ((e^x) - 1)^-1

        """
        numerator = (z**3) / ((1 - z)**3)
        denominator = np.exp(z / (1 - z)) - 1
        dz = 1 / ((1 - z)**2)

        return (numerator/denominator) * dz

    constant = ((kb**4) * (T**4)) / ((4*np.pi**2) * (c**2) * (h**3))

    a = 0.0
    b = 1.0
    z, w = gaussxwab(N, a, b)
    s = 0.0
    for k in range(N):
        s += w[k] * f(z[k])

    return constant * s


def per_error(x1, x2):
    """
    Calculates the percent error between two values.

    Args:
        float x1: Theoretical/known value
        float x2: Experimental/calculates value

    Returns:
        float: Percent error between x1 and x2
    """

    return abs((x1-x2)/x1) * 100.0


if __name__ == "__main__":

    N = 50
    T = 1.0
    result = W(T, N)

    print("\nValues for Stefan-Boltzmann constant")
    print("--------------------------------------")
    print(f"Calculated: {result}")
    print(f"Theoretical: {sb}")
    print(f"Percent error: {per_error(x1=result, x2=sb): .3f} %")
