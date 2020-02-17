# Journey Python - Chapter 35
# Heap sort implementation.

# initialization
GOAL_SCORES = [16, 15, 7, 6, 8, 10, 9, 12, 13, 11]

# processing
def max_heapfy(vector, n, i):
    """Create max binary tree"""
    current_parent = i
    child_left = 2 * i + 1
    child_right = 2 * i + 2

    ## see if the left child exists and if is grater than current parent
    if child_left < n and vector[child_left] > vector[current_parent]:
        current_parent = child_left
    ## see if the right child exists and if is grater than current parent
    if child_right < n and vector[child_right] > vector[current_parent]:
        current_parent = child_right
    # change root if needed
    if current_parent != i:
        # current parent is now a index of one of his children
        vector[i], vector[current_parent] = vector[current_parent], vector[i]
        max_heapfy(vector, n, current_parent)           
def heap_sort(vector):
    """Sort array in ascending order"""

    n = len(vector)

    # build a max heap
    for i in range(n//2, 0, -1):
        max_heapfy(vector, n, i)
    # sort elements
    for i in range(n-1, 0, -1):
        print(vector)
        vector[i], vector[0] = vector[0], vector[i]
        max_heapfy(vector, i, 0)


# termination

print(GOAL_SCORES)
heap_sort(GOAL_SCORES)
#print(GOAL_SCORES)