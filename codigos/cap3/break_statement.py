# Jornada Python - Capítulo 3
# Using the break statement to avoid repeating code in Class average problem.

#initialization
total = 0
grade_counter = 0


#processing
while 1:
    grade = input("Enter grade, -1 to exit: ")
    grade = int(grade)

    if grade == -1:
        break

    total += grade
    grade_counter += 1
    


#termination
if grade_counter > 0:
    average = float(total) / grade_counter
    print("Class average is :", average)
else:
    print("No grades were entered!")

