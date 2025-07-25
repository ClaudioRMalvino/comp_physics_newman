"""
Exercise 2.11 Part C

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


def unbiased_coin_toss(num_tosses, num_results):
    """
    Function calculates the probability that an unbiased coin tossed
    n times will come up heads or tails k times.

    args:
    int num_tosses: The number of simulated tosses of the coin
    int num_results: The number of times the coin will come up heads or tails

    return:
    float prob: probability of getting num_results within num_tosses
    """
    prob = binomial(n=num_tosses, k=num_results) * (0.5**num_tosses)
    return prob


def prob_k_or_more(num_tosses, K):
    """
    Function calculates the probability of that it comes up heads or tails K
    or more times
    args:
    int num_tosses: The number of simulated tosses of the coin
    int K: The number of results

    return:
    float prob: Probability of getting heads or tails K or more times.
    """
    prob = sum(
        unbiased_coin_toss(num_tosses=num_tosses, num_results=i)
        for i in range(K, num_tosses + 1)
    )
    return prob


if __name__ == "__main__":

    def main():
        """
        Function prompts the user for inputs n,k in order to simulate
        tossing of the unbiased coin. Prints the probability of getting
        heads/tails k times out of n number of flips and the probability
        of getting heads/tails k or more times out of n number of flips.
        """

        print("Unbiased Coin Toss Simulator")
        print("Input 'q' to quit")

        while True:
            n_input = input("Input number of coin tosses (n): ")
            if n_input == "q":
                break

            k_input = input("Input number of desired heads/tails (k): ")
            if k_input == "q":
                break

            try:
                n = int(n_input)
                k = int(k_input)

                if n <= 0:
                    raise ValueError("Error: n must be >= 1")
                if k <= 0 or k > n:
                    raise ValueError("Error: k must be <= 0 and k must be <= n")

                prob1 = unbiased_coin_toss(num_tosses=n, num_results=k)
                prob2 = prob_k_or_more(num_tosses=n, K=k)

                print(
                    f"\nProbability of {
                      k} heads/tails out of {n} tosses: {
                      prob1*100: .2f}%"
                )
                print(
                    f"Probability of heads/tails {k} times or more: {
                        prob2*100: .2f}%\n"
                )
            except ValueError as e:
                print(f"Error: {e}. Please try again")

    main()
