'''
# Journey Python - Chapter 37
# Merge sort implementation.
'''
from random import shuffle

# initialization
GOAL_SCORES = list(range(15))
shuffle(GOAL_SCORES)

# process
def insertion_sort(elements):
    """Order elements using insertion sort algorithm"""
    length = len(elements)
    for j in range(1, length):
        key = elements[j]
        # put the key in the right position in A[1..j-1]
        i = j - 1
        while i > -1 and elements[i] > key:
            elements[i+1] = elements[i]
            i -= 1
        elements[i+1] = key
        print(elements)

# termination
print(GOAL_SCORES)
insertion_sort(GOAL_SCORES)
