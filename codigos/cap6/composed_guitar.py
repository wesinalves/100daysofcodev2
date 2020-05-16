'''
How to program in Python - Chapter 6
Composed class guitar.
'''

from string import GuitarString
from equalizer import Equalizer


class Guitar:
    '''Composed class guitar'''

    def __init__(self, pick):
        self.pick = pick # a pick object
        self._strings = list()
        self._equalizer = Equalizer()

    def add_strings(self, string):
        '''Add string to guitar'''
        if len(self._strings) < 6 and isinstance(string, GuitarString):
            self._strings.append(string)
    def get_strings(self):
        '''Retrieve strings on the guitar'''
        for string in self._strings:
            print(string.get_name() + f' ({string.get_frequency()})')

    def increase_equalizer(self, feature, value):
        '''Increase controls'''
        self._equalizer.increase(feature, value)
    def decrease_equalizer(self, feature, value):
        '''Increase controls'''
        self._equalizer.decrease(feature, value)
    def flatten_equalizer(self):
        '''Increase controls'''
        self._equalizer.flat()
    def get_equalizer(self):
        '''Return values of control in the equalizer'''
        print(f'Volume: {self._equalizer.volume}, \
            Treble: {self._equalizer.treble}, \
            Middel: {self._equalizer.middle}, \
            Bass: {self._equalizer.bass}')
