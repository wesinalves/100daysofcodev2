'''
How to program in Python - Chapter 6
Simulating equalizer using special attribute of class Equalizer.
'''
from equalizer import Equalizer

def main():
    '''Main program'''
    control = Equalizer()
    while 1:
        print('Attributes avaiable:\n')
        print(f'volume: {control.volume}\ttreble: {control.treble}\tbass: {control.bass}\tmiddle: {control.middle}')
        attribute = input('Enter attribute to change (blank to exit): ')

        if attribute == '':
            break

        while 1:
            action = int(input('Type 1 to Increase, 2 to decrease, 3 to make it flat, 4 to exit: '))
            if action == 1:
                value = int(input('Type the value: '))
                control.increase(attribute, value)
            elif action == 2:
                value = int(input('Type the value: '))
                control.decrease(attribute, value)
            elif action == 3:
                control.flat()
            elif action == 4:
                break
            else:
                print('action not avaiable')
    print('\nEqualizer after tuning:')
    print(f'volume: {control.volume}\ttreble: {control.treble}\tbass: {control.bass}\tmiddle: {control.middle}')

main()
