# Recursive Function to find
# sum of a list
def Sum(L, i, n, count):
    
    # Base case
    if n <= i:
        return count
    
    count += L[i]
    
    # Going into the recursion
    count = Sum(L, i + 1, n, count)
    
    return count
    
# Driver's code
L = [1, 2, 3, 4, 5]
count = 0
n = len(L)
print(Sum(L, 0, n, count))