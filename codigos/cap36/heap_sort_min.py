"""
A Python Journey - Chapter 36
Heap Sort min heapfy implementation
"""

# initialization
GOAL_SCORES = [16, 15, 7, 6, 8, 10, 9, 12, 13, 11]

# processing
def min_heapfy(elements, index):
    """Build min binary tree"""
    length = len(elements)
    current_parent = index
    child_left = index * 2 + 1
    child_right = index * 2 + 2

    if child_left < length and elements[child_left] < elements[current_parent]:
        current_parent = child_left
    if child_right < length and elements[child_right] < elements[current_parent]:
        current_parent = child_right
    if current_parent != index:
        elements[index], elements[current_parent] = elements[current_parent], elements[index]
        min_heapfy(elements, current_parent)

def build_min_heap(elements):
    """Build heap"""
    length = len(elements)

    for i in range(length//2, 0, -1):
        min_heapfy(elements, i)

def heap_sort(elements):
    """Sort array in ascending mode"""
    length = len(elements)
    build_min_heap(elements)
    for i in range(length-1, 0, -1):
        elements[i], elements[0] = elements[0], elements[i]
        min_heapfy(elements, length)
        print(elements)

#termination
print(GOAL_SCORES)
heap_sort(GOAL_SCORES)
