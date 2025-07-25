import numpy as np
import time
from numba import jit

"""
Exercise 5.2: Utilizing the Extended Simpson Rule

Textbook: Computational Physics by Mark Newman
"""


@jit(nopython=True)
def ext_simspon_rule(a, b, N):
    def f(x):
        """
        Function calculates x^4 - 2x + 1
        """
        return x**4 - 2 * x + 1

    h = (b - a) / N
    c = h / 3.0  # caluclated the constant to reduce computation
    I = c * (f(a) + f(b))
    odds = 0.0
    evens = 0.0

    for k in range(1, N, 2):
        odds += f(a + k * h)
    for k in range(2, N, 2):
        evens += f(a + k * h)
    I += c * (4 * odds + 2 * evens)

    return I


def per_error(E, T):
    """
    Function calculates the percent difference between two values
    """
    return ((np.abs(E - T)) / T) * 100


if __name__ == "__main__":

    a = 0.0
    b = 2.0
    N = [10, 100, 1000]

    print(f"Integrating x^4 -2x + 1 from [{a}, {b}]\n")
    for i in N:
        start_time = time.time()
        result = ext_simspon_rule(a, b, i)
        end_time = time.time()
        execution_time = end_time - start_time
        error = per_error(result, 4.4)

        print(f"For N = {i}")
        print(f"Result = {result}")
        print(f"Execution time = {execution_time: .8f} sec")
        print(f"Percent Error = {error: .8f} %\n")
        print("-------------------------------\n")
