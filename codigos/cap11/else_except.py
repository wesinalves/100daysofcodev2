'''
How to program in Python - Chapter 11
Simple exception handling example.
'''

def main():
    '''Main function'''
    number1 = input("Enter numerator: ")
    number2 = input("Enter denominator: ")

    # attempt to convert and divide values
    try:
        number1 = float(number1)
        number2 = float(number2)
        result = number1 / number2

    # float raises a ValueError exception
    except ValueError:
        print("You must enter two numbers")

    # division by zero raises a ZeroDivisionError exception
    except ZeroDivisionError:
        print("Dividing by zero is not allowed")

    # else clause's suite executes if try suite raises no exceptions
    else:
        print("{:.3f} / {:.3f} = {:.3f}".format(number1, number2, result))

main()