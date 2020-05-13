'''
How to program in Python - Chapter 6
Demonstrating Relationships between objects.
'''

from string import GuitarString
from pick import Pick
from composed_guitar import Guitar


def main():
    '''Main program'''
    my_pick = Pick()
    my_guitar = Guitar(my_pick)

    strings = {1: ('e', 330), 2: ('B', 247), 3: ('G', 196),
               4: ('D', 146), 5: ('A', 110), 6: ('E', 82)}
    for key, value in strings.items():
        string = GuitarString()
        string.set_number(key)
        string.set_name(value[0])
        string.set_frequency(value[1])
        my_guitar.add_strings(string)
    
    my_guitar.increase_equalizer('volume', 50)
    my_guitar.increase_equalizer('treble', 60)
    my_guitar.increase_equalizer('middle', 52)
    my_guitar.increase_equalizer('bass', 58)

    print(my_guitar.pick.size, my_guitar.pick.color)
    my_guitar.get_strings()
    print()
    my_guitar.get_equalizer()

main()
