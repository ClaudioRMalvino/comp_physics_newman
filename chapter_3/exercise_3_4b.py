from vpython import *
import numpy as np

"""
Exercise 3.4 Part b): Construct a 3D representation of a face-centered cubic
lattice.

Textbook: Computational Physics by Mark Newman
"""


def fcc_lattice(L, R):
    """
    Function constructs a 3D face-centered cubic lattice utilizing vpython.

    args:
    int L: Number of lattice sites
    float R: Radius of spheres

    """
    # Sets up scene
    scene = canvas(title='3D Face-Centered Cubic Lattice', width=800,
                   height=600, background=color.white)

    # Create spheres
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(-L, L+1):
                sphere(pos=vector(i, j, k), radius=R, color=color.red)

                # Face center atoms
                if i < L and j < L:
                    sphere(pos=vector(i+0.5, j+0.5, k),
                           radius=R, color=color.red)
                if i < L and k < L:
                    sphere(pos=vector(i+0.5, j, k+0.5),
                           radius=R, color=color.red)
                if j < L and k < L:
                    sphere(pos=vector(i, j+0.5, k+0.5),
                           radius=R, color=color.red)

    # Create connecting lines
    for i in range(-L, L):
        for j in range(-L, L+1):
            for k in range(-L, L+1):
                curve(pos=[vector(i, j, k), vector(
                    i+1, j, k)], color=color.black)

    for i in range(-L, L+1):
        for j in range(-L, L):
            for k in range(-L, L+1):
                curve(pos=[vector(i, j, k), vector(
                    i, j+1, k)], color=color.black)

    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(-L, L):
                curve(pos=[vector(i, j, k), vector(
                    i, j, k+1)], color=color.black)

    # Add orbital controls
    scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
    To zoom, use scroll wheel or middle button drag or Alt/Option depressed with right button drag."""

    # Keep the script running
    while True:
        rate(30)


if __name__ == "__main__":

    # Global parameters
    L = 2
    R = 0.1

    fcc_lattice(L, R)
