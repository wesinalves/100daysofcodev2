'''
How to program in Python
Understand try/except block.
'''

# try:
#     val = int(input("Please enter a small positive integer: "))
#     print('You entered', val)
# except:
#     print('Input not accepted')
val = input("Please enter a small positive integer: ")

if val.isdigit():
    print('You entered', int(val))