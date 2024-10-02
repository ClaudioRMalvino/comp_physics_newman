"""
Exercise 5.9 Heat capacity of a solid

Textbook: Computational Physics by Mark Newman
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab


def cv(T, V, rho, theta, N):
    """
    Function calculates the heat capacity of a material utilizing the Debeye
    theory of solids.

    Args:
        float T: Temperature [K]
        float V: Volume [m^3]
        float rho: Number density of atoms [m^3]
        float theta: Debeye temperature of a material [K]
        int N: Number of sample points

    Returns:
        float: Heat capacity of material   
    """
    def f(x):
        numerator = (x**4)*(np.e**x)
        denominator = ((np.e**x)-1)**2
        return numerator/denominator

    kb = 1.380649e-23  # Bolztmann's constant [J/K]
    a = 0.0
    b = theta/T
    x, w = gaussxwab(N, a, b)
    s = 0.0
    for k in range(N):
        s += w[k] * f(x[k])

    coefficient = 9 * V * rho * kb * ((T/theta)**3)
    return coefficient * s


def cvplot(x, y):

    plt.plot(x, y)
    plt.title("Heat Capacity vs Temperature")
    plt.xlabel("Temperature, K")
    plt.ylabel(r"$C_{v}$")

    plt.show()


if __name__ == "__main__":

    T = 5
    V = 0.001
    rho = 6.002e+28
    theta = 428.0
    N = 50
    Vcv = np.vectorize(cv)
    heatCapacity = [Vcv(t, V, rho, theta, N) for t in range(5, 500+1)]
    T_range = [t for t in range(5, 500+1)]

    print(f"Heat Capacity for {V} cubic meters of Al at T = {
          T} K: \nC_v = {round(cv(T, V, rho, theta, N), 4)}")
    cvplot(x=heatCapacity, y=T_range)
