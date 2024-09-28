"""
Exercise 5.7 Part a): Integrating utilizing the adaptive trapezoidal method
 
Textbook: Computational Physics by Mark Newman
"""

import numpy as np


def adaptive_trapezoidal_rule(a, b):
    """
    Function utilizes the adaptive trapezoidal rule to integrate
    the function f(x). Function prints the value the step number,
    the integral, and the approximate error.

    Args:
        float a: Lower limit of integration
        float b: Upper limit of integration
        int N_1: Number of initial slices
    """

    def f(x):
        """
        Function defines the function within the integrand

        Args:
            float x: the value in which the function will be evaluated

        Returns:
            float: the value of f(x) at x
        """

        return (np.sin(np.sqrt(100 * x))) ** 2

    N = 1  # Number of slices
    h = (b - a) / N  # Size of slices
    s = 0.5 * f(a) + 0.5 * f(b)  # Inital value
    epsilon = 1.0e-6  # The approximate error
    step = 1        # Number of steps

    # Loops calculates the integral utilizing trapezoidal method
    for k in range(1, N + 1):
        s += f(a + k * h)

    I1 = h * s  # Value of initial integration

    print(f"Step: {step}\nResult: {I1}")

    # Loop runs while the error is below the intended error target
    while True:

        N *= 2
        step += 1
        h = (b - a) / N
        second_term = 0

        # Loop calculates the odd terms of the adaptive trapezoidal method
        for k in range(1, N, 2):
            second_term += f(a + k * h)

        I = 0.5 * I1 + (h * second_term)  # Value of the ith integral
        error = np.abs(I - I1) / 3  # Error estimation

        print(f"Step: {step}\nN: {N}\nResult: {I}\nError: {error}")

        if error <= epsilon:
            return I
        I1 = I  # Sets the value of i-1 integration step


def main():
    """
    Function performs the main loop of the program. Prompts the user for inputs
    concerning the limits of integration.
    """

    print("Integral Calculation Utilizing the Adaptive Trapezoidal Rule")
    print("Input 'q' to quit.")

    while True:

        a_input = input("Input lower limit of integration (a): ")
        if a_input == "q":
            break

        b_input = input("Input upper limit of integration (b): ")
        if b_input == "q":
            break

        try:
            a = float(a_input)
            b = float(b_input)

            adaptive_trapezoidal_rule(a, b)

        except Exception as e:
            print(f"Error: {e}. Please try again")


if __name__ == "__main__":

    main()
