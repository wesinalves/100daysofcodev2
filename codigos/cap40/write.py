"""
# Journey Python - Chapter 40
# Writing Files.
"""
file = open('myfile.bin', 'wb')

content = file.write(b'Hello World\n')
print(content)

file.write(b'Hello World\n')
file.write(b'Hello World\n')

file.close()