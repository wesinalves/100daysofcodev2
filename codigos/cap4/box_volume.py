'''
How to program in Python - Chapter 4
Default arguments example.
'''

def box_volume(length=1, width=1, height=1):
    '''Calculating box volume'''
    return length * width * height


print(box_volume())
print(box_volume(10))
print(box_volume(10, 5))
print(box_volume(10, 5, 2))
