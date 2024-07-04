from math import pi

"""
Exercise 2.2 Altitude of a satellite 

Textbook: Computational Physics by Mark Newman
"""
def altitude(T):
    """
    Function calculates the orbital height of a satellite when given an orbital period T.
    Returns the height in meters.
    """    
    G = 6.67E-11
    M = 5.97E+24
    R = 6.37E+6
    h = ((G * M * (T**2))/(4 * (pi**2)))**(1/3) - R
    print(f"Required altitude: {round(h, 0)} m")

def altitude_of_sat():
    """
    Function holds the logical operations for selectiong the desired metric of orbital period T.
    It then calls function altitude(T) to calculate the orbital height of the satellite utilizing
    the input. 
    """
    q = True

    while q:
        T_input = input("If desired orbital period is in minutes input 'min'\ntype 'q' to quit\nInput orbital period (in hours): ")

        if T_input == "min":
            T_input = int(input("Input orbital period (in minutes): "))
            T_sec = 60 * T_input
            altitude(T_sec)
        elif T_input == "q":
            q = False
        else:
            T_sec = 3600 * float(T_input)
            altitude(T_sec)

altitude_of_sat()

