# Journey Python - Chapter 5
# Quick sort implementation.

# initialization
goal_scores = [16, 15, 7, 6, 8, 10, 9, 12, 13, 11]

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


def quick_sort(vector, start, end):
    if start < end:
        index = partition(vector, start, end)
        quick_sort(vector, start, index - 1)
        quick_sort(vector, index + 1, end)
        print(vector)
    


# termination
print(goal_scores)
quick_sort(goal_scores,0,len(goal_scores)-1)
#print(goal_scores)