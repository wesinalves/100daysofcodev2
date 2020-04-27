'''
How to program in Python - Chapter 3
Class average problem with sentinel repetition.
####################################################
Develop a class-averaging program that processes an arbitrary number of grades each time
the program is executed.
'''

# Determine the class average for the quiz

# Initialize variables
# Input, sum and count the quiz grades
# Calculate and print the class average

# Initialize variables
## Initialize total to zero
## Initialize counter to zero
# Input, sum and count the quiz grades
## Input the first grade (possibly the sentinel)
## While the user has not as yet entered the sentinel
##  Add this grade into the running total
##  Add one to the grade counter
##  Input the next grade (possibly the sentinel)
# Calculate and print the class average
## If the counter is not equal to zero
##  Set the average to the total divided by the counter
##  Print the average
## else
##  Print “No grades were entered”

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
