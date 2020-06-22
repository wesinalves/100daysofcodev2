'''
How to program in Python - Chapter 12
Repetition patterns, matching vs searching
'''
import re

def main():
    '''Main Function'''
    test_strings = ["Heo", "Helo", "Hellllo"]
    expressions = ["Hel?o", "Hel+o", "Hel*o"]

    # match every expression with every string
    for string in test_strings:
        for expression in expressions:
            if re.match(expression, string):
                print(expression, "matches", string)
            else:
                print(expression, "doesn't match", string)
        print()

    # demonstrate the difference between matching and searching
    expression1 = "elo"
    expression2 = "^elo"
    expression3 = "elo$"

    # match expression1 with test_strings[1]
    if re.match(expression1, test_strings[1]):
        print(expression1, "matches", test_strings[1])

    # search expression1 with test_strings[1]
    if re.search(expression1, test_strings[1]):
        print(expression1, "found in", test_strings[1])

    # search expression2 with test_strings[1]
    if re.search(expression2, test_strings[1]):
        print(expression2, "found in", test_strings[1])

    # search expression3 with test_strings[1]
    if re.search(expression3, test_strings[1]):
        print(expression3, "found in", test_strings[1])

main()