"""
Exercise 5.17: The Gamma Function

Textbook: Computational Physics by Mark Newman
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab


def integrand(a, x):
    """
    Function defines the integrand of the gamma function.

        x^(a -1)exp[-x]

    Args:
        float a
        float x

    Returns:
        the value of x^(a -1)exp[-x] at a and x
    """

    return (x**(a-1)) * (np.exp(-x))


def gamma(a):
    """
    Calculates the gamma function utilizing a change of variables
    and the Gaussian Quadrature method of numerical integration.

    Change of variable:

            x = (z*c) / (1 - z),    dx = c / (1 - z)^2 dz

    We further corrected the form of the integrand in order to mitigate
    numerical underflow and overlow.

    Substituion:

        x^(a-1) = e^((a-1)lnx)

    Args:
        float a: A positive real number

    Returns:
        float value of the gamma function evaluated at a
    """

    def f(a, z):
        c = a-1
        x = (z*c) / (1-z)
        dz = c / ((1 - z)**2)
        arg = (((a - 1) * np.log(x)) - x)
        return np.exp(arg) * dz

    N = 20
    lower = 0.0
    upper = 1.0
    x, w = gaussxwab(N=N, a=lower, b=upper)
    s = 0.0
    for k in range(N):
        s += w[k] * f(a, x[k])

    return s


def plot_integrand(a, x1, x2):
    """
    Plots the integrand function for selections of 'a' in the domain x:[x1, x2]

    Args:
        float (optional array): a
        float x1: Lower bound along the x-axis
        float x2: Upper bound along the x-axis
    """
    x = np.linspace(x1, x2, 100)

    for i in a:
        plt.plot(x, integrand(a=i, x=x))
    plt.title(r"$f(x) = x^{a-1}e^{-x}$")
    plt.xlabel(r"x")
    plt.ylabel(r"f(x)")
    plt.legend([f"a={a}" for a in a])
    plt.show()


if __name__ == "__main__":

    # Part a)
    a = [2, 3, 4]
    plot_integrand(a, 0, 5)

    # Part c)
    a = 3/2
    print(gamma(a))

    # Part b)
    values = [(3, 2), (6, 120), (10, 362880)]

    for val in values:
        print(f"Numerical Gamma({val[0]}) = {gamma(val[0])}")
        print(f"Analytical Gamma({val[0]}) = {val[1]}")
