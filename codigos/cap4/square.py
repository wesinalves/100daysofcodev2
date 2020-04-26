'''
How to program in Python - Chapter 4
Creating and using a programmer-defined function.
'''

def square(number):
    '''Defining square function'''
    return number * number

for x in range(1, 11):
    print(square(x))
