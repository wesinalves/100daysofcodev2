'''
How to program in Python - Chapter 12
Program that demonstrates classes and special sequences
'''
import re

def main():
    '''Main Function'''
    # specifying character classes with [ ]
    test_strings = ["2x+5y","7y-3z"]
    expressions = [r"2x\+5y|7y-3z", 
                r"[0-9][a-zA-Z0-9_].[0-9][yz]",
                r"\d\w-\d\w"]

    # match every expression with every string
    for string in test_strings:
        for expression in expressions:
            if re.match(expression, string):
                print(expression, "matches", string)

    # specifying character classes with special sequences
    test_string1 = "800-123-4567"
    test_string2 = "617-123-4567"
    test_string3 = "email: \t joe_doe@deitel.com"

    expression1 = r"^\d{3}-\d{3}-\d{4}$"
    expression2 = r"\w+:\s+\w+@\w+\.(com|org|net)"

    # matching with character classes
    if re.match(expression1, test_string1):
        print(expression1, "matches", test_string1)

    if re.match(expression1, test_string2):
        print(expression1, "matches", test_string2)

    if re.match(expression2, test_string3):
        print(expression2, "matches", test_string3)

main()

