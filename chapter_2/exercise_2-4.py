from math import sqrt

"""
Exercise 2.4: Calculating travel time from two different reference frames at relativistic speeds.
"""

c = 2.0E+8  # Speed of light in m/s


def earth_ref_frame(x, v):
    """
    Function that calculates the time it takes to travel distance x at a
    fraction of the speed of light v*c from Earth reference point.

    int x: distance in light years
    float v: a value (0,1] 

    returns travel time in light years
    """
    x_meters = x * 9.460730E+15
    beta = v*c
    return x_meters/beta


def ship_ref_frame(x, v):
    """
    Function that calculates proper time from the reference frame of the passenger on the
    ship traversing a distance x at a velocity a fraction of the speed of light c
    """
    gamma = 1 / sqrt(1 - v**2)
    return earth_ref_frame(x, v)/gamma

if __name__ == "__main__":

    def main():
        """
        Functions asks inputs for x (distance in light years) and v (a number (0,1]) to 
        to calculate the time it takes for a spaceship to travel a distance x at velocity v*c
        for Earth reference frame and passenger reference frame. 
        """
    
        while True:
            print("\nCalculating travel time from Earth reference frame and passenger reference frame.")
            print("Input 'q' to quit.")
    
            x_input = input("Input distance in lightyears: ")
            if x_input == 'q':
                break
    
            v_input = input(
                "Input velocity as a fraction of speed of light (number from (0,1]):")
            if v_input == 'q':
                break
            try:
                x = float(x_input)
                v = float(v_input)
    
                if v <= 0 or v >= 1:
                    raise ValueError("Velocity must be between (0,1]")
    
                earth_frame = earth_ref_frame(x, v) / 31556952
                ship_frame = ship_ref_frame(x, v) / 31556952
    
                print(f"\nTravel time from Earth reference frame: {
                      round(earth_frame, 2)}")
                print(f"Travel time from ship reference frame: {
                      round(ship_frame, 2)}\n")
    
            except ValueError as e:
                print(f"Error:{e}. Please try again.")


    main()
