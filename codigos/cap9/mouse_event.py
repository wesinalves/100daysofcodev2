# Jornada Python - Capítulo 9
# Mouse events demonstration.

from tkinter import *

class MouseEvent( Frame ):
    """Demonstrate binding mouse events"""

    def __init__( self ):
        """Create a Label, pack it and bind mouse events"""

        Frame.__init__( self )
        self.pack( expand = YES, fill = BOTH )
        self.master.title("Demonstrating Mouse Events")
        self.master.geometry("275x100")

        self.mousePosition = StringVar() # displays mouse position
        self.mousePosition.set("Mouse outside window")
        self.positionLabel = Label(self, textvariable = self.mousePosition)
        self.positionLabel.pack(side = BOTTOM)

        # bind mouse events to window
        self.bind("<Button-1>", self.leftClick)
        self.bind("<Button-2>", self.centerClick)
        self.bind("<Button-3>", self.rightClick)
        self.bind("<ButtonRelease-1>", self.buttonReleased)
        self.bind("<Enter>", self.enteredWindow)
        self.bind("<Leave>", self.exitedWindow)
        self.bind("<B1-Motion>", self.mouseDragged)
    
    def buttonReleased(self, event): 
        self.showPosition(event.x, event.y, "Released")
    
    def enteredWindow(self, event):
        self.mousePosition.set("Mouse in window")
    
    def exitedWindow(self, event):
        self.mousePosition.set("Mouse outside window")
    
    def mouseDragged(self, event):
        self.showPosition(event.x, event.y, "Dragged")
    
    def leftClick(self, event):
        self.showPosition(event.x, event.y, "Pressed")
        self.master.title("Pressed with left mouse button")

    def centerClick( self, event ):
        self.showPosition(event.x, event.y, "Clicked")
        self.master.title("Clicked with center mouse button")

    def rightClick(self, event):
        self.showPosition(event.x, event.y, "Clicked")
        self.master.title("Clicked with right mouse button")
    
    def showPosition(self, x, y, action):
        self.mousePosition.set(action + " at [ " + str( x ) +
                                ", " + str( y ) + " ]")

def main():
    MouseEvent().mainloop()

if __name__ == "__main__":
    main()
