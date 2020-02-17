# Journal of Python - Chapter 35
# Heapsort algorithm in a interative way

# initialization
RAW_ELEMENTS = input("Give the elements sapareted by comma")
ELEMENTS = [int(x) for x in RAW_ELEMENTS.split(",")]
# processing
def max_heapfy(vector, length, index):
    """Create max binary tree"""
    current_parent = index
    child_left = index * 2 + 1
    child_right = index * 2 + 2

    # see if the left child exists and his value if is grater than current parent
    if child_left < length and vector[child_left] > vector[current_parent]:
        current_parent = child_left
    # see if the right child exists and if his value is grater than current parent
    if child_right < length and vector[child_right] > vector[current_parent]:
        current_parent = child_right
    # change root if needed
    if current_parent != index:
        # current parent is now a index of one of his children
        vector[index], vector[current_parent] = vector[current_parent], vector[index]
        max_heapfy(vector, length, current_parent)
def build_max_heap(vector):
    """Sort elements in ascending order"""
    length = len(vector)

    # build max heap
    for i in range(length//2, 0, -1):
        max_heapfy(vector, length, i)
    # sort elments
    for i in range(length - 1, 0, -1):
        print(vector)
        vector[i], vector[0] = vector[0], vector[i]
        max_heapfy(vector, i, 0)

# termination
print(ELEMENTS)
build_max_heap(ELEMENTS)
