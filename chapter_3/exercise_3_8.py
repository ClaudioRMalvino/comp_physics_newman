import numpy as np
from scipy import constants
import matplotlib.pyplot as plt

"""
Exercise 3.8: Least-square fitting and the photoelectric effect

Textbook: Computational Physics by Mark Newman

You can find the data millikan.txt @ https://public.websites.umich.edu/~mejn/cp/
"""


def Ex(x):
    N = len(x)
    return (1/N) * (np.sum(x))


def Ey(y):
    N = len(y)
    return (1/N) * (np.sum(y))


def Exx(x):
    N = len(x)
    return (1/N) * (np.sum(x**2))


def Exy(x, y):
    N = len(x)
    return (1/N) * (np.sum(x * y))


def m(Ex, Ey, Exx, Exy):
    """
    Function calculates the slop of the line, m, from the least-squares fit equation
    """
    return (Exy - Ex*Ey) / (Exx - Ex**2)


def c(Ex, Ey, Exx, Exy):
    """
    Function calculates the slope intercept, c, from the least-squares fit equation
    """
    return (Exx*Ey - Ex*Exy) / (Exx - Ex**2)


def per_diff(V1, V2):
    """
    Function calculates the percent difference between two values
    """
    return round(((np.abs(V1 - V2)) / ((V1 + V2)/2)) * 100, 2)


if __name__ == "__main__":

    data = np.loadtxt("millikan.txt", float)
    x = data[:, 0]
    y = data[:, 1]

    Ex = Ex(x)
    Ey = Ey(y)
    Exx = Exx(x)
    Exy = Exy(x, y)
    m = m(Ex, Ey, Exx, Exy)
    c = c(Ex, Ey, Exx, Exy)
    line = list(map(lambda x: m*x + c, x))
    e = constants.e
    exp_h = m * e
    theory_h = constants.h
    print(f"slope = {m}\nintercept = {c}")
    print(f"Experimental Planck constant, h = {exp_h}")
    print(f"Theoretical Planck constant, h = {theory_h}")
    print(f"Percent difference from theoretical value and experimental =\
 {per_diff(exp_h, theory_h)}%")

    plt.scatter(x, y)
    plt.plot(x, line)
    plt.title("Millikan Oil-Drop Experiment")
    plt.xlabel("Frequency, $s^{-1}$")
    plt.ylabel("Voltage, $V$")
    plt.show()
