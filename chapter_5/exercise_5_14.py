"""
Exercise 5.14: Gravitational pull of a uniform sheet

Textbook: Computational Physics by Mark Newman
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab


def gravitational_force(N, z, L, m):
    """
    Function calculates the gravitational force felt by a point mass of 1 kg
    a distance z from the center of a square sheet of are LxL and of negligible thickness


    Args:
        list args

    Returns:
        return description
    """

    area = L*L
    sigma = m/area   # Mass per unit area
    G = 6.674E-11       # Newton's gravitational constant
    a = -L/2             # Lower limit of integration
    b = L/2            # Upper limit of integration

    def f(x, y, z):

        return (z / (np.sqrt((x**2) + (y**2) + (z**2)) ** 3))

    y, wj = gaussxwab(N, a, b)
    x, wi = gaussxwab(N, a, b)
    s = 0.0

    # If the limits of integration differed between x and y,
    # a nested for loop would be required
    for k in range(N):
        s += wj[k] * wi[k] * f(x=x[k], y=y[k], z=z)

    return G * sigma * s


def plot(z, Fz):

    plt.plot(z, Fz)
    plt.title(r"Gravitational Force $F_{z}(z)$")
    plt.xlabel(r"z, [m]")
    plt.ylabel(r"$F_{z}(z)$")
    plt.show()


def checks(L, m, z):

    if L <= 0:
        raise Exception("The sheet must have a length L > 0")

    if m <= 0:
        raise Exception("The sheet must have a mass m > 0")

    if z <= 0:
        raise Exception("z must be at a height z > 0")


def main():

    print("Gravitational force due to a plate")
    print("Calculates the gravitational force of an object a height z in meters above a plate of area LxL with a mass, m.")
    print("The mass of the object above the sheet has been set to 1 kg.")
    print("Input q to quit.")

    while True:
        l_input = input("\nInput the length in meters, L: ")
        if l_input == "q":
            break

        m_input = input("Input the mass of the sheet, m: ")
        if m_input == "q":
            break

        z_input = input("Input the height of the object, z: ")
        if z_input == "q":
            break

        try:

            L = float(l_input)
            m = float(m_input)
            z = float(z_input)

            checks(L, m, z)

            N = 100
            z_domain = np.linspace(0, z, N)
            plot(z=z_domain, Fz=gravitational_force(z=z_domain, N=N, L=L, m=m))

        except Exception as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":

    main()
