import numpy as np


"""
Exercise 5.6: Error on Simpson's Rule

Textboox: Computational Physics by Mark Newman
"""


def trapezoidal_rule(N, a, b):
    """
    Function integrates f(x) = x**4 - 2*x +1 from [a,b] utilizing
    the trapezoidal rule.

    Args:
        int N: Number of slices
        float a: Lower limit of integration
        float b: Upper limit of integration

    Returns:
        float: result of integration
    """

    def func(x):
        """
        Function calculates f(x) = x**4 - 2*x + 1
        """
        return x**4 - 2 * x + 1

    h = (b - a) / N  # Width of slices
    s = 0.5 * func(a) + 0.5 * func(b)  # Initial value

    for k in range(1, N):
        s += func(a + k * h)

    return h * s


def error_estimation(I1, I2):
    """
    Function calculates the error of integration. Where the integration
    is done such at N1 slices != N2 slices.

    Args:
        float I1: Value of integral with N1 slices
        float I2: Value of integral with N2 slices

    Returns:
        float: absolute error
    """
    return 0.333 * np.abs(I2 - I1)


def print_results():
    """
    Functions prints the results calculated from trapezoidal_rule
    and error_estimation
    """

    print(f"Value of integral from {a} to {b} when N = 20: {I2}")
    print(f"Error of integration from epsilon: {error}")
    print(
        f"Error of integration from taking the difference when N = 20 : {
            np.abs(4.4 - I2)}"
    )


if __name__ == "__main__":

    a = 0.0
    b = 2.0

    I1 = trapezoidal_rule(N=10, a=a, b=b)
    I2 = trapezoidal_rule(N=20, a=a, b=b)
    error = error_estimation(I1, I2)
    print_results()
