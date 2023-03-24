# Python Journey - Chapter 11
# Demonstrating a programmer-defined exception class.

import math

class NegativeNumberError(ArithmeticError):
    """Attempted improper operation on negative number."""
    pass

def square_root(number):
    """Computes square root of number."""

    if number < 0:
        raise NegativeNumberError("Square root of negative number not permitted")
    
    return math.sqrt(number)

def main():
    '''Main Program'''
    while 1:
        # get user-entered number and compute square root
        try:
            user_value = float(input("\nPlease enter a number: "))
            print(square_root(user_value))
        except ValueError:
            print("The entered value is not a number")
        except NegativeNumberError as e:
            print(e)
        else:
            break

if __name__ == '__main__':
    main()
