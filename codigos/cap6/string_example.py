'''
How to program in Python - chapter 6
Accessing methods of class String.
'''

from string import GuitarString

def main():
    '''Main program'''
    string1 = GuitarString()
    print(string1.get_number())
    print(string1.get_name())
    print(string1.get_frequency())
    print(string1.get_type())
    print(string1.is_tuned())

    print('Changing string')
    string1.set_number(4.2)
    string1.set_name('D')
    string1.set_frequency(140)
    print(string1.is_tuned())
    print(string1._name)
    print(string1._number)
    print(string1._frequency)
    print(string1.__type)
    
main()
    