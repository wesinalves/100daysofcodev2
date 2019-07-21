# Jornada Python - Capítulo 6
# Equalizer class.

class Equalizer:
    """create class to equalize a guitar"""

    def __init__(self):
        self.treble = 0
        self.bass = 0
        self.middle = 0
    
    def increase(self, feature, value):
        self.__dict__[feature] += value
    
    def decrease(self, feature, value):
        self.__dict__[feature] -= value
    
    def flat(self):
        self.treble = 0
        self.bass = 0
        self.middle = 0

