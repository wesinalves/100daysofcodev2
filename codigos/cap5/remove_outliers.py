'''
How to program in Python - Chapter 5
Removing outliers from data set.
'''
import random

def remove_outliers(data, num_outliers):
    '''Removing outliers'''
    data.sort()

    for _ in range(num_outliers):
        print('upper outlier removed: {:.2f}'.format(data.pop()))
    for _ in range(num_outliers):
        print('lower outlier removed: {:.2f}'.format(data.pop(0)))

def main():
    '''Generating random numbers and remove outliers'''
    dataset = [random.gauss(5.1, 2.5) for _ in range(14)]

    print('Original dataset:')
    for number in dataset:
        print('{:.2f}'.format(number), end='\t')
    print()
    remove_outliers(dataset, 2)
    print('\nOrdered dataset and without outliers')
    for number in dataset:
        print('{:.2f}'.format(number), end='\t')

main()
