# Python program to demonstrate
# higher order functions

def generate_ints(N):
   for i in range(N):
       yield i

gen = generate_ints(3)
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))