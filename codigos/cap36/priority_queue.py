"""
A Python Journey - Chapter 36
Priority Queue implementation
"""
import heap_sort as hp

def heap_maximum(elements):
    """Return the max item of the heap"""
    return elements[0]

def heap_extract_max(elements, length):
    """Method to extract max element"""
    if length < 0:
        raise BaseException("heap under flow") 
    max = elements[0]
    elements[0] = elements[length]
    length = length - 1
    hp.max_heapfy(elements, length, 0)
    return max

def heap_increase_key(elements, index, key):
    """Method to increase value of key"""
    if key < elements[index]:
        raise BaseException("new key is lower than current key")
    elements[index] = key
    while index > 0 and elements[len(elements)//2] < elements[index]:
        elements[index], elements[len(elements)//2] = elements[len(elements)//2], elements[index]
        index = len(elements)//2
