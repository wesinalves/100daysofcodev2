# Jornada Python - Capítulo 9
# Card shuffling and dealing program

import random
from tkinter import *

class Card:
    """Class that represents one playing card"""

    # class attributes faces and suits contain strings
    # that correspond to card face and suit values
    faces = [ "Ace", "Deuce", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King" ]
    
    suits = [ "Hearts", "Diamonds", "Clubs", "Spades" ]

    def __init__( self, face, suit ):
        self.face = face
        self.suit = suit
    
    def __str__( self ):
        return "{} of {}".format( self.face, self.suit )

class Deck( Frame ):
    """Class to represent a GUI card deck shuffler"""

def main():
    Deck().mainloop()

if __name__ == "__main__":
    main()