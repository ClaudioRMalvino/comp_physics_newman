import numpy as np
import matplotlib.pyplot as plt
import time

"""
Exercise 5.4 Part b): The diffraction limit of a telescope

Textbook: Computational Physics by Mark Newman
"""


def J(m, x):
    """
    Function represents the Bessel function, evaluated for m and x
    utilizing the extended simpson rule for integration.
    """
    def f(m, x, theta):
        """
        Function calculates (1/pi)*cos(m*theta -x*sin(theta))
        """
        return np.cos(m*theta - x*np.sin(theta))

    def ext_simspon_rule(m, x):
        """
        Function performs the extended Simpson rule for approximating integrals
        """
        N = 1000    # Number of slices
        a = 0.      # Starting point
        b = np.pi   # End point
        h = (b - a)/N   # Width of slices
        c = h/3.0   # caluclated the constant to reduce computation
        # holds the first term in the Ext Simpson Rule
        I = c * (f(m, x, a) + f(m, x, b))
        odds = 0.
        evens = 0.
        # Loops through for the odd and even summations of the Ext Simpson Rule
        for k in range(1, N, 2):
            odds += f(m, x, k*h)
        for k in range(2, N, 2):
            evens += f(m, x, k*h)

        I += c * (4*odds + 2*evens)

        return (1/np.pi) * I
    J = ext_simspon_rule(m, x)
    return J


def I(r, lamda):
    """ Function calculates the intensity of the light diffracted within a telescope """

    k = 2*np.pi/lamda
    I = ((J(1, k*r))/(k*r))**2
    return I


def plot_func(values):
    """ Function plots a heatmap of the calculated intensity """

    # Plot the result
    plt.figure(figsize=(10, 8))
    plt.imshow(values, extent=[-1, 1, -1, 1], cmap='viridis', vmax=0.01)
    plt.colorbar(label='Intensity')
    plt.title('Airy Disk Pattern')
    plt.xlabel('x, ${\mu}m)$')
    plt.ylabel('y, ${\mu}m$')
    plt.show()


if __name__ == "__main__":

    t0 = time.time()
    lamda = 0.5  # Unit micrometers
    N = 500     # Higher N increases resolution
    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)

    # Constructs the grid of values
    X, Y = x[:, np.newaxis], y[np.newaxis, :]
    # Constructs an array for the radius along the grid {x, y]
    R = np.sqrt(X**2 + Y**2)
    intensity = I(R, lamda)
    tf = time.time()
    run_time = tf - t0
    print(f"Execution time: {run_time}")
    plot_func(intensity)
