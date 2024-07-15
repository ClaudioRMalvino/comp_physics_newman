import matplotlib.pyplot as plt
import numpy as np

"""
Exercise 3.2: Curve Plotting

Textbook: Computational Physics by Mark Newman
"""


def deltoid_curve():
    """
    Function calculates the values for the deltoid curve.
    Returns the values for x and y.
    """
    theta = np.linspace(0, 2*np.pi, 1000)
    x = 2 * np.cos(theta) + np.cos(2 * theta)
    y = 2 * np.sin(theta) - np.sin(2 * theta)

    return x, y


def galilean_spiral():
    """
    Function calculates the values for x,y to plot the Galilean spiral.
    Where r = \theta^2 for \theta: [0, 10*pi].

    Returns the values for x and y.
    """

    theta = np.linspace(0, 10 * np.pi, 1000)

    x = (theta**2) * np.cos(theta)
    y = (theta**2) * np.sin(theta)

    return x, y


def feys_function():
    """
    Function calculates the values for x,y to plot Fey's function.

    Returns the values for x, y
    """

    theta = np.linspace(0, 24 * np.pi, 1000)

    r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.sin(theta/12)**5
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y


def plt_figs(funcs, titles):
    """
    Function plots graphs of functions provided in the parameters with
    the title provided as well.

    """
    figures = []

    for i in range(len(funcs)):
        fig = plt.figure(i)
        figures.append(fig)
        plt.plot(funcs[i][0], funcs[i][1])
        plt.title(titles[i])
        plt.xlabel("x")
        plt.ylabel("y")
    plt.show()
    return figures


if __name__ == "__main__":

    funcs = [deltoid_curve(), galilean_spiral(), feys_function()]
    titles = ["Deltoid Curve", "Galilean Spiral", "Fey's Function"]

    plt_figs(funcs=funcs, titles=titles)
