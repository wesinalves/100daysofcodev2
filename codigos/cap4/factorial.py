'''
How to program in Python - Chapter 4
Factorial function using recursion
'''

def factorial(number):
    '''Factorial of a number'''
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print(factorial(10))
