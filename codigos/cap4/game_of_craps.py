'''
How to program in Python - Chapter 4
Simulating the game of craps.
'''

import random

def roll_dices():
    '''Roll two dices'''
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    work_sum = die1 + die2
    print('Player rolled {:d} + {:d} = {:d}'.format(die1, die2, work_sum))
    return work_sum

def craps():
    '''Playng game of craps'''
    dices_value = roll_dices()

    if dices_value == 7 or dices_value == 11:
        game_status = 'WON'
    elif dices_value == 2 or dices_value == 3 or dices_value == 12:
        game_status = 'LOST'
    else:
        game_status = 'CONTINUE'
        my_point = dices_value
        print('Point is', my_point)

    while game_status == 'CONTINUE':
        dices_value = roll_dices()

        if dices_value == my_point:
            game_status = 'WON'
        elif dices_value == 7:
            game_status = 'LOST'

    if game_status == 'WON':
        print('Player wins')
    else:
        print('Player loses')

craps()
