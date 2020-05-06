'''
How to program in Python - Chapter 5
Creating, accessing and changing a list.
'''

MY_LIST = []  # create empty list

# add values to list
for number in range(1, 11):
    MY_LIST += [number]

print("The value of MY_LIST is:", MY_LIST)

# access list values by iteration
print("\nAccessing values by iteration:")

for item in MY_LIST:
    print(item, end="\t")

print()

# access list values by index
print("\nAccessing values by index:")
print("Subscript Value")

for index, value in enumerate(MY_LIST):
    print("%9d %7d" % (index, value))

# modify list
print("\nModifying a list value...")
print("Value of MY_LIST before modification:", MY_LIST)
MY_LIST[0] = -100
MY_LIST[-3] = 19
print("Value of MY_LIST after modification:", MY_LIST)
