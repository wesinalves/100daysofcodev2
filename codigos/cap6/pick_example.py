'''
How to program in Python - chapter 6
Demonstrating Class attribute access with class Pick
'''

from pick import Pick

def main():
    '''Main program'''
    print('Number of picks before inicialization', Pick.count)
    # creating three picks objects
    pick1 = Pick()
    pick2 = Pick(0.7)
    pick3 = Pick(0.4, 'blue')
    pick4 = pick1
    print('Number of picks after inicialization', Pick.count)

    # explicitly delete pick objects by removing references
    del pick1
    del pick2
    del pick3
    print('Number of picks after destruction', Pick.count)

    print(pick4.size)
    print(pick4.color)

main()
