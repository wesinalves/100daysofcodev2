'''
How to program in Python - Chapter 6
Creating and manipulating of class Guitar.
'''

from guitar import Guitar

def main():
    '''Main program'''
    my_guitar = Guitar()
    print(my_guitar.brand, my_guitar.body)
    print(my_guitar.play("strumming", "98", "Help"))

    my_guitar.check_strings()
    my_guitar.tune_strings()
    my_guitar.check_strings()
    my_guitar.tune_strings(['D', 'A', 'D', 'G', 'A', 'd'])
    my_guitar.check_strings()

main()
