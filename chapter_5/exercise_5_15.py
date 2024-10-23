"""
Exercise 5.15: Calculate f'(x) for f(x) = 1 + (1/2)tanh(2x)

Textbook: Computational Physics by Mark Newman
"""
import numpy as np
import matplotlib.pyplot as plt


def central_diff(x, h):
    """
    Function calculates the derivative of f(x) by way of the central
    difference, specifically the forward difference for equally spaced points.

    Args:
        float x: Point in the x-axis
        float h: The distance from the point x to be evaluated

    Returns:
        return description
    """

    def f(x):
        """
        Function defines f(x) = 1 + (1/2)tanh(2x)

        Args:
            float x: Point in the x-axis

        Returns:
            float: The calculation of f(x=x)
        """

        return 1.0 + (0.5) * np.tanh(2.0 * x)

    return (f(x + h) - f(x - h)) / (2 * h)


def f_prime(x):
    """
    Function provides the analytical formula for (d/dx)f(x) 

    (d/dx)f(x) = (d/dx)(1 + (1/2)tanh(2x)) = Sech(2x)^2

    Args:
        float x


    Returns: 
        float: The calculation of f'(x=x)

    """

    return 1/(np.cosh(2*x))**2


def plot_fprime(x1, x2, h):

    x = np.linspace(x1, x2, 100)

    plt.plot(x, central_diff(x, h), '.')
    plt.plot(x, f_prime(x))
    plt.title(r"Numerical vs Analytical f'(x)")
    plt.xlabel(r"x")
    plt.ylabel(r"f'(x)")
    plt.legend(["Numerical", "Analytical"])
    plt.show()


def check_values(x1, x2, h):
    """
    Checks that the values x1, x2, and h are acceptable and fall within 
    the boundaries. 

    """

    if x1 > x2:
        raise Exception("x1 must be > x2. Please try again.")

    if h <= 0:
        raise Exception("h must be a value > 0. Please try again.")


def main():
    """
    Asks the user to input values for the domain of x in order to plot
    the numerical and analytical solution to (d/dx)(1 + (1/2)tanh(2x)).

    """
    print(
        "Calculating and plotting (d/dx)(1 + (1/2)tanh(2x)) for x in [x1, x2]")
    print("Input q to quit.")

    while True:
        x1_input = input("\nInput a lower bound x1 for [x1, x2]: ")
        if x1_input == 'q':
            break
        x2_input = input("Input an upper bound x2 for [x1, x2]: ")
        if x2_input == 'q':
            break
        h_input = input("Input the distance from x to be evaluated, h: ")
        if h_input == 'q':
            break

        try:
            x1 = float(x1_input)
            x2 = float(x2_input)
            h = float(h_input)

            check_values(x1, x2, h)

            plot_fprime(x1, x2, h)

        except Exception as e:
            print(f"\nError: {e}. Please try again.")


if __name__ == "__main__":

    main()
