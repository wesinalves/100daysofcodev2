'''
How to program in Python - Chapter 3
Class average problem with counter-controlled repetition.
'''

# initialization
TOTAL = 0
GRADE_COUNTER = 0

GRADE = input("Enter grade: ")
GRADE = int(GRADE)

# processing
while GRADE != -1:
    TOTAL = TOTAL + GRADE
    GRADE_COUNTER = GRADE_COUNTER + 1
    GRADE = input("Enter grade: ")
    GRADE = int(GRADE)

# termination
if GRADE_COUNTER > 0:
    AVAREGE = float(TOTAL) / GRADE_COUNTER
    print("Class avarege is :", AVAREGE)
else:
    print("No grades were entered!")
