# Journey Python - Chapter 12
# Program that demonstrates grouping and greedy operations.

import re

format_string1 = "%-22s: %s" # string to format output

# string that contains fields and expression to extract fields
test_string1 = "Albert Antstein, phone: 123-4567, e-mail: albert@bug2bug.com"

expression1 = r"(\w+ \w+), phone: (\d{3}-\d{4}), e-mail: (\w+@\w+\.\w{3})"

print(format_string1 % ("Extract all user data", re.match( expression1, test_string1 ).groups()))
print(format_string1 % ("Extract all user email", re.match( expression1, test_string1 ).group(3)))

# greedy operations and grouping
format_string2 = "%-38s: %s" # string to format output

# strings and patterns to find base directory in a path
path_string = "/books/2001/python"
expression2 = "(/.+)/"

print(format_string1 % ("Greedy error", re.match( expression2, path_string ).group(1)))

expression3 = "(/.+?)/" # non-greedy operator expression
print(format_string1 % ("No error, base only", re.match( expression3, path_string ).group(1)))


