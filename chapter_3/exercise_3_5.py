from vpython import *
import numpy as np

"""
Exercise 3.5: Visualization of the solar system

Textbook: Computational Physics by Mark Newman
"""


def ang_vel(T):
    """
    Calculates angular velocity, omega
    """
    return 2 * np.pi / T


def solar_system():
    """
    Function construct the 3D model of our solar system.
    Returns a list of lists containing the planet objects, 
    their radius frome the sun, and their orbital period in days.
    """
    # Scene settings
    scene = canvas(title='Solar System',
                   width=1000,
                   height=600,
                   background=color.black)
    local_light(pos=vector(0., 0., 0.), color=color.white)

    # Constructs the bodies in the solar system
    sun = sphere(pos=vector(0., 0., 0.),
                 radius=0.05*695500.,
                 color=color.yellow,
                 emissive=True)
    mercury = sphere(pos=vector(22*58., 0., 0.),
                     radius=2440.,
                     texture=textures.rock)
    venus = sphere(pos=vector(25*108., 0., 0.),
                   radius=5052.,
                   color=color.orange,
                   texture=textures.granite)
    earth = sphere(pos=vector(25*150., 0., 0.),
                   radius=6371.,
                   texture=textures.earth)
    mars = sphere(pos=vector(25*230., 0., 0.),
                  radius=3386,
                  color=color.orange,
                  texture=textures.rough)
    jupiter = sphere(pos=vector(10*779., 0., 0.),
                     radius=0.1*69173,
                     texture=textures.wood_old)
    saturn = sphere(pos=vector(7*1433.0, 0., 0.),
                    radius=0.1*57316,
                    color=color.yellow,
                    texture=textures.wood)

    # Holds the planet objects, with their respective radius from
    # the sun and their orbital period in days
    planets = [
        [mercury, 22*58, 88],
        [venus, 25*108., 225],
        [earth, 25*150., 365],
        [mars, 25*230., 687],
        [jupiter, 10*779, 4333],
        [saturn, 7*1433, 10759]
    ]

    return planets


if __name__ == "__main__":

    # Animation loop
    day = 0
    dt = 0.5

    # Holds the list of planets
    planets = solar_system()

    while True:
        rate(60)
        day += dt

        for planet, r, T in planets:
            # Keeps angle within [0, 2pi]
            theta = (ang_vel(T) * day) % (2 * np.pi)
            x = 50 * r * np.cos(theta)
            z = 50 * r * np.sin(theta)
            planet.pos = vector(x, 0, z)
