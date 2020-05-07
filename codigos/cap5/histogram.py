'''
How to program in Python - Chapter 5
Creating a histogram from a list of values.
'''

def main():
    '''Creating a histogram'''
    values = []  # a list of values

    print("Enter 10 integers:")

    for i in range(10):
        new_value = int(input("Enter integer %d: " % (i + 1)))
        values.append(new_value)

    # create histogram
    print("\nCreating a histogram from values:")
    print("%s %10s %10s" % ("Element", "Value", "Histogram"))

    for index, value in enumerate(values):
        print("%7d %10d %s" % (index, value, "*" * value))

main()
