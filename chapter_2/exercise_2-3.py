from math import atan, sqrt, pi

"""
Exercise 2.3: Converting Cartesian coordinates to polar coordinates
"""


def cart_to_polar(x, y):
    """
    Function converts Cartesian coordinates into polar coordinates.
    """
    r = sqrt((x**2) + (y**2))
    theta = atan(y/x)
    print(f"Cartesian Coordinates: ({x}, {
          y}) -> Polar Coordinates: ({round(r, 2)}, {round(theta * (180 / pi), 2)})")


if __name__ == "__main__":

    def main():
    """
    Function performs the process of taking the inputs for the Cartesian coordinates (x,y).
    Then utilizes the cart_to_polar(x,y) function to calculate the provided inputs.
    """

    while True:
    inputx = input("Converting Cartesian to Polar\nInput 'q' to quit \
                        \nInput x coordinate: ")
       if inputx == 'q':
            break
        inputy = input("\nInput y coordinate: ")
        if inputy == 'q':
            break

        x = float(inputx)
        y = float(inputy)
        cart_to_polar(x, y)


    main()
