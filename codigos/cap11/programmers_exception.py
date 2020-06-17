# Python Journey - Chapter 11
# Demonstrating exception arguments and stack unwinding.

import math

class NegativeNumberError(ArithmeticError):
    """Attempted improper operation on negative number."""
    pass

def square_root(number):
    """Computes square root of number. Raises NegativeNumberError
    if number is less than 0."""

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
        except NegativeNumberError as exception:
            print(exception)
        else:
            break

main()
