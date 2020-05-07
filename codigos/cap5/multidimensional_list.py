'''
How to program in Python - Chapter 5
Multidimensional list example.
'''
from random import uniform


def print_grades(grades):
    '''Print matrix of grades'''
    students = len(grades)  # number of students
    exams = len(grades[0])  # number of exams

    # print table headers
    print("The list is: \n")
    print(" ", end='\t\t')    
    for i in range(exams):
        print("[%d]" % i, end='\t')
    print()

    # print scores, by row
    for i in range(students):
        print("grades[%d] " % i, end='\t')
        for j in range(exams):
            print("%.2f" % grades[i][j], "", end='\t')
        print()

def minimum(grades):
    '''Compute minimum grade'''
    low_score = 100

    for students in grades:  # loop over students
        for score in students:  # loop over scores
            if score < low_score:
                low_score = score
    return low_score


def maximum(grades):
    '''Compute maximum grade'''
    high_score = 0
    for students in grades:  # loop over students
        for score in students:  # loop over scores
            if score > high_score:
                high_score = score
    return high_score

def average(exams):
    '''Compute average grade'''
    total = 0.0
    for grade in exams:
        total += grade
    return total / len(exams)

def main():
    '''Main program'''

    # genarate grade matrix (4 rows x 5 column) using list comprehension
    grades = [[uniform(1, 10) for scores in range(5)] for students in range(4)]

    print_grades(grades)
    print("\n\nLowest grade: {:.2f}".format(minimum(grades)))
    print("Highest grade: {:.2f}".format(maximum(grades)))
    print("\n")

    # print average for each student
    for student, exams in enumerate(grades):
        print("Average for student {} is {:.2f}".format(student, average(exams)))

main()
