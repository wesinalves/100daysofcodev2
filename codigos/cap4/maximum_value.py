'''
How to program in Python - Chapter 4
Finding the maximum of three integers
'''


def maximum_value(x, y, z):
    '''Maximum value between three numbers'''
    maximum = x

    if y > maximum:
        maximum = y

    if z > maximum:
        maximum = z

    return maximum


a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

# function call
print("Maximum integer is:", maximum_value(a, b, c))
print()  # print new line

d = int(input("Enter first integer: "))
e = int(input("Enter second integer: "))
f = int(input("Enter third integer: "))

print("Maximum integer is:", maximum_value(d, e, f))
print()

g = int(input("Enter first integer: "))
h = int(input("Enter second integer: "))
i = int(input("Enter third integer: "))

print("Maximum integer is:", maximum_value(g, h, i))
print()