"""
Exercise 5.21 Parts a) and b): Electric field of a charge distribution

Textbook: Computational Physics by Mark Newman
"""

import numpy as np
import matplotlib.pyplot as plt


def electric_potential(particles, x, y):
    """
    Function calculates the electric field at a point (x, y) in an
    N-particle system.

    Args:
        dict particle: A dictionary of particles with values (charge, x_pos, y_pos)
        float x: Test point on the x-axis
        float y: Test point on the y-axis

    Returns:
        float: The electric potential at test position (x, y)
    """
    coulomb_const = 8.99e9  # Coulomb's Contant
    elec_potential = 0.0

    for i in particles.keys():
        charge = particles[i][0]
        x_pos = particles[i][1]
        y_pos = particles[i][2]
        distance = np.sqrt((x - x_pos) ** 2 + (y - y_pos) ** 2)
        elec_potential += charge / distance

    return coulomb_const * elec_potential


def electric_field(particles, x, y, h):
    """
    Calculates the electric field at a point (x, y) for an N-particle system
    utilizing the central difference method.

    Args:
        dict particle: A dictionary of particles with values (charge, x_pos, y_pos)
        float x: Test point on the x-axis
        float y: Test point on the y-axis
        float h: Distance from point of differentation

    Returns:
        float valued tuple of the electric field in the x and y directions
    """

    Ex = (
        electric_potential(particles, x + (h / 2), y)
        - electric_potential(particles, x - (h / 2), y)
    ) / h
    Ey = (
        electric_potential(particles, x, y + (h / 2))
        - electric_potential(particles, x, y - (h / 2))
    ) / h

    return -Ex, -Ey


def plot_elec_potential(particles, grid):
    """
    Function plots the electric potential (edge on),
    density of electric potential, and the electric field lines

    Arg:
        np.ndarray: Grid which represents the cartesian plane

    """

    fig, ax = plt.subplots()
    # Plot 1: Electric Potential (edge on)
    plt.figure(1)
    ax.plot(grid)
    ax.set(
        xticks=np.arange(0, 110, 10),
        title="Electric Potential of the Plane (edge on)",
        xlabel="Distance along x direction, cm",
        ylabel="Electric Potential, V",
    )

    # Plot 2: Density of Electric Potential
    plt.figure(2)
    plt.pcolormesh(grid.T, alpha=0.7)
    plt.colorbar()
    plt.title("Density of Electric Potential Across the Plane")
    x, y = np.meshgrid(np.arange(1, 101, 1), np.arange(1, 101, 1))
    h = 0.1

    # Plot 3: Electric Field
    plt.figure(3)
    plt.streamplot(
        x,
        y,
        electric_field(particles, x, y, h)[0],
        electric_field(particles, x, y, h)[1],
        density=2,
    )
    plt.title("Electric Field between $+q_1$ and $-q_2$")
    plt.show()


def main():

    print("Electric potential and Electric field calculator")
    print("Input 'q' to quit.")

    while True:
        num_particles = input("Input number of particles (integer >= 2): ")
        if num_particles == "q":
            break
        num_particles = int(num_particles)
        if num_particles < 2:
            raise Exception("Number of particles must be greater than 2.")

        particles = {}
        for i in range(num_particles):

            charge_input = input(f"Input charge of particle {i+1}: ")
            if charge_input == "q":
                break

            x_pos_input = input(f"Input x_pos of particle {i+1} [0,100]: ")
            if x_pos_input == "q":
                break

            x_pos = float(x_pos_input)
            if (x_pos < 0) or (x_pos > 100):
                raise Exception("x_pos must be 0 <= x_pos <= 100. Try again.")

            y_pos_input = input(f"Input y_pos of particle {i+1} [0,100]: ")
            if y_pos_input == "q":
                break

            y_pos = float(y_pos_input)
            if (y_pos < 0) or (y_pos > 100):
                raise Exception("y_pos must be 0 <= y_pos <= 100. Try again.")

            particles[i] = (int(charge_input), x_pos, y_pos)

        # vectorizes the potential in order to utilize it in the loop
        vect_potential = np.vectorize(electric_potential)

        grid = np.zeros((100, 100))  # creates 2D plane that is 100 x 100

        x2 = np.arange(1, 101, 1)
        y2 = np.arange(1, 101, 1)

        for i in range(0, len(x2) - 1):
            for j in range(0, len(y2) - 1):
                grid[i, j] = vect_potential(particles, i, j)

        plot_elec_potential(particles, grid)


if __name__ == "__main__":

    main()
