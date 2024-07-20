import numpy as np

"""
Exercise 4.2: Quadratic Equations

Textbook: Computational Physics by Mark Newman
"""


def quadratic_eq_witherror(a, b, c):
    """
    Function calculates the value of x utilizing the quadratic formula.
    Should produce numerical errors due to accuracy and precision. 
    returns a tuple with lists for the values of x when calculated two different ways.
    quadratic_eq[0] provides a list of the solutions for the standard formula
    quadratic_eq[1] provides a list of the solutions for the alternative formula
    """

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the equation has real roots
    if discriminant < 0:
        return None  # No real roots

    # Solutions for the standard quadratic formula
    x00 = (-b + np.sqrt(discriminant)) / 2*a
    x01 = (-b - np.sqrt(discriminant)) / 2*a

    # Solutions for the alternative formula
    x10 = 2*c / (-b - np.sqrt(discriminant))
    x11 = 2*c / (-b + np.sqrt(discriminant))

    return ([x00, x01], [x10, x11])


def quadratic_eq(a, b, c):
    """
    Function calculates the roots of a quadratic equation ax^2 + bx + c = 0
    accurately in all cases.

    Returns a tuple containing the two roots.
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the equation has real roots
    if discriminant < 0:
        return None  # No real roots

    # Choose the appropriate formula based on the sign of b
    if b >= 0:
        # Use the standard formula for the first root
        x1 = (-b - np.sqrt(discriminant)) / (2*a)
        # Use the alternative formula for the second root
        x2 = (2*c) / (-b - np.sqrt(discriminant))
    else:
        # Use the alternative formula for the first root
        x1 = (2*c) / (-b + np.sqrt(discriminant))
        # Use the standard formula for the second root
        x2 = (-b + np.sqrt(discriminant)) / (2*a)

    return (x1, x2)


def print_solutions(sol_witherror, solution):
    """
    Functions prints the solutions to the quadratic formulas.
    """
    print("Solutions with errors")
    print("-----------------------")
    print(f"Standard Formula: x = [{sol_witherror[0][0]: .10e}, {
          sol_witherror[0][1]: .10e}]")
    print(f"Alternative Formula: x = [{sol_witherror[1][0]: .10e}, {
          sol_witherror[1][1]: .10e}]")
    print("-----------------------")
    print("Solutions without errors")
    print("-----------------------")
    print(f"x = [{solution[0]: .10e}, {solution[1]: .10e}]")


def main():
    """
    Function asks user for input in order to calculate for a quadratic ax^2 + bx + c = 0.
    Prints out solutions for quadratic_eq_witherror and quadratic_eq to show the difference
    in accuracy between the two methods. 
    """

    print("Quadratic Equation Calculator (ax^2 + bx + c = 0)")
    print("Input 'q' to quit")
    while True:

        a_input = input("Input a: ")
        if a_input == 'q':
            break
        b_input = input("Input b: ")
        if b_input == 'q':
            break
        c_input = input("Input c: ")
        if c_input == 'q':
            break

        a = float(a_input)
        b = float(b_input)
        c = float(c_input)

        solutions_witherror = quadratic_eq_witherror(a, b, c)
        solutions = quadratic_eq(a, b, c)

        print(f"Solutions to {a}x^2 + {b}x + {c} = 0")
        print_solutions(solutions_witherror, solutions)


if __name__ == "__main__":
    main()
