import numpy as np
import time

"""
Exercise 2.10 Part d): The semi-empirical mass formula

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


def semi_empirical_mass():
    """
    Function provides the logical steps towards defining the value a_5 within the semi_empirical_mass_formula. Runs through the first 100 elements Z = [1,100] and 
    calculates the approximate value for the highest binding energy per nucleon and 
    the corresponding atomic mass for each element in Z. 

    args:
        int Z: Atomic number

    """
    Z = np.arange(1, 101)
    A_range = np.arange(1, 3*len(Z))

    # Iterates through all atomic numbers from [1, 100]
    for z in Z:
        values = []
    # Iterates through all elements of A_range to select value of a_5
        for A in A_range:

            if (A % 2) != 0:
                a_5 = 0
            elif (A % 2) == 0 and (z % 2) == 0:
                a_5 = 12.0
            elif (A % 2) == 0 and (z % 2) != 0:
                a_5 = -12.0

            values.append(semi_empirical_mass_formula(z, A, a_5=a_5))

    # Returns the maximum binding energy per nucleon and the corresponding
    # atomic mass, returning the most stable nuclear configuration for Z
        print(f"Atomic number: {z}")
        print(f"Highest binding energy per nucleon: {
              float(max(values)): .2f} MeV")
        print(f"Most stable isotope: {
              float(A_range[values.index(max(values))])} u")
        print("--------------------------------------------\n")


if __name__ == "__main__":

    start_time = time.time()
    semi_empirical_mass()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"execution time: {execution_time}")
