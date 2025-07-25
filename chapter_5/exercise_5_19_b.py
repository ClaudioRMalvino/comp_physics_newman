"""
Exercise 5.19 Part b): Diffraction grating

Covers part e.i)

Textbook: Computational Physics by Mark Newman 
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab


def q(u, delta_u):
    """
    Calculates the transmission function of a diffraction grating with slits
    a distance delta_u apart at a position u from the central-axis.

    Args:
        float delta_u: The distance in meters between slits
        float u: The distance in meters from the central-axis

    Returns:
        float: Calculation of sin^2(alpha*u) * sin^2(beta*u)
    """

    alpha = np.pi / delta_u  # Periodic condition for slit separation
    beta = 0.5 * alpha
    return (np.sin(alpha * u) ** 2) * (np.sin(beta * u) ** 2)


def intensity(x, wavelength, focal_len, delta_u, num_slits, N):
    """
    Calculates the intensity of a diffraction pattern on a screen a distance x
    from the central axis of the system from diffracted light passing through
    a lens.

    The integration is done by Gaussian Quadrature.

    Args:
        float x: Distance from the central axis
        int wavelength: Wavelength of the incident light [m]
        float f: Focal length of the lens from the screen [m]
        float delta_u : The distance between slits [m]
        int num_slits: The number of slits on the diffraction grating
        int N: Number of slices

    Returns:
        float: Calculated intensity at a point x on the screen
    """

    def integrand(x, u):

        phase = (2 * np.pi * x * u) / (wavelength * focal_len)

        return np.sqrt(q(u, delta_u)) * np.exp(1j * phase)

    w = delta_u * (num_slits - 1)  # Total width of the diffraction grating
    a = -(0.5 * w)  # Lower limit of inegration
    b = 0.5 * w  # Upper limit of integration
    u, weights = gaussxwab(N, a, b)

    result = 0j
    for k in range(N):
        result += weights[k] * integrand(x, u[k])

    return abs(result) ** 2


def intensity_plot(x, intensity):

    plt.plot(x, intensity)
    plt.title("Intensity vs Position")
    plt.xlabel(r"x, m")
    plt.ylabel(r"$I(x)$")
    plt.show()


def intensity_heatmap(intensity):
    """
    Constructs a heat map which represents how the intensity
    would appear on the screen.

    Args:
        array intensity: A (N,1) array of values for intensity along the screen
    """

    plt.figure(figsize=(10, 8))
    plt.imshow(
        intensity_2d, extent=[x_domain[0], x_domain[-1], 0.02, -0.02], cmap="grey"
    )
    plt.colorbar(label="Intensity")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Diffraction Pattern for {num_slits} Slits")
    plt.show()


if __name__ == "__main__":

    N = 1000
    wavelength = 500e-9  # 500 nanometers to meters
    focal_length = 1.0  # [m]
    num_slits = 10
    delta_u = 20e-6  # 20 micrometers to meters
    x_domain = np.linspace(-0.05, 0.05, 500)  # 10 cm wide screen
    intensity_range = np.array(
        [
            intensity(x, wavelength, focal_length, delta_u, num_slits, N)
            for x in x_domain
        ]
    )
    intensity_range = intensity_range / np.max(intensity_range)

    intensity_2d = np.tile(intensity_range, (N, 1))
    intensity_plot(x_domain, intensity_range)
    intensity_heatmap(intensity_2d)
