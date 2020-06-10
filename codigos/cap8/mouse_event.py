'''
How to program in Python - Chapter 8
Mouse events demonstration.
'''

from tkinter import *

class MouseEvent( Frame ):
    """Demonstrate binding mouse events"""

    def __init__( self ):
        """Create a Label, pack it and bind mouse events"""

        Frame.__init__( self )
        self.pack( expand = YES, fill = BOTH )
        self.master.title("Demonstrating Mouse Events")
        self.master.geometry("275x100")

        self.mouse_position = StringVar() # displays mouse position
        self.mouse_position.set("Mouse outside window")
        self.position_label = Label(self, textvariable = self.mouse_position)
        self.position_label.pack(side = BOTTOM)

        # bind mouse events to window
        self.bind("<Button-1>", self.left_click)
        self.bind("<Button-2>", self.center_click)
        self.bind("<Button-3>", self.right_click)
        self.bind("<ButtonRelease-1>", self.button_released)
        self.bind("<Enter>", self.entered_window)
        self.bind("<Leave>", self.exited_window)
        self.bind("<B1-Motion>", self.mouse_dragged)
    
    def button_released(self, event): 
        '''button released callback'''
        self.show_position(event.x, event.y, "Released")
    
    def entered_window(self, event):
        '''entered window callback'''
        self.mouse_position.set("Mouse in window")
    
    def exited_window(self, event):
        '''exited window callback'''
        self.mouse_position.set("Mouse outside window")
    
    def mouse_dragged(self, event):
        '''mouse dragged callback'''
        self.show_position(event.x, event.y, "dragged")
    
    def left_click(self, event):
        '''left click callback'''
        self.show_position(event.x, event.y, "Pressed")
        self.master.title("Pressed with left mouse button")

    def center_click( self, event ):
        '''center click callback'''
        self.show_position(event.x, event.y, "clicked")
        self.master.title("clicked with center mouse button")

    def right_click(self, event):
        '''right click callback'''
        self.show_position(event.x, event.y, "Clicked")
        self.master.title("Clicked with right mouse button")
    
    def show_position(self, x, y, action):
        '''show position callback'''
        self.mouse_position.set(action + " at [ " + str( x ) +
                                ", " + str( y ) + " ]")

def main():
    '''Main function'''
    MouseEvent().mainloop()

if __name__ == "__main__":
    main()
