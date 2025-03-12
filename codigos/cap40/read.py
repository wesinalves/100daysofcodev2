"""
# Journey Python - Chapter 40
# Reading files.
"""

file = open('/Users/wesin/Pictures/logo.png', 'r')
#file = open('myfile.bin', 'r')

for line in file:
    print(line, end='\n')

file.close()