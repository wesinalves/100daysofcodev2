'''
How to program in Python - Chapter 4
Fibonacci function using recursion
'''

def fibonacci(number):
    '''Generate fibonacci numbers'''
    if number < 0:
        print('Negative value is invalid')
    if number == 0 or number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)
