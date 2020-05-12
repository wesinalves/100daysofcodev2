'''
Jornada Python - Capítulo 6
Acessing methods of class String.
'''

from string import String

def main():
    '''Main program'''
    string1 = String()
    print(string1.get_name())
    print(string1.get_frequency())
    print(string1.get_type())
    print(string1.is_tuned())

    print('Changing string')
    string1.set_name('D')
    string1.set_frequency(140)
    print(string1._name)
    print(string1._frequency)
    print(string1.is_tuned())
    print(string1.__type)
    

main()
    