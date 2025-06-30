# Python program to demonstrate 
# immutable data types
L = [1, 2, 3]
it = iter(L)

print(type(L))
print(type(it))

print(it.__next__())  # same as next(it)

print(next(it))

print(next(it))

print(next(it))