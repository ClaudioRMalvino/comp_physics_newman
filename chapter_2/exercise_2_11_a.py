"""
Exercise 2.11: Binomial Coefficients Part A)

Textbook: Computational Physics by Mark Newman
"""


def factorial(x):
    """
    Function calculates the factorial of an integer x.

    args:
    int x

    returns: x!
    """
    f = 1.0
    for i in range(1, x + 1):
        f *= i
    return f


def binomial(n, k):
    """
    Function calculates the binomial coefficient for a given n and k.

    args:
    int n
    int k

    returns: int value of binomial coefficient for values n and k.
    """
    if k == 0:
        return 1
    else:
        binom_coef = factorial(n) / (factorial(k) * (factorial(n - k)))

    return int(binom_coef)


def main():
    """
    Function takes the user inputs for the parameters n,k for binomial function
    and then prints the calculated values.
    """

    print("Binomial Coefficient Calculator")
    print("Input 'q' to quit")

    while True:

        n_input = input("Input an integer for n: ")
        if n_input == "q":
            break

        k_input = input("Input an integer for k: ")
        if k_input == "q":
            break

        try:

            n = int(n_input)
            k = int(k_input)

            if k < 0 or n < 0:
                raise ValueError("k and n must be greater than or equal to 0")

            print(f"Binomial coefficient for ({n},{k}): {binomial(n, k)}")

        except ValueError as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":

    main()
