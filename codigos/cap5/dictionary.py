'''
How to program in Python - Chapter 5
Creating, accessing and modifying a dictionary.
'''


def main():
    '''Dictionary example'''
    # create and print an empty dictionary
    empty_dictionary = {}
    print("The value of empty_dictionary is:", empty_dictionary)

    # create and print a dictionary with initial values
    grades = {"João": 87, "Paulo": 76, "Laura": 92, "Maria": 89}
    print("\nAll grades:", grades)

    # access and modify an existing dictionary
    print("\nPaulo's current grade:", grades["Paulo"])
    grades["Paulo"] = 90
    print("Paulo's new grade:", grades["Paulo"])

    # add to an existing dictionary
    grades["Antonio"] = 93
    print("\nDictionary grades after modification:")
    print(grades)

    # delete entry from dictionary
    del grades["João"]
    print("\nDictionary grades after deletion:")
    print(grades)
    excluded = grades.popitem()
    print('\nexcluded item: {} from dict: {}'.format(excluded, grades))

main()
