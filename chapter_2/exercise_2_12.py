import numpy as np

"""
Exercise 2.12: Prime numbers

Textbook: Computational Physics by Mark Newman
"""


def prime_nums(n):
    """
    Function finds prime numbers up to n.

    args:
    int n: the range from [2, n] for finding prime numbers

    returns a list of all prime numbers within the range [2, n]
    """

    primes = [2]

    if n < 2:
        return []

    for i in range(3, n + 1, 2):
        # Sets the default value of i as True and then
        # the for loop will check to see if this is indeed the case
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        # If i is still prime, it is added to primes
        if is_prime:
            primes.append(i)
    print(primes)


def main():
    """
    Function prompts the user for an input to pass into prime_nums(n) function.
    """

    print("Prime Number Sieve")
    print("Input 'q' to quit")
    while True:

        n_input = input("Input an integer to search for primes from [3,n]: ")
        if n_input == "q":
            break

        try:
            n = int(n_input)
            if n < 0:
                raise ValueError("n must be be a positive value")

            prime_nums(n)

        except Exception as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":

    main()
