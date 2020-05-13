'''
Jornada Python - Capítulo 6
Set and Get methods of class GuitarString.
'''

FREQUENCIES = {'E':82, 'A':110, 'D':146, 'G':196, 'B':247, 'e':330}

class GuitarString:
    '''Simulate a string of guitar'''

    def __init__(self):
        self._number = 5
        self._name = "A"
        self._frequency = 110
        self.__type = 'Nylon'
    def set_number(self, number):
        '''Set number attribute '''
        self._number = int(number)
    def set_name(self, name):
        '''Set name attribute '''
        if name in FREQUENCIES.keys():
            self._name = name
    def set_frequency(self, value):
        '''Set frequency attribute'''
        if 82 <= value < 330:
            self._frequency = value
    def get_number(self):
        '''Get number attribute'''
        return int(self._number)
    def get_name(self):
        '''Get name attribute'''
        return self._name + ' string'
    def get_frequency(self):
        '''Get freqeuncy attribute'''
        return str(self._frequency / 1000) + ' Khz' # return value in KHz
    def get_type(self):
        '''Get type attribute'''
        return self.__type
    def is_tuned(self):
        '''check if string is tunned'''
        if self._frequency == FREQUENCIES[self._name]:
            return True
        else:
            print('The right afination of string {} is {} Hz'.format(self._name, FREQUENCIES[self._name]))
            return False
