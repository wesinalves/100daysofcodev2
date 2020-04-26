'''
How to program in Python - Chapter 3
Analysis of examination results
A counter-controlled repetition example
'''

# initialize variables
PASSES = 0
FAILURES = 0
STUDENT_COUNTER = 0

# processing phase
while STUDENT_COUNTER < 10:
    RESULT = input("Enter RESULT (1=pass,2=fail):")
    RESULT = int(RESULT)

    if RESULT == 1:
        PASSES = PASSES + 1
    else:
        FAILURES = FAILURES + 1

    STUDENT_COUNTER = STUDENT_COUNTER + 1

# termination phase
print("Passed", PASSES)
print("FAILURES", FAILURES)

if PASSES > 8:
    print("Raise Tuition")
