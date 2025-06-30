# Python program to demonstrate
# lambda expression

# def adder(x, y):
#     return x + y

# def print_assign(name, value):
#     return name + '=' + str(value)

adder = lambda x, y: x+y

print_assign = lambda name, value: name + ' = ' + str(value)

print(print_assign("4 + 6", adder(4,6)))

