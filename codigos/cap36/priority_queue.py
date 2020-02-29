"""
A Python Journey - Chapter 36
Priority Queue implementation
"""
import heap_sort as hp

def parent(i):
    """get parent index of item i"""
    return i//2

def left(i):
    """get left child index of item i"""
    return i * 2 + 1

def right(i):
    """get right child index of item i"""
    return i * 2 + 2

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
    while index > 0 and elements[parent(index)] < elements[index]:
        elements[index], elements[parent(index)] = elements[parent(index)], elements[index]
        index = parent(index)

def max_heap_insert(elements, length, key):
    """Method to insert an element"""
    length += 1
    elements[length] = float('-inf')
    heap_increase_key(elements,lengh, key)

