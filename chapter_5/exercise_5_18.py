"""
Exercise 5.18

Textbook: Computational Physics by Mark Newman
"""


def f(x):
    """
    Function defines f(x) = x^3 - 2x  + 1

    Args:
        float x: Point on the x-axis

    Returns:
        float: calculation of  f(x=x)
    """

    return (x**4) - 2*x + 1


def f_prime(x):
    """
    Function calculates the derivative of f(x) by way of the central 
    difference, specifically the forward difference. 

    Args:
        float x: Point on the x-axis
        float h: the distance from the point x to be evaluated

    Returns:
        float value for f'(x) at x
    """

    h = 0.00005     # Evaluation point from x
    H = h/2
    return (f(x + H) - f(x-H)) / (h)


def fourth_order(a, b, N):
    """
    Function calculates the integral of f(x) upto O(h^4) approximation.

    Args:
        float a: Lower limit of integration
        float b: Upper limit of integration 
        float h: Width of slices
        int N: Number of slices

    Returns:
        float: The integral of f(x) evaluated between [a,b]
    """

    h = (b - a)/N
    s = 0.5 * f(a) + 0.5 * f(b)
    second_term = (1/12)*(h**2)*(f_prime(a) - f_prime(b))

    for k in range(1, N):
        s += f(a + k*h)
    return h*s + second_term


def trapezoidal_rule(a, b, N):
    """
    Function integrates f(x) utilizing the Trapezoidal rule. 

    Args:
        float a: Lower limit of integration
        float b: Upper limit of integration 
        float h: Width of slices
        int N: Number of slices

    Returns:
        float: The integral of f(x) evaluated between [a,b]
    """

    h = (b - a)/N
    s = 0.5 * f(a) + 0.5 * f(b)

    for k in range(1, N):
        s += f(a + k*h)
    return h*s


if __name__ == "__main__":

    a = 0.0     # Lower limit of integration
    b = 2.0     # Upper limit of integration
    N = 10      # Number of slices

    print(f"Fourth order approximation: {fourth_order(a, b, N)}")
    print(f"Trapezoidal Rule (Second order approximation): {
        trapezoidal_rule(a, b, N)
    }")
    print(f"Exact value: 4.4")
