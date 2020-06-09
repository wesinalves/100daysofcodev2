# Jornada Python - Capítulo 9
# Pack layout demonstration.

from tkinter import *

class PackDemo( Frame ):
    """Demonstrate some options of Pack"""

    def __init__( self ):
        """Create four Buttons with different pack options"""

        Frame.__init__( self )
        self.master.title( "Packing Demo" )
        self.master.geometry( "400x150" )
        self.pack( expand = YES, fill = BOTH )

        self.button1 = Button( self, text = "Add Button",
                command = self.addButton )
        
        # Button component placed against top of window
        self.button1.pack( side = TOP )
        self.button2 = Button( self, text = "expand = NO, fill = BOTH" )

        # Button component placed against bottom of window
        # fills all available vertical and horizontal space

        self.button2.pack( side = BOTTOM, fill = BOTH )
        
        self.button3 = Button( self, text = "expand = YES, fill = X" )

        # Button component placed against left side of window
        # fills all available horizontal space
        self.button3.pack( side = LEFT, expand = YES, fill = X )


        self.button4 = Button( self, text = "expand = YES, fill = Y" )

        # Button component placed against right side of window
        # fills all available vertical space
        self.button4.pack( side = RIGHT, expand = YES, fill = Y )

    def addButton( self ):
        """Create and pack a new Button"""
        Button( self, text = "New Button" ).pack( pady = 5 )

def main():
    PackDemo().mainloop()

if __name__ == "__main__":
    main()

