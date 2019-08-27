# Python Journey - Chapter 12
# Repetition patterns, matching vs searching

import re

testStrings = ["Heo", "Helo", "Hellllo"]
expressions = ["Hel?o", "Hel+o", "Hel*o"]

# match every expression with every string
for string in testStrings:
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

# match expression1 with testStrings[1]
if re.match(expression1, testStrings[1]):
    print(expression1, "matches", testStrings[1])

# search expression1 with testStrings[1]
if re.search(expression1, testStrings[1]):
    print(expression1, "found in", testStrings[1])

# search expression2 with testStrings[1]
if re.search(expression2, testStrings[1]):
    print(expression2, "found in", testStrings[1])

# search expression3 with testStrings[1]
if re.search(expression3, testStrings[1]):
    print(expression3, "found in", testStrings[1])