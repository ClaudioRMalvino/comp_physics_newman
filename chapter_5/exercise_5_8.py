"""
Exercise 5.8 Part b): Integration by adaptive Simspon's rule

Textbook: Computational Physics by Mark Newman
"""
import numpy as np


def adaptive_simpson_rule(a, b):
    """
    Function utilzies the adaptive Simpson's rule to integrate the function
    f(x). Function prints the value of the integration, the step number, and
    the approximate error.

    Args:
        float a: Lower limit of integration
        float b: Uppper limit of integration

    """
    def f(x):

        return (np.sin(np.sqrt(100*x))) ** 2

    def S(a, b, N, h):
        def evenSum(N, h):
            s = 0
            if N <= 2:
                return 2.0 * f(a + 2 * h)
            for k in range(2, N-2, 2):
                s += f(a + k * h)
            return 2.0 * s
        return (1/3) * (f(a) + f(b) + evenSum(N, h))

    def T(a, N, h):

        def oddSum(N, h):
            s = 0
            if N <= 1:
                return (2/3)*f(a + h)
            for k in range(1, N, 2):
                s += f(a + k * h)
            return s
        return (2/3) * oddSum(N, h)

    N = 2   # Number of slices
    h = (b - a) / N  # Width of slices
    epsilon = 1.0e-6    # The approximate error
    step = 1    # Initialize the number of steps
    S1 = S(a, b, N, h)
    T1 = T(a, N, h)
    I1 = h * (S(a, b, N, h) + 2 * T(a, N, h))   # The initial integral

    # Loop performs while error >= to the required level of accuracy
    while True:

        N *= 2
        step += 1
        h = (b - a) / N
        sNew = S1 + T1
        tNew = T(a, N, h)
        I = h*(sNew + 2 * tNew)

        error = (1/15)*np.abs((I - I1))
        print(f" Step: {step}\nN: {N}\nResult: {I}\nError: {error}")

        if error <= epsilon:
            return I

        S1 = sNew
        T1 = tNew
        I1 = I


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

            adaptive_simpson_rule(a, b)

        except Exception as e:
            print(f"Error: {e}. Please try again")


if __name__ == "__main__":

    main()
