import numpy as np

"""
Exercise 2.10 Part c): The semi-empirical mass formula

Textbook: Computational Physics by Mark Newman
"""


def semi_empirical_mass_formula(Z, A, a_5):
    """
    Function calculates the approximate binding energy per nucleon of an
    atomic nucleus with atomic number Z and mass number A.


    args:
        int Z: Atomic number
        float A: Mass number

    returns binding energy per nuclean (B/A) in units of MeV
    """

    a_1 = 15.8  # [MeV]
    a_2 = 18.3  # [MeV]
    a_3 = 0.714  # [MeV]
    a_4 = 23.2  # [MeV]

    B = a_1*A - a_2*(A**(2/3)) - a_3*((Z**2)/(A**(1/3))) - \
        a_4*((A - 2*Z)**2)/A + a_5/np.sqrt(A)

    return B/A


def semi_empirical_mass(Z):
    """
    Function provides the logical steps towards defining the value a_5 within the semi_empirical_mass_formula.

    args:
        int Z: Atomic number


    returns max binding energy per nucleon (B/A) with the corresponding atomic mass (A)
    """
    values = []
    # Holds the range of possible values for atomic mass for isotopes of element Z
    A_range = np.arange(Z, 3*Z+1)

    # Iterates through all elements of A_range to select value of a_5
    for A in A_range:

        if (A % 2) != 0:
            a_5 = 0
        elif (A % 2) == 0 and (Z % 2) == 0:
            a_5 = 12.0
        elif (A % 2) == 0 and (Z % 2) != 0:
            a_5 = -12.0

        values.append(semi_empirical_mass_formula(Z, A, a_5=a_5))

    # Returns the maximum binding energy per nucleon and the corresponding
    # atomic mass, returning the most stable nuclear configuration for Z
    return float(max(values)), float(A_range[values.index(max(values))])


if __name__ == "__main__":

    def main():
        """
        Function takes in the necessary inputs for calculating the nuclear binding
        energy per nucleon (B/A) within the semi_empirical_mass_formula function.
        """
        print("Nuclear Binding Energy Calculator (semi-empirical mass approximation)")
        print("Input 'q' to quit\n")

        while True:
            Z_input = input("Input atomic number (Z): ")
            if Z_input == 'q':
                break

            try:
                Z = int(Z_input)
                if Z <= 0:
                    raise Exception("Z must be > 0")

                B = semi_empirical_mass(Z)
                print(f"\nAtomic number: {Z}")
                print(f"Largest binding energy per nucleon: {B[0]: .2f} MeV")
                print(f"Most stable nucleus at atomic mass: {B[1]} u\n")

            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    main()
