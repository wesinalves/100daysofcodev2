'''
How to program in Python - Chapter 5
Unpacking sequences.
'''

def unpacking():
    '''Unpacking example'''
    # create sequences
    my_string = "abc"
    my_list = [1, 2, 3]
    my_tuple = "a", "A", 1

    # unpack sequences to variables
    print("Unpacking string...")
    first, second, third = my_string
    print("String values:", first, second, third)

    print("\nUnpacking list...")
    first, second, third = my_list
    print("List values:", first, second, third)

    print("\nUnpacking tuple...")
    first, second, third = my_tuple
    print("Tuple values:", first, second, third)

    # swapping two values
    number_x = 3
    number_y = 4

    print("\nBefore swapping: number_x = %d, number_y = %d" % (number_x, number_y))
    number_x, number_y = number_y, number_x  # swap variables
    print("After swapping: number_x = %d, number_y = %d" % (number_x, number_y))

unpacking()
