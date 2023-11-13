# Journey Python - Chapter 37
# Quick sort implementation.
from random import shuffle

# initialization
GOAL_SCORES = list(range(10))
shuffle(GOAL_SCORES)

# processing
def partition(vector, start, end):
    pivot = vector[end]
    index = start

    for i in range(start, end):
        if vector[i] <= pivot:
            vector[index], vector[i] = vector[i], vector[index]
            index += 1
    
    vector[index], vector[end] = vector[end], vector[index]

    return index


def quick_sort(vector, start, end):
    if start < end:
        index = partition(vector, start, end)
        quick_sort(vector, start, index - 1)
        quick_sort(vector, index + 1, end)
        print(vector)
    


# termination
print(GOAL_SCORES)
quick_sort(GOAL_SCORES, 0, len(GOAL_SCORES)-1)
#print(goal_scores)