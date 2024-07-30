from math import sqrt

"""
Exercise 2.5: Quantum Potential Step

Textbook: Computational Physics by Mark Newman
"""

# Global constants
m = 0.5109989461  # Mass of electron in eV
h_bar = 6.5821196  # Reduced Planck constant in eV*s


def k1(E):
    """
    Function which calculates initial wave vector k1.

    float E: Initial energy of the electron

    returns float
    """
    return sqrt(2 * m * E / h_bar)


def k2(E, V):
    """
    Function which calculates reflected wave vector k2.

    float E: Initial energy of the electron
    float V: Potential step

    returns float
    """
    return sqrt(2 * m * (E - V) / h_bar)


def T(k1, k2):
    """
    Function calculates the probability of transmission over the potential step given k1 and k2.

    float k1: initial wavevector form function k1(E, V)
    float k2: wavevector which passes across the potential step k2(E, V)

    return float: probability as a percentage of transmission
    """

    return (4 * k1 * k2) / (k1 + k2) ** 2


def R(k1, k2):
    """
    Function calculates the probability of reflecting back towards intial source
    given k1 and k2.

    float k1: initial wavevector form function k1(E, V)
    float k2: wavevector which passes across the potential step k2(E, V)

    return float: probability as a percentage of reflection
    """
    return ((k1 - k2) / (k1 + k2)) ** 2


def main():

    print("Calculating transmission and reflection probabilities.")
    print("Input 'q' to quit")

    while True:

        E_input = input("Input energy of electron in eV: ")
        if E_input == "q":
            break

        V_input = input("Input energy of potential step in eV: ")
        if V_input == "q":
            break

        E = float(E_input)
        V = float(V_input)

        if E <= V:
            k = -k1(E)
            print(f"wavevector: {k}, Probability of Reflection: 100%")
        else:
            print(
                f"\nGiven an electron of mass {m} eV, initial energy {
                    E} eV and potential step {V} eV:\n"
            )
            print(
                f"Probability of reflection:{
                    round(R(k1=k1(E), k2=k2(E, V))*100, 1)}% || wavevector : {round(-k1(E), 3)}"
            )
            print(
                f"Probability of transmission:{
                    round(T(k1=k1(E), k2=k2(E, V))*100, 1)}% || wavevector: {round(k2(E, V), 3)}"
            )


if __name__ == "__main__":

    main()
