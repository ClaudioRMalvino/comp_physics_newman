"""
Exercise 5.13: Quantum uncertainity in the harmonic oscillator 

Textbook: Computational Physics by Mark Newman
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
from math import factorial


def H(n, x):
    """
    Function calculates the Hermite polynomial for a given x and any int n >= 0.

            H_{n +1}(x) = 2*x*H_{n}(x) - 2*n*H_{n-1}(x)
    Args:
        float x: Position along the x-axis
        int n: Selects the nth Hermite polynomial

    Returns:
        float: The nth Hermite polynomial

    """

    H0 = 1.0
    H1 = 2.0 * x
    hermite = [H0, H1]

    for n in range(1, n):

        HN = (2 * x * hermite[n]) - (2 * n * hermite[n-1])
        hermite.append(HN)

    return hermite[-1]


def psi(n, x):
    """
    Function describes the wave function of a one-dimensional quantum oscillator when all constants are set equal to 1. 

    Args:
        float x: Position along the x-axis

    Returns:
        float: Value of the wave function at x
    """

    coeff = 1/(np.sqrt((2**n) * factorial(n) * np.sqrt(np.pi)))

    x_terms = np.exp(-(x**2)/2) * H(n, x)

    return coeff * x_terms


def x_uncertainty(N, n):
    """
    Function calculates the uncertainty in the position of the wave function via
    the root-mean-square position.
    Utilizes Gaussian quadrature and change of variables to calculate the 
    integral for the expectation value of the position squared: < x^2 >.

    Args:
        int N: Integer for the number of sample points
        int n: Denotes the nth level of the quantum harmonic oscillator

    Returns:
        float: returns the root-mean-square position: (< x^2 >)^(1/2)
    """

    def H(n, z):
        """
        Function calculates the Hermite polynomial for a given z and any int n >= 0.

                H_{n +1}(z) = 2 * tan(z) * H_{n}(x) - 2*n*H_{n-1}(z)
        Args:
            float z: Position along the x-axis after change of variables
            int n: Selects the nth Hermite polynomial

        Returns:
            float: The nth Hermite polynomial

        """
        x = np.tan(z)
        H0 = 1.0
        H1 = 2.0 * x
        hermite = [H0, H1]

        for n in range(1, n):

            HN = (2 * x * hermite[n]) - (2 * n * hermite[n-1])
            hermite.append(HN)

        return hermite[-1]

    def psi(n, z):
        """
        Function describes the wave function of a one-dimensional quantum oscillator when all constants are set equal to 1. 
        A change of variables is performed for the purpose of integration.

            x = tan(z), dx = dx/cos()^2
        Args:
            float z: Sample points from gaussxwab


        Returns:
            float: Value of the wave function at z
        """

        coeff = 1/(np.sqrt((2**n) * factorial(n) * np.sqrt(np.pi)))
        x = np.tan(z)

        x_terms = np.exp(-(x**2)/2) * H(n, z)

        return coeff * x_terms

    def integrand(n, z):
        """
        Args: 
            int n: Denotes the nth level of the quantum harmonic oscillator       
            float z: Sample points from gaussxwab

        Returns:
            float: the integral at points z
        """

        x = np.tan(z)
        dx = 1 / (np.cos(z)**2)

        return (x**2) * (np.abs(psi(n, z))**2) * dx

    a = -np.pi/2    # Lower limit of integration
    b = np.pi/2     # Upper limit of integration
    z, w = gaussxwab(N, a, b)   # Sample points and weights
    s = 0

    for k in range(N):
        s += w[k] * integrand(n, z[k])

    return np.sqrt(s)


if __name__ == "__main__":

    # Part a)

    n_max = 3                       # Max number of levels
    x = np.linspace(-4, 4, 50)      # The domain along x
    results = []

    for n in range(n_max + 1):
        results.append([psi(n=n, x=x)])

    # Loops through the values of n and plots the graph of each wavefunction
    for n in range(n+1):
        plt.plot(x, results[n][0])

    plt.title(r"$\psi_{n}(x)$")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\psi_{n}(x)$")
    plt.legend(labels=[
               "n = 0", "n = 1", "n = 2", "n = 3"])
    plt.show()

    # Part b)

    n = 30                          # Quantum number
    x = np.linspace(-10, 10, 100)   # The domain along x
    results = [psi(n=n, x=x) for x in x]

    # Plots the graph of Psi(x) for n = 30
    plt.plot(x, results)
    plt.title(r"$\psi_{30}(x)$")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\psi_{30}(x)$")
    plt.show()

    # Part c)

    N = 100     # Number of sample points
    n = 5       # Quantum number

    print(x_uncertainty(N, n))
