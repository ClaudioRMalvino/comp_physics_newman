from vpython import *

"""
Exercise 3.4 Part a): Construct a 3D representation of sodium chloride lattice

Textbook: Computational Physics by Mark Newman
"""


def nacl_lattice(L, R):
    """
    Function constructs a 3D lattice of sodium chloride utilizing vpython.

    args:
    int L: Number of lattice sites
    float R: Radius of spheres

    """
    # Sets up scene
    scene = canvas(title='3D Sodium Chloride', width=800,
                   height=600, background=color.white)

    # Create spheres
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(-L, L+1):
                if abs(i+j+k) % 2 == 0:
                    sphere(pos=vector(i, j, k), radius=R, color=color.red)
                else:
                    sphere(pos=vector(i, j, k), radius=R, color=color.blue)

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
    scene.caption = """Sodium (Red); Chlorine (Blue).\nTo rotate "camera", drag with right button or Ctrl-drag.
    To zoom, use scroll wheel or middle button drag or Alt/Option depressed with right button drag."""

    # Keep the script running
    while True:
        rate(30)


if __name__ == "__main__":

    # Global parameters
    L = 5
    R = 0.3

    nacl_lattice(L, R)
