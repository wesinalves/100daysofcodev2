'''
How to program in Python - Chapter 5
Creating, accessing and changing a list.
'''

def create_list():
    '''Creating list'''
    my_list = []  # create empty list

    # add values to list
    for number in range(1, 11):
        my_list += [number]

    print("The value of my_list is:", my_list)

    # access list values by iteration
    print("\nAccessing values by iteration:")

    for item in my_list:
        print(item, end="\t")

    print()

    # access list values by index
    print("\nAccessing values by index:")
    print("Subscript Value")

    for index, value in enumerate(my_list):
        print("%9d %7d" % (index, value))

    # modify list
    print("\nModifying a list value...")
    print("Value of my_list before modification:", my_list)
    my_list[0] = -100
    my_list[-3] = 19
    print("Value of my_list after modification:", my_list)

create_list()
