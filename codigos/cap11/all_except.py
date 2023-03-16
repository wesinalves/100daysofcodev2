'''
How to program in Python - Chapter 11
Catch all exception example.
'''

import random

def main():
    '''Catch all exceptions.'''
    for i in range(10):
        # Loop 10 times
        print('####### Beginning of loop iteration', i)
        try:
            r = random.randint(1, 5)
            # r is pseudorandomly 1, 2, 3, or 4
            match r:
                # r is pseudorandomly 1, 2, 3, or 4
                case 1:
                    print(int('one')) # Try to convert a non-integer
                case 2:
                    [][2] = 5
                # Try to assign to a nonexistent index of the empty list
                case 3:
                    print({}[1]) # Try to use a nonexistent key to get an item from a dictionary
                case 4:
                    print(3/0) # Try to divide by zero
                case _:
                    print(x)
        except ValueError:
            print('Cannot convert integer')
        except IndexError:
            print('List index is out of range')
        except ZeroDivisionError:
            print('Division by zero not allowed')
        except NameError:
            print('Variable must be declared')
        except:
            # Catch absolutely any other type of exception
            print('This program has encountered a problem')

if __name__ == '__main__':
    main()
    