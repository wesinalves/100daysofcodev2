'''
How to program in Python - Chapter 4
Finding the maximum of three integers
using keyboard entry
'''

def maximum_value(x_value, y_value, z_value):
    '''Maximum value between three numbers'''
    maximum = x_value

    if y_value > maximum:
        maximum = y_value

    if z_value > maximum:
        maximum = z_value

    return maximum


A_VALUE = int(input("Enter first integer: "))
B_VALUE = int(input("Enter second integer: "))
C_VALUE = int(input("Enter third integer: "))

# function call
print("Maximum integer is:", maximum_value(A_VALUE, B_VALUE, C_VALUE))
print()  # print new line

D_VALUE = int(input("Enter first integer: "))
E_VALUE = int(input("Enter second integer: "))
F_VALUE = int(input("Enter third integer: "))

print("Maximum integer is:", maximum_value(D_VALUE, E_VALUE, F_VALUE))
print()

G_VALUE = int(input("Enter first integer: "))
H_VALUE = int(input("Enter second integer: "))
I_VALUE = int(input("Enter third integer: "))

print("Maximum integer is:", maximum_value(G_VALUE, H_VALUE, I_VALUE))
print()
