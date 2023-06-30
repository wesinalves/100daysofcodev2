"""
# Journey Python - Chapter 40
# Writing Files.
"""

file = open('myfile.txt', 'w', encoding="utf-8")

content = file.write('Hello World\n')
print(content)

file.write('Hello World\n')
file.write('Hello World\n')

file.close()