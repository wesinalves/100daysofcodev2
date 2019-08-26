# Python Journey - Chapter 12
# Simple regular-expression example.

import re

# list of strings to search and expressions used to search
testStrings = ["Hello World", "Hello world!", "hello world"]
expressions = ["hello", "Hello", "world!"]

# search every expression in every string
for string in testStrings:
    for expression in expressions:
        if re.search(expression, string):
            print(expression, "found in", string)
        else:
            print(expression, "not found in ", string)