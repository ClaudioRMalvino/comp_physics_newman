import numpy as np
import matplotlib.pyplot as plt

"""
Exercise 3.6: Feigenbaum Plot

Textbook: Computational Physics by Mark Newman
"""


def logistic_map(r, x0, iterations):
    """
    Calculate the logistic map for a given r value.

    args:
    r: The r parameter in the logistic map equation
    x0: Initial x value
    iterations: Number of iterations

    returns: Array of x values after n+m iterations
    """
    x = np.zeros(iterations)
    x[0] = x0
    for i in range(1, iterations):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x


def feigenbaum_plot(r_min, r_max, dr, x0, iterations):
    """
    Generate data for the Feigenbaum diagram.

    args:
    r_min, r_max: Range of r values to plot
    dr: Step size for r values
    x0: Initial x value
    iterations: Number of iterations
    returns: r_values, x_values for plotting
    """
    r_values = np.arange(r_min, r_max, dr)
    x_values = []

    for r in r_values:
        x = logistic_map(r, x0, iterations)
        x_values.extend([(r, xi) for xi in x])

    return zip(*x_values)


def main():
    """
    Function asks the user for inputs for plotting the Feigenbaum Diagram.
    Asks for the range of r, steps dr, intitial value of x, and number of iterations
    """

    print("Feigenbaum Plot Generator")
    print("Input 'q' to quit")

    while True:

        r_min_input = input("Input r_min (range: [-2, 4]): ")
        if r_min_input == 'q':
            break
        r_max_input = input("Input r_max (range: [-2, 4]): ")
        if r_max_input == 'q':
            break
        dr_input = input("Input increment (dr must be > 0): ")
        if dr_input == 'q':
            break
        x0_input = input("Input initial x value (x0 must be >0): ")
        if x0_input == 'q':
            break
        iter_input = input("Input number of iterations (must be > 0): ")
        if iter_input == 'q':
            break
        try:
            r_min = float(r_min_input)
            r_max = float(r_max_input)
            dr = float(dr_input)
            x0 = float(x0_input)
            iter = int(iter_input)

            if r_min > r_max:
                raise ValueError("r_min must be greater than r_max")
            if r_min < 2 and r_min > 4:
                raise ValueError("r_min must be within [2, 4]")
            if r_max < 2 and r_max > 4:
                raise ValueError("r_max must be within [2, 4]")
            if dr <= 0:
                raise ValueError("dr must be greater than 0")
            if iter <= 0:
                raise ValueError("Number of iterations must be greater than 0")
            if x0 <= 0:
                raise ValueError("x0 must be greater than 0")

            # Calculates our r,x values
            r, x = feigenbaum_plot(r_min, r_max, dr, x0, iter)

            # Plots the Feigenbaum Diagram
            plt.figure(figsize=(12, 8))
            plt.plot(r, x, ',k', alpha=0.4, markersize=0.1)
            plt.title('Feigenbaum Diagram (Logistic Map)')
            plt.xlabel('r')
            plt.ylabel('x')
            plt.ylim(0, 1)
            plt.show()

        except Exception as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":
    main()
