# Python Journey - Chapter 12
# Program that demonstrates classes and special sequences

import re

# specifying character classes with [ ]
testStrings = ["2x+5y","7y-3z"]
expressions = [r"2x\+5y|7y-3z", 
               r"[0-9][a-zA-Z0-9_].[0-9][yz]",
               r"\d\w-\d\w"]

# match every expression with every string
for string in testStrings:
    for expression in expressions:
        if re.match(expression, string):
            print(expression, "matches", string)

# specifying character classes with special sequences
testString1 = "800-123-4567"
testString2 = "617-123-4567"
testString3 = "email: \t joe_doe@deitel.com"

expression1 = r"^\d{3}-\d{3}-\d{4}$"
expression2 = r"\w+:\s+\w+@\w+\.(com|org|net)"

# matching with character classes
if re.match(expression1, testString1):
    print(expression1, "matches", testString1)

if re.match(expression1, testString2):
    print(expression1, "matches", testString2)

if re.match(expression2, testString3):
    print(expression2, "matches", testString3)

