import numpy as np
import matplotlib.pyplot as plt
import time
"""
Exercise 4.4: Calculating Integrals 

Textbook: Computational Physics by Mark Newman
"""


def integral(N):
    """
    Function takes the integral of I = \int_{-1}^{1} \sqrt{1 -x^{2}}dx
    """

    h = 2/N
    I = 0
    for k in np.arange(N):
        x = -1 + h*k
        y = np.sqrt(1-x**2)
        I += h*y
    return I


def per_error(E, T):
    """
    Function calculates the percent difference between two values
    """
    return round(((np.abs(E - T)) / T) * 100, 2)


def plot_func():
    x = np.linspace(-1, 1, 1000)
    y = np.sqrt(1-x**2)
    fig, ax = plt.subplots()
    ax.plot(x, y, color='blue', alpha=1.00)
    ax.fill_between(x, y, color='blue', alpha=.1)
    ax.set_title(r"f(x) = $\sqrt{1 - x^{2}}$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(0, 1.5)
    plt.show()


if __name__ == "__main__":

    N = 1000
    start_time = time.time()
    result = integral(N)
    end_time = time.time()
    actual_value = 1.57079632679
    error = per_error(result, actual_value)

    print(f"Area under f(x): {result}")
    print(f"Percent error: {error}")
    print(f"Execution time: {end_time - start_time}")

    plot_func()
