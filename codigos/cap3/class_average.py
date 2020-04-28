'''
How to program in Python - Chapter 3
Class average problem with counter-controlled repetition.
#########################################################
A class of ten students took a quiz. The grades (integers numbers) for this quiz
are given by keyboard. Determine the class average on the quiz.
'''

#initialization
TOTAL = 0
GRADE_COUNTER = 1

#processing
while GRADE_COUNTER <= 10:
    GRADE = input("Enter GRADE: ")
    GRADE = int(GRADE)
    TOTAL = TOTAL + GRADE
    GRADE_COUNTER = GRADE_COUNTER + 1

#termination
AVERAGE = TOTAL / 10
print("Class AVERAGE is :", AVERAGE)

