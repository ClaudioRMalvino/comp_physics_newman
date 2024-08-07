from math import sqrt

"""
Exercise 2.10 Part a) & b): The semi-empirical mass formula

Textbook: Computational Physics by Mark Newman
"""


def semi_empirical_mass_formula(Z, A, a_5):
    """
    Function calculates the approximate nuclear binding energy B of an
    atomic nucleus with atomic number Z and mass number A.


    args:
        int Z: Atomic number
        float A: Mass number

    returns binding energy B in units of MeV
    """

    a_1 = 15.8  # [MeV]
    a_2 = 18.3  # [MeV]
    a_3 = 0.714  # [MeV]
    a_4 = 23.2  # [MeV]

    B = a_1*A - a_2*(A**(2/3)) - a_3*((Z**2)/(A**(1/3))) - \
        a_4*((A - 2*Z)**2)/A + a_5/sqrt(A)

    return B


def semi_empirical_mass(Z, A):
    """
    Function provides the logical steps towards defining the value a_5 within the semi_empirical_mass_formula.

    args:
        int Z: Atomic number
        float A: Mass number

    returns binding energy B in units of MeV
    """

    if (A % 2) != 0:
        a_5 = 0
    elif (A % 2) == 0 and (Z % 2) == 0:
        a_5 = 12.0
    elif (A % 2) == 0 and (Z % 2) != 0:
        a_5 = -12.0

    return semi_empirical_mass_formula(Z, A, a_5)


def main():
    """
    Function takes in the necessary inputs for calculating the nuclear binding
    energy B within the semi_empirical_mass_formula function.
    """
    print("Nuclear Binding Energy Calculator (semi-empirical mass approximation)")
    print("Input 'q' to quit")

    while True:

        Z_input = input("Input atomic number (Z): ")
        if Z_input == 'q':
            break

        A_input = input("Input atomic mass (A): ")
        if A_input == 'q':
            break

        try:
            Z = int(Z_input)
            A = float(A_input)

            if A <= 0 or Z <= 0:
                raise Exception("A and Z must be > 0")

            B = semi_empirical_mass(Z, A)

            print(f"Atomic number: {Z}")
            print(f"Mass number: {A} u")
            print(f"Approx nuclear binding energy: {B: .2f} Mev")
            print(f"Binding energy per nucleon: {B/A: .2f} MeV")

        except ValueError as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":

    main()
