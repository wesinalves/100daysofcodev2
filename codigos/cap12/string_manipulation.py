# Journey Python - Chapter 12
# Regular-expression string manipulation.

import re

def main():
    '''Main Function'''
    test_string1 = "This sentence ends in 5 stars *****"
    test_string2 = "1,2,3,4,5,6,7"
    test_string3 = "1+2x*3-y"
    format_string = "%-34s: %s"

    print(format_string % ("Original String", test_string1))

    # regular expression substitution
    test_string1 = re.sub(r"\*", r"^", test_string1)
    print(format_string % ("^ substituted for *", test_string1))

    test_string1 = re.sub(r"stars", "carets", test_string1)
    print(format_string % ("'carets' substituted for 'stars'", test_string1))

    print(format_string % ("every word replaced by 'word'", re.sub(r"\w+", "word", test_string1)))

    print(format_string % ("replace first 3 digits by 'digit'", re.sub(r"\d", "digit", test_string2, 3)))

    # regular expression splitting
    print(format_string % ("splitting " + test_string2, re.split(r",", test_string2)))

    print(format_string % ("splitting " + test_string3, re.split(r"[+\-*/%]", test_string3)))

main()

