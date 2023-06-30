"""
# Journey Python - Chapter 40
# Reading files.
"""

file = open('myfile.txt', 'r')

for line in file:
    print(line, end='')

file.close()