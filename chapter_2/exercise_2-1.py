from math import * 
"""
Exercise 2.1: Another ball dropped from a tower 

Textbook: Computational Physics by Mark Newman 
"""
def time_to_ground():
    """
    Function that calculates total time until object hits the ground when released 
    from a height h. Disregarding air resistence. 
    """
    h = int(input("Input height in meters: "))
    g = 9.81    # acceleration due to gravity
    t = sqrt((2 * h) / g)
    print(f"Total travel time: {round(t,2)} s")

time_to_ground()
