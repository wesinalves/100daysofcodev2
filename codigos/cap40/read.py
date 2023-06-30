"""
# Journey Python - Chapter 40
# Reading files.
"""

file = open('myfile.txt', 'rb')

for line in file:
    print(line, end='')

file.close()