'''
How to program in Python - Chapter 5
Student poll program.
'''

def main():
    '''Count method example'''
    responses = [1, 2, 6, 4, 8, 5, 9, 7, 8, 10, \
                5, 1, 6, 3, 8, 6, 10, 3, 8, 2, 7, \
                6, 6, 5, 7, 6, 8, 6, 7, 5, 6, 6, \
                7, 5, 6, 7, 5, 6, 4, 8, 6, 8, 10]

    print("Rating Frequency")

    for i in range(1, 11):
        print("%6d %13d" % (i, responses.count(i)))

main()
