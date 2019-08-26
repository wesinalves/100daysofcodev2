# Python Journey - Chapter 12
# Token splitting and delimiter joining.

# splitting strings
string1 = "A, B, C, D, E, F"

print("String is: ", string1)
print("Split string by spaces: ", string1.split())
print("Split string by commas: ", string1.split(','))
print("Split string by commas: ", string1.split(',', 2))
print()

# joining strings

list1 = string1.split(',')
pattern = "___"

print("List is: ", list1)
print("joining list with '{}': {}".format(pattern, pattern.join(list1)))
print("Joining list with '--.--': {}".format("--.--".join(list1)))

