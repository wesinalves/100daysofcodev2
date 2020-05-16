'''
Jornada Python - Capítulo 6
Special Attribute in class Equalizer.
'''

class Equalizer:
    '''Class to equalize a guitar'''

    def __init__(self):
        self.treble = 0
        self.bass = 0
        self.middle = 0
        self.volume = 0
    def increase(self, feature, value):
        '''inscreasing control'''
        self.__dict__[feature] += value
        if self.__dict__[feature] > 100:
            self.__dict__[feature] = 100
    def decrease(self, feature, value):
        '''decreasing control'''
        self.__dict__[feature] -= value
        if self.__dict__[feature] < 0:
            self.__dict__[feature] = 0
    def flat(self):
        '''Make it flat'''
        self.treble = 50
        self.bass = 50
        self.middle = 50
        self.volume = 50
