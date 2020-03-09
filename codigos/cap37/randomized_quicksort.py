# Journey Python - Chapter 37
# Randomized Quick sort implementation.
from random import shuffle, randint

# initialization
GOAL_SCORES = list(range(10))
shuffle(GOAL_SCORES)

# processing
def partition(vector, start, end):
    pivot = vector[end]
    index = start

    for i in range(start, end):
        if vector[i] <= pivot:
            vector[i], vector[index] = vector[index], vector[i]
            index += 1
    
    vector[index], vector[end] = vector[end], vector[index]

    return index

def randomized_partition(vector, start, end):
    """randomized version of partition operation"""
    index = randint(start, end)
    vector[start], vector[index] = vector[index], vector[start]
    return partition(vector, start, end)

def randomized_quick_sort(vector, start, end):
    """randomized version of quick sort algorithm"""
    if start < end:
        pivot = randomized_partition(vector, start, end)
        randomized_quick_sort(vector, start, pivot - 1)
        randomized_quick_sort(vector, pivot + 1, end)
        print(vector)

# termination
print(GOAL_SCORES)
randomized_quick_sort(GOAL_SCORES,0,len(GOAL_SCORES)-1)