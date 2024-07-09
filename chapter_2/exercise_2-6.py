import numpy as np

"""
Exercise 2.6: Planetary Orbit

Textbook: Compuational Physics by Mark Newman
"""

# Global Variables
M = 1.9891E+30  # Mass of the Sun
G = 6.6738E-11  # Netwon's gravitational constant


def v2(v1, l1):
    """
    Function calculates the velocity of the planetary body at its aphelion by taking its velocity
    and distance from the Sun at its perihelion, as v1 and l1, respectively.

    float v1: velocity at perihelion
    float l1: distance from Sun at perihelion

    returns velocity at aphelion
    """
    solutions = []

    v2plus = (((2*G*M) / (v1*l1)) + np.sqrt((-(2*G*M) / (v1*l1))
              ** 2 - 4*(-v1**2 + ((2*G*M) / (l1))))) / 2
    solutions.append(v2plus)

    v2minus = (((2*G*M) / (v1*l1)) - np.sqrt((-(2*G*M) / (v1*l1))
               ** 2 - 4*(-v1**2 + ((2*G*M) / (l1))))) / 2
    solutions.append(v2minus)

    return min(solutions)


def l2(v1, l1, v2):
    """
    Function caculates the distance from the Sun at aphelion.

    float v1: Velocity at perihelion
    float l1: Distance from the Sun at perihelion
    float v2: Velocity at aphelion

    returns l2 distance from the sun at aphelion
    """
    return (l1*v1) / np.abs(v2)


def a(l1, l2):
    """
    Function calculates the semi-major axis of the planetary bodies orbit provided the distance
    from the sun at perihelion and aphelion.

    float l1: Distance from the sun at perihelion
    float l2: Distance from the sun at aphelion

    returns the semi-major axis usually denoted as 'a'
    """
    return (1 / 2)*(l1 + l2)


def b(l1, l2):
    """
    Function calculates the semi-minor axis of the planetary bodies orbit provided the distance
    from the sun at perihelion and aphelion.

    float l1: Distance from the sun at perihelion
    float l2: Distance from the sun at aphelion

    returns the semi-minor axis usually denoted as 'b'
    """
    return np.sqrt(l1*l2)


def orbital_period(a, b, l1, v1):
    """
    Function calculated the orbital period of the plantery body provided the semi-major and semi-minor
    axis, and l1 and v1.

    float a: Semi-major axis calculated with a()
    float b: Semi-minor axis calculated with b()
    float l1: Distance from the Sun at perihelion
    float v1: Velocity at perihelion

    returns the oribital period of the body usually denoted as 'T'
    """
    return (2 * np.pi * a * b) / (l1 * v1)


def orbital_eccent(l1, l2):
    """
    Function calculates the orbital eccentricity of the planetary body provided the distance from the Sun
    at perihelion and aphelion, l1 and l2 respectively.

    float l1: Distance from the sun at perihelion
    float l2: Distance from the sun at aphelion

    returns the eccentricity of the orbit
    """
    return (l2 - l1) / (l2 + l1)


def main():
    """
    Function take the user input for v1 and l1 and then returns the completed calculations for the following:
    - l2: Distance from the sun at aphelion
    - v2: Velocity at aphelion
    - T: Orbital period
    - e: Orbital eccentricity
    """
    print("Orbital Properties Calculator")
    print("Input 'q' to quit")

    while True:

        v1_input = input("Input perihelion velocity (v1): ")
        if v1_input == 'q':
            break

        l1_input = input("Input perihelion distance (l1): ")
        if l1_input == 'q':
            break

        try:
            v1 = float(v1_input)
            l1 = float(l1_input)

            if v1 < 0 or l1 < 0:
                raise ValueError("l1 & v1 can't have a negative value.\n \
                Please try again.")

            v2_val = v2(v1, l1)
            l2_val = l2(v1, l1, v2_val)
            a_val = a(l1, l2_val)
            b_val = b(l1, l2_val)
            T = orbital_period(l1=l1, v1=v1, a=a_val, b=b_val)
            ecc = orbital_eccent(l1, l2_val)

            print(f"\nVelocity at aphelion (v2) = {
                np.format_float_scientific(v2_val, precision=4)} m/s")
            print(f"Distance from Sun at aphelion (l2) = {
                np.format_float_scientific(l2_val, precision=4)} m")
            print(f"Orbital period (T) = {
                np.format_float_scientific(T/3.154E+7, precision=4)} years")
            print(f"Orbital eccentricity = {
                np.format_float_scientific(ecc, precision=4)}")

        except ValueError as e:
            print(f"Error:{e}. Please try again.")


if __name__ == "__main__":

    main()
