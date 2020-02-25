# Journey Python - Chapter 35
# Heap sort implementation.
from random import shuffle

# initialization
#GOAL_SCORES = [16, 15, 7, 6, 8, 10, 9, 12, 13, 11]
#GOAL_SCORES = [7, 5, 8, 3, 2, 11, 20, 6, 1, 15, 16, 4]
GOAL_SCORES = list(range(1000))
shuffle(GOAL_SCORES)

# processing
def max_heapfy(elements, length, index):
    """Make sure max heap property"""
    current_parent = index
    child_left = index * 2 + 1
    child_right = index * 2 + 2
    #print(child_left, child_right, current_parent)

    # check if child_left value is lower than current_parent value
    if child_left <= length and elements[child_left] > elements[current_parent]:
        current_parent = child_left
    # check if child_rigth value is lower than current_parent value
    if child_right <= length and elements[child_right] > elements[current_parent]:
        current_parent = child_right
    # check if current_parent was changed to swap values
    if current_parent != index:
        elements[index], elements[current_parent] = elements[current_parent], elements[index]
        max_heapfy(elements, length, current_parent)
def build_max_heap(elements):
    """Build a max heap"""
    length = len(elements)
    for i in range(length//2 - 1, -1, -1):
        max_heapfy(elements, length - 1, i)
def heap_sort(elements):
    """Sort elements in ascending order"""
    length = len(elements)
    build_max_heap(elements)
    for i in range(length - 1, 0, -1):
        #print(elements)
        elements[i], elements[0] = elements[0], elements[i]
        max_heapfy(elements, i - 1, 0)


# termination
print(GOAL_SCORES)
heap_sort(GOAL_SCORES)
print(GOAL_SCORES)
