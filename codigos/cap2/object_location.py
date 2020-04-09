"""
# Como Programar em Python - Capítulo 2
# Sum two intergers showing metadatas.
"""
INTEGER1 = input("Enter first integer:\n")
print("INTEGER1: ", id(INTEGER1), type(INTEGER1), INTEGER1)
INTEGER1 = int(INTEGER1)
print("INTEGER1: ", id(INTEGER1), type(INTEGER1), INTEGER1)


INTEGER2 = input("Enter second integer:\n")
print("INTEGER2: ", id(INTEGER2), type(INTEGER2), INTEGER2)
INTEGER2 = int(INTEGER2)
print("INTEGER2: ", id(INTEGER2), type(INTEGER2), INTEGER2)

SUM_INTEGER = INTEGER1 + INTEGER2

print("Sum is: ", SUM_INTEGER)
print("sum: ", id(SUM_INTEGER), type(SUM_INTEGER), SUM_INTEGER)
