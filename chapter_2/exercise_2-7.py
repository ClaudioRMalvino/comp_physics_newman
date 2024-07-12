"""
Exercise 2.7: Catalan numbers

Textbook: Computational Physics by Mark Newman
"""


def catalan_num(max_val):
    """
    Function calculates Catalan numbers for numbers <= max_val and
    prints each Catalan number within the range max_val

    int max_val: maximum value for range of Catalan numbers

    """
    c0 = 1
    n = 1
    while c0 <= max_val:
        print(int(c0))
        cn = ((4*n + 2)/(n + 2)) * c0
        n += 1
        c0 = cn

if __name__ == "__main__":
    
    def main():
        """
        Function takes user input to provide to the catalan_num() function
        as input.
        """
    
        print("Catalan number generator")
        print("Input 'q' to quit")
    
        while True:
    
            val_input = input("Input an integer > 0: ")
            if val_input == 'q':
                break
    
            try:
                val = int(val_input)
                if val <= 0 or val == float:
                    raise ValueError("The value must be an integer and > 0.")
    
                catalan_num(val)
    
            except ValueError as e:
                print(f"Error:{e}. Please try again.")

    main()
