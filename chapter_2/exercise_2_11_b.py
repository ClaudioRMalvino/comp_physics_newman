"""
Exercise 2.11: Binomial Coefficients Part B)

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
    for i in range(1, x+1):
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
        binom_coef = factorial(n)/(factorial(k)*(factorial(n-k)))

    return int(binom_coef)


def pascals_triangle(N):
    """
    Function utilizes the binomial(n, k) function to calculate and print 
    Pascal's triangle.
    """
    n = 1
    print([1])
    while n < N:
        triangle = []
        for k in range(0, n+1):
            triangle.append(binomial(n=n, k=k))
        n += 1
        print(triangle)


if __name__ == "__main__":

    def main():
        """
        Function asks for the number of lines from Pascal's triangle 
        the user desires.
        """
        print("Pascal's Triangle Generator")
        print("Input 'q' to quit")

        while True:

            N_input = input(
                "Input number of lines of Pascal's triangle to be generated: ")
            if N_input == 'q':
                break

            try:
                N = int(N_input)

                if N <= 0:
                    raise ValueError("The number of lines must be > 0.")

                pascals_triangle(N)

            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    main()
