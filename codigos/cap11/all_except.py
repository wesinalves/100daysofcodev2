import random

for i in range(10):
    # Loop 10 times
    print('####### Beginning of loop iteration', i)
    try:
        r = random.randint(1, 5)
        # r is pseudorandomly 1, 2, 3, or 4
        if r == 1:
            print(int('um')) # Try to convert a non-integer
        elif r == 2:
            [][2] = 5
        # Try to assign to a nonexistent index of the empty list
        elif r == 3:
            print({}[1]) # Try to use a nonexistent key to get an item from a dictionary
        elif r == 4:
            print(3/0) # Try to divide by zero
        else:
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
    