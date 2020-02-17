# Journey Python - Chapter 35
# Heap sort implementation.

# initialization
GOAL_SCORES = [16, 15, 7, 6, 8, 10, 9, 12, 13, 11]

# processing
def max_heapfy(elements, length, index):
    """Create a max binary tree"""
    current_parent = index
    child_left = index * 2 + 1
    child_right = index * 2 + 2

    # check if child_left value is lower than current_parent value
    if child_left < length and elements[child_left] > elements[current_parent]:
        current_parent = child_left
    # check if child_rigth value is lower than current_parent value
    if child_right < length and elements[child_right] > elements[current_parent]:
        current_parent = child_right
    # check if current_parent was changed to swap values
    if current_parent != index:
        elements[index], elements[current_parent] = elements[current_parent], elements[index]
        max_heapfy(elements, length, current_parent)
def build_max_heap(elements):
    """Sort an element list in ascending order"""
    length = len(elements)
    # build a max heap
    for i in range(length//2, 0, -1):
        max_heapfy(elements, length, i)
    # print sorted elements
    for i in range(length - 1, 0, -1):
        print(elements)
        elements[i], elements[0] = elements[0], elements[i]
        max_heapfy(elements, i, 0)


# termination
print(GOAL_SCORES)
build_max_heap(GOAL_SCORES)
