# Jornada Python - Capítulo 3
# Analysis of examination results

# initialize variables
passes = 0
failures = 0
student_counter = 0

# processing phase
while student_counter < 10:
    result = input("Enter result (1=pass,2=fail):")
    result = int(result)

    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1
    
    student_counter = student_counter + 1

# termination phase
print("Passed", passes)
print("Failures", failures)

if passes > 8:
    print("Raise Tuition")
