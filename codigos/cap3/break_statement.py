'''
How to program in Python - Chapter 3
Using the break statement to avoid repeating code in Class average problem.
'''

# initialization
TOTAL = 0
GRADE_COUNTER = 0

# processing
while 1:
    GRADE = input("Enter GRADE, -1 to exit: ")
    GRADE = int(GRADE)

    if GRADE == -1:
        break

    TOTAL += GRADE
    GRADE_COUNTER += 1


# termination
if GRADE_COUNTER > 0:
    AVERAGE = float(TOTAL) / GRADE_COUNTER
    print("Class AVERAGE is :", AVERAGE)
else:
    print("No grades were entered!")
