"""
Exercise 5.21 Part c): Electric field of a charge distribution 

For this exercise, and all exercises moving forward, I want to move away from utilizing the user-defined function
that performs Gaussian quadrature and refrain from taking the derivitive 
myself (as was done in exercise_21_ab.py) in order to become more familiar 
with the numpy and scipy libraries. 

Textbook: Computational Physics by Mark Newman
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def charge_density(ypos: float, xpos: float, length: float, charge: int) -> float:
    """
    Function describes the charge density of a continuous LxL square.

    Args:
        float xpos: Position on the x-axis
        float ypos: Position on the y-axis
        float length: Length
        int charge: The charge carried by the object

    Returns:
        float: The charge density
    """
    return (
        charge * np.sin(2 * np.pi * xpos / length) * np.sin(2 * np.pi * ypos / length)
    )


def potential_integrand(
    ypos: float, xpos: float, x_point: float, y_point: float, length: float, charge: int
) -> float:
    """
    Function contains the integrand for calculating the electric potential
    of a continuous charge.

    Args:
        xpos (float): Position on the x-axis
        ypos (float): Position on the y-axis
        x_point (float): Test point for calculating potential on x-axis
        y_point (float): Test point for calculating potential on y-axis
        length (float): Length of continues charge
        charge (float): The charge carried by the object


    Returns:
        return description
    """

    distance = np.sqrt((x_point - xpos) ** 2 + (y_point - ypos) ** 2)
    if distance < 1e-10:  # Avoid division by zero
        return 0
    return charge_density(xpos, ypos, length, charge) / (distance + 1.0e-10)


def calculate_potential(
    x_point: float, y_point: float, length: float, charge: int
) -> float:
    """Calculate electric potential at a point using double integral"""
    k = 8.99e9  # Coulomb's constant in N⋅m²/C²

    # Limits of integeration
    x_min, x_max = x_point - length / 2, x_point + length / 2
    y_min, y_max = y_point - length / 2, y_point + length / 2

    # Perform double integral
    result, _ = sp.integrate.dblquad(
        lambda ypos, xpos: potential_integrand(
            ypos, xpos, x_point, y_point, length, charge
        ),
        x_min,
        x_max,
        lambda ypos: y_min,
        lambda ypos: y_max,
        epsabs=1e-3,  # Absolute tolerance
        epsrel=1e-3,  # Relative tolerance
    )

    return k * result


def plot_results(X: np.ndarray, Y: np.ndarray, Ex: np.ndarray, Ey: np.ndarray) -> None:
    """
    Plots the electric field of a continuous distribution of charge over
    and L x L square.

    Args:
        X (array): Grid of positions on x-axis
        Y (array): Grid of positions on y_axis
        Ex (array): The x-component of the electric field at (X,Y)
        Ey (array): The y-component of the electric field at (X,Y)

    """

    plt.figure(figsize=(10, 8))
    plt.streamplot(X * 100, Y * 100, Ex, Ey)  # Convert to cm for display
    plt.title("Electric Field Vector Plot")
    plt.xlabel("x (cm)")
    plt.ylabel("y (cm)")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


def main() -> None:

    # Parameters
    length = 0.1  # 10 cm converted to meters
    charge = 100  # C/m^2
    n_points = 20  # Number of points in each dimension (1 cm spacing over 10 cm)

    # Create grid of points
    x = np.linspace(-length / 2, length / 2, n_points)
    y = np.linspace(-length / 2, length / 2, n_points)
    X, Y = np.meshgrid(x, y)

    # Calculate potential at each point
    V = np.zeros((n_points, n_points))
    for i in range(n_points):
        for j in range(n_points):
            V[i, j] = calculate_potential(X[i, j], Y[i, j], length, charge)

    # Calculate electric field components (E = -∇V)
    Ex, Ey = np.gradient(-V, x, y)

    plot_results(X, Y, Ex, Ey)


if __name__ == "__main__":

    main()
