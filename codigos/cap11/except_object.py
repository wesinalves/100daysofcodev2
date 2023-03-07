import random

def main():
    for i in range(10):
        # Loop 10 times
        print('####### Beginning of loop iteration', i)
        try:
            r = random.randint(1, 5)
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
        except ValueError as e:
            print('Cannot convert integer', type(e), e)
        except IndexError as e:
            print('List index is out of range', type(e), e)
        except ZeroDivisionError as e:
            print('Division by zero not allowed', type(e), e)
        except NameError as e:
            print('Variable must be declared', type(e), e)
        except Exception as e:
            # Catch absolutely any other type of exception
            print('This program has encountered a problem', type(e), e)

if __name__ == '__main__':
    main()