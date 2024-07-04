from math import * 

def time_to_ground():
    """
    Function that calculates total time until object hits the ground when released 
    from a height h. Disregarding air resistence. 
    """
    h = int(input("Input height in meters: "))
    g = 9.81    # Earth gravitational constant
    t = sqrt((2 * h) / g)
    print(f"Total travel time: {round(t,2)} s")

time_to_ground()
