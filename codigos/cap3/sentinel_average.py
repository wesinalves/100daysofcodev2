# Jornada Python - Capítulo 3
# Class average problem with counter-controlled repetition.

#initialization
total = 0
grade_counter = 0

grade = input("Enter grade: ")
grade = int(grade)

#processing
while grade != -1:
    total = total + grade
    grade_counter = grade_counter + 1
    grade = input("Enter grade: ")
    grade = int(grade)


#termination
if grade_counter > 0:
    average = float(total) / grade_counter
    print("Class average is :", average)
else:
    print("No grades were entered!")

