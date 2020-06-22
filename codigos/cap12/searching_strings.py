'''
How to program in Python - Chapter 12
Searching string.
'''


def main():
    '''Main Function'''
    string1 = "Test1, test2, test3, test4, Test5, test6"

    print('"test" occurs %d times in \n\t%s' %
          (string1.count("test"), string1))
    print('"test" occurs %d times in \n\t%s' %
          (string1.count("test", 18, len(string1)), string1))
    print("")

    # finding a substring in a string
    string2 = "Odd or even"

    print('"%s" contains "or" starting at index %d' %
          (string2, string2.find("or")))

    # find index of "even"
    try:
        print('"even" index is', string2.index("even"))
    except ValueError:
        print('"even" does not occur in "%s"' % string2)

    if string2.startswith("odd"):
        print('"%s" starts with "Odd"' % string2)

    if string2.endswith("even"):
        print('"%s" ends with "Even"' % string2)

    # searching from end of string
    print('Index from end of "test" in "%s" is %d'
          % (string1, string1.rfind("test")))

    # find rindex of "Test"
    try:
        print('First occurrence of "Test" from end at index',
              string1.rindex("Test"))
    except ValueError:
        print('"Test" does not occur in "%s"' % string1)

    print("")

    # replacing a substring

    string3 = "One, one, one, one, one, one"

    print("Original: ", string3)
    print('Replaced: "one" with "two":', string3.replace("one", "two"))
    print("Replaced 3 maximum: ", string3.replace("one", "two", 3))


main()
