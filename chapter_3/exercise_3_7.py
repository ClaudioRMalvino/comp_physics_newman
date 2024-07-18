
import numpy as np
import matplotlib.pyplot as plt
from numba import jit
"""
Exercise 3.7: The Mandelbrot Set

Textbook: Computational Physics by Mark Newman
"""


@jit(nopython=True)
def mandelbrot(ext, max_steps, Nx, Ny):
    """
    Function calculates the values for plotting the Mandelbrot set.
    """

    # Holds the values for the NxN array
    data = np.ones((Nx, Ny)) * max_steps
    for i in np.arange(Nx):
        for j in np.arange(Ny):
            x = ext[0] + (ext[1] - ext[0])*i / (Nx - 1.)
            y = ext[2] + (ext[3] - ext[2])*j / (Ny - 1.)
            z0 = x + y*1j
            z = 0j
            for n in np.arange(max_steps):
                if np.abs(z) > 2.:
                    data[j, i] = n
                    break
                z = z*z + z0
    return data


def ax_update(ax):
    ax.set_autoscale_on(False)
    xstart, ystart, xdelta, ydelta = ax.viewLim.bounds
    xend = xstart + xdelta
    yend = ystart + ydelta
    ext = np.array([xstart, xend, ystart, yend])
    data = mandelbrot(ext, max_steps, Nx, Ny)

    im = ax.images[-1]
    im.set_data(data)
    im.set_extent(ext)
    ax.figure.canvas.draw_idle()


if __name__ == "__main__":

    Nx = 1000
    Ny = 1000
    max_steps = 1000

    # The region in which we will be calculating the Mandelbrot set
    ext = [-2, 2, -2, 2]
    data = mandelbrot(np.array(ext), max_steps, Nx, Ny)

    fig, ax = plt.subplots(1, 1)
    ax.imshow(data, extent=ext, origin='lower')
    ax.callbacks.connect('xlim_changed', ax_update)
    ax.callbacks.connect('ylim_changed', ax_update)
    plt.show()
