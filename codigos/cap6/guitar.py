class Guitar:
    def __init__(self):
        self._brand = 'Taylor'
        self._body = 'solid'
        self._shape = 'grand concert'
        self._numStrings = 6
        self._model = '314ce'
        self._strings = []
        self._price = 2000

    def play(self, style, bpm, music):
        return "Let's play {} at {} bpm using {} style with {} {}".format(music, bpm, style, self._brand, self._model)
    
    def tuneStrings(self, afination=['E','A','D','G','B','e']):
        self._strings = afination
    
    def checkStrings(self):
        if len(self._strings) == 0:
            print("Guitar is not tuned!")
        else:
            print(self._strings)
    
    def equalize(self):
        pass
