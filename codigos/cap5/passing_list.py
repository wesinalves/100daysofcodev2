'''
How to program in Python - Chapter 5
Passing list as parameter.
'''

def modify_list(some_list):
    ''''Modifying a list'''
    length = len(some_list)
    for i in range(length):
        some_list[i] *= 2


def modify_element(element):
    '''Modifying an element inside a list'''
    element *= 2

def main():
    '''main method to pass list as parameter example'''
    my_list = list(range(5))

    print("Effects of passing entire list:")
    print("The values of the original list are:")

    print(my_list)

    modify_list(my_list)

    print("\n\nThe values of the modified list are:")

    print(my_list)

    print("\n\nEffects of passing list element:")
    print("my_list[ 3 ] before modify_element:", my_list[3])
    modify_element(my_list[3])
    print("my_list[ 3 ] after modify_element:", my_list[3])

    print("\nEffects of passing slices of list:")
    print("my_list[ 2:4 ] before modify_list:", my_list[2:4])
    modify_list(my_list[2:4])
    print("my_list[ 2:4 ] after modify_list:", my_list[2:4])

main()
