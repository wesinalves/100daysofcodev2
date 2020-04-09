'''
COMO PROGRAMAR EM PYTHON - chapter 3
if statements used to show improper indentation
'''
print("Enter two integers, and I will tell you")
print("the relationships they satisfy.")

# read first string and convert to integer
NUMBER1 = input("Please enter first integer: ")
NUMBER1 = int(NUMBER1)

# read second string and convert to integer
NUMBER2 = input("Please enter second integer: ")
NUMBER2 = int(NUMBER2)

if NUMBER1 == NUMBER2:
    print("%d is equal to %d" % (NUMBER1, NUMBER2))

    # improper indentation
    if NUMBER1 != NUMBER2:
        print("%d is not equal to %d" % (NUMBER1, NUMBER2))

if NUMBER1 < NUMBER2:
    print("%d is less than %d" % (NUMBER1, NUMBER2))

if NUMBER1 > NUMBER2:
    print("%d is greater than %d" % (NUMBER1, NUMBER2))

if NUMBER1 <= NUMBER2:
    print("%d is less than or equal to %d" % (NUMBER1, NUMBER2))

if NUMBER1 >= NUMBER2:
    print("%d is greater than or equal to %d" % (NUMBER1, NUMBER2))
