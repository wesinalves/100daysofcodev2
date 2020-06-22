'''
How to program in Python - Chapter 12
Compiled regular-expression and match objects
'''
import re

def main():
    '''Main Function'''
    test_string = "God is love"
    format_string = "%-35s: %s"

    # create regular expression and compiled expression
    expression = "love"
    compiled_expression = re.compile(expression)

    # print expression and compiled expression
    print(format_string % ("The expression", expression))
    print(format_string % ("The compiled expression", compiled_expression))

    # search using re.search and compiled expression's search method
    print(format_string % ("Non-compiled string", re.search(expression, test_string)))
    print(format_string % ("Compiled string", re.search(compiled_expression, test_string)))

    # print results of searching
    print(format_string % ("search SRE_Match contains", re.search(expression, test_string).group()))
    print(format_string % ("compiled search SRE_Match contains", re.search(compiled_expression, test_string).group()))

main()