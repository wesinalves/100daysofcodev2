'''
How to program in Python - Chapter 3
Using the continue statement.
'''

for x in range(1, 11):
    if x > 5:
        continue
    print(x, end=' ')

print("\nUsed continue to skip print values grater than 5")
