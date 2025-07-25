"""
Exercise 2.13: Recursion

Textbook: Computational Physics by Mark Newman
"""

"""
Part A) Catalan Numbers utilizing recursion
"""


def catalan_recursion(nth):
    """
    Function takes an integer and calculates the nth Catalan number C_n
    utilizing recursion.

    arg:
    int n: A number to construct the range [0, n]

    returns: Catalan numbers within [0, n]
    """

    if nth == 0:
        return 1
    else:
        mu = (4 * nth - 2) / (nth + 1)
        return mu * catalan_recursion(nth=nth - 1)


"""
Part B) Greatest common divisor utilizing recurison
"""


def g(m, n):
    """
    Function calculates the greatest common divisor of two nonnegative
    integers m and n.

    args:
    int m: A positiive integer
    int n: A positive integer

    returns: Greatest common divisor of m and n
    """

    if n == 0:
        return m
    else:
        return g(m=n, n=(m % n))


if __name__ == "__main__":
    nth = 100
    m = 108
    n = 192

    # Calculates and prints the 100th Catalan number
    print(f"The {nth}th Catalan number: {catalan_recursion(nth=nth)}")

    # Calculates and prints the GCD of 108 and 192
    print(f"The GCD of {m} and {n}: {g(m=m, n=n)}")
