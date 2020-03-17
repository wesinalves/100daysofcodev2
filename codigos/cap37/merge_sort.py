'''
# Journey Python - Chapter 37
# Merge sort implementation.
'''
from random import shuffle
from math import ceil

# initialization
GOAL_SCORES = list(range(10))
shuffle(GOAL_SCORES)

# processing
def merge(elements, start, middle, end):
    '''Implement merge operation'''
    # left[start..middle] e right[middle + 1..end]
    left = elements[start:middle]
    right = elements[middle:end]
    left.append(float('inf'))
    right.append(float('inf'))
    i = 0 # index for left vector
    j = 0 # index for right vector
    for k in range(start, end):
        if left[i] <= right[j]:
            elements[k] = left[i]
            i += 1
        else:
            elements[k] = right[j]
            j += 1

def merge_sort(elements, start, end):
    '''Implement merge sort algorithm'''
    if start < end:
        middle = ceil((start + end) / 2)
        merge_sort(elements, start, middle)
        merge_sort(elements, middle, end)
        merge(elements, start, middle, end)

# termination
print(GOAL_SCORES)
merge_sort(GOAL_SCORES, 0, len(GOAL_SCORES))
print(GOAL_SCORES)
