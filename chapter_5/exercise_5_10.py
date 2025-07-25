"""
Exercise 5.10: Period of an anharmonic oscillator

Textbook: Mark Newman
"""
import matplotlib.pyplot as plt
import numpy as np
from gaussxw import gaussxwab


def T(upper, mass, N):
    """
    This function calculates the period of the anharmonic oscillator utilziing
    Gaussian quadrature.

    Args:
        float upper: Upper limit of integration
        float mass: The mass of the object

    Returns:
        float T: The period of the an harmonic oscillation
    """

    def f(x, upper):
        """
        Function that wll be integrated to solve for the period T

        Args:
            float x: Position
            float m: Mass of object

        Returns:
            float: value at x
        """
        return (1/np.sqrt((upper**4) - (x**4)))
    x, w = gaussxwab(N, a=0, b=upper)
    s = 0.0
    coeff = np.sqrt(8 * mass)
    for k in range(N):
        s += w[k] + f(x[k], upper)

    return coeff * s


def Tplot(x, y):

    plt.plot(x, y)
    plt.title("Period vs Amplitude")
    plt.xlabel(r"Amplitude, $m$")
    plt.ylabel(r"$T(a), s$")

    plt.show()


def checks(upper, mass, N):

    if N < 0:
        raise ValueError("N must be > 0")
    if mass < 0:
        raise ValueError("Object must have a mass.")
    if upper < 0:
        raise ValueError("Upper bounds must be > 0")


def main():

    print("Period for Anharmonic Oscillator V(x) = X^4")
    print("Input 'q' to quit")

    while True:
        upper_input = input("Input a value for the amplitude: ")
        if upper_input == 'q':
            break

        mass_input = input("Input the mass of the object: ")
        if mass_input == 'q':
            break

        n_input = input("Input number of slices for integration: ")
        if n_input == 'q':
            break

        try:
            upper = float(upper_input)
            mass = float(mass_input)
            N = int(n_input)

            checks(upper, mass, N)

            VT = np.vectorize(T)
            amplitudes = np.arange(upper)
            periods = VT(mass=mass, N=N, upper=amplitudes)
            Tplot(x=amplitudes, y=periods)

        except Exception as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":

    main()
