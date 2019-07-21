# Jornada Python - Capítulo 6
# String class.

class String:
    """Simulate a string of guitar"""

    def __init__(self):
        self.name = "A"
        self.frequency = 440
    
    def set_name(self, name):
        self.name = name

    def set_frequency(self, value):
        self.frequency = value