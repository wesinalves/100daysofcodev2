'''
How to program in Python - Chapter 6
Simple definition of class Guitar.
'''

class Guitar:
    '''class Guitar definition'''

    def __init__(self):
        self.brand = 'Taylor'
        self.body = 'solid'
        self.shape = 'grand concert'
        self.num_strings = 6
        self.model = '314ce'
        self.strings = []
        self.price = 2000

    def play(self, style, bpm, music):
        '''Play song'''
        return "Let's play {} at {} bpm using {} style with {} {}".format(music, bpm, style,
                                                                          self.brand, self.model)

    def tune_strings(self, afination=None):
        '''Tuning strings'''
        if afination is None:
            afination = ['E', 'A', 'D', 'G', 'B', 'e']
        self.strings = afination

    def check_strings(self):
        '''Cheking strings tuning'''
        if len(self.strings) == 0:
            print("Guitar is not tuned!")
        else:
            print(self.strings)
