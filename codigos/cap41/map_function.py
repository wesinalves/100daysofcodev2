# Python program to demonstrate working 
# of map. 
  
# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
results = map(addition, numbers) 

# Does not Print the value
print(results)

# For Printing value
for result in results:
    print(result, end = " ")