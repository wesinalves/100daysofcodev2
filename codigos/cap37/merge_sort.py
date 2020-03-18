'''
# Journey Python - Chapter 37
# Merge sort implementation.
'''
from random import shuffle
# from math import ceil

# initialization
GOAL_SCORES = list(range(15))
shuffle(GOAL_SCORES)

# processing
def merge(elements, start, middle, end):
    '''Implement merge operation'''
    # left[start..middle] e right[middle + 1..end]
    length_left = middle - start + 1
    length_right = end - middle
    left, right = [], []
    for i in range(length_left):
        left.append(elements[start + i])
    for j in range(length_right):
        right.append(elements[middle + j + 1])
    
    left.append(float('inf'))
    right.append(float('inf'))
    
    i = 0 # index for left vector
    j = 0 # index for right vector
    for k in range(start, end + 1):
        if left[i] <= right[j]:
            elements[k] = left[i]
            i += 1
        else:
            elements[k] = right[j]
            j += 1
    
    '''
    # for debug
    print(start, middle, end)
    print(i, j)
    print('left: ', left)
    print('right: ', right)
    print(elements)
    print('*' * 10)
    '''
def merge_sort(elements, start, end):
    '''Implement merge sort algorithm'''
    if start < end:
        middle = (start + end) // 2
        merge_sort(elements, start, middle)
        merge_sort(elements, middle + 1, end)
        merge(elements, start, middle, end)

# termination
print(GOAL_SCORES)
merge_sort(GOAL_SCORES, 0, len(GOAL_SCORES)-1)
print(GOAL_SCORES)
