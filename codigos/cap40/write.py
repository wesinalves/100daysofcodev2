"""
# Journey Python - Chapter 40
# Writing Binary File.
"""

file = open('myfile.bin', 'wb')

content = file.write(b'\x00\x01\x02\x03\x04')
print(content)

file.write(b'\x00\x01\x02\x03\x04')
file.write(b'\x00\x01\x02\x03\x04')

file.close()