# Jornada Python - Capítulo 3
# Class average problem with counter-controlled repetition.

#initialization
total = 0
grade_counter = 0

#processing
while grade_counter <= 10:
    grade = input("Enter grade: ")
    grade = int(grade)
    total = total + grade
    grade_counter = grade_counter + 1


#termination
average = total / 10
print("Class average is :", average)

