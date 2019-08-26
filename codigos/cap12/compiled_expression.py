# Python Journey - Chapter 12
# Compiled regular-expression and match objects

import re

testString = "God is love"
formatString = "%-35s: %s"

# create regular expression and compiled expression
expression = "love"
compiledExpression = re.compile(expression)

# print expression and compiled expression
print(formatString % ("The expression", expression))
print(formatString % ("The compiled expression", compiledExpression))

# search using re.search and compiled expression's search method
print(formatString % ("Non-compiled string", re.search(expression, testString)))
print(formatString % ("Compiled string", re.search(compiledExpression, testString)))

# print results of searching
print(formatString % ("search SRE_Match contains", re.search(expression, testString).group()))
print(formatString % ("compiled search SRE_Match contains", re.search(compiledExpression, testString).group()))
