import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit

"""
Exercise 5.3: Integrating \int_{0}^{x} e^{-t^{2}} dt

Textbook: Computational Physics by Mark Newman
"""

@jit(nopython=True)
def ext_simspon_rule(x, h, N):
    def f(t):
        """
        Function evaluates e^{-t^{2}}
        """
        return np.exp(-t**2)

    c = h/3.0
    I = c * (f(x) + f(0))
    odds = 0.
    evens = 0.

    for k in range(1, N, 2):
        odds += f(k * h)
    for k in range(2, N, 2):
        evens += f(k * h)
    I += c * (4*odds + 2*evens)

    return I

def plot_func(x):
    """
    Function plots the graph of e^(-t^(2))
    """
    xs = np.linspace(0,x,1000)
    ys = np.array([np.exp(-x**2) for x in xs])

    plt.plot(xs, ys, color='b')
    plt.title("f(t) = $e^{-t^{2}}$")
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.show()


def main():
    """
    Function prompts user for inputs to calculate the integral of
    e^(-t^(2)) from [0, t] at intervals h
    """

    print("Integration Calculator")
    print("Input 'q' to quit")

    while True:
        x_input = input("Input a value for the upper limit of integration [0, t]: ")
        if x_input == 'q':
            break
        h_input = input("Input the size of steps, h: ")
        if h_input == 'q':
            break
        n_input = input("Input the number of slices, N: ")
        if n_input == 'q':
            break

        try:
            x = float(x_input)
            h = float(h_input)
            N = int(n_input)

            if h < 0:
                raise ValueError("h must be > 0")
            if N <= 1:
                raise ValueError("N must be > 1")
            if not isinstance(N, int):
                raise ValueError("N must be an integer")

            print(f"\nIntegrating e^(-t^(2)) from [0, {x}]\n")
            warmup = ext_simspon_rule(1,0.1,10)

            start_time = time.time()
            result = ext_simspon_rule(x, h, N)
            end_time = time.time()
            execution_time = end_time - start_time

            print(f"For N = {N}")
            print(f"Result = {result}")
            print(f"Execution time = {execution_time: .8f} sec")
            print("-------------------------------\n")

            plot_func(x)

        except Exception as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":

    main()
