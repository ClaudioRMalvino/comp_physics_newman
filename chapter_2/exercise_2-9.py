import numpy as np
from numba import jit
import time

"""
Exercise 2.9: The Madelung constant

Textbook: Computational Physics by Mark Newman 
"""


@jit(nopython=True)
def madelung_constant(L):
    """
    Function calculates the Madelung constant for crystalline sodium chloride (NaCl).

    int L: Number of lattice sites around a sodium cation

    returns a float value for Madelung constant
    """
    M = 0.

    # Iterates through all lattice sites at position (i, j, k)
    for i in range(-L, L + 1):
        for j in range(-L, L + 1):
            for k in range(-L, L + 1):
                # Handles zero division
                if i == 0 and j == 0 and k == 0:
                    continue
                # Distance from origin to neighboring sites
                r = np.sqrt(i*i + j*j + k*k)
                # Handles sign altering due to positive Na atom and negative Cl atom
                sign = (-1)**(np.abs(i) + np.abs(j) + np.abs(k))
                M += sign / r
    return -M


if __name__ == "__main__":

    L = 1000

    # Warm-up run for JIT compilation
    madelung_constant(1)

    # Timing the run
    start_time = time.time()
    result = madelung_constant(L)
    end_time = time.time()

    execution_time = end_time - start_time

    print(f"Madelung constant for L = {L}: {result}")
    print(f"Execution time: {execution_time:.6f} seconds")
