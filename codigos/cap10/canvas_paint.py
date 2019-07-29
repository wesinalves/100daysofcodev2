# Python Journey - Chapter 10
# Canvas paint demonstration.

from tkinter import *

class PaintBox(Frame):
    """Demonstrate drawing on a Canvas"""
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Canvas paint program")
        self.master.geometry("300x150")
    
        self.message = Label(self, text = "Drag the mouse to draw")
        self.message.pack(side = BOTTOM)

        # create Canvas component
        self.my_canvas = Canvas(self)
        self.my_canvas.pack(expand = YES, fill = BOTH)

        # bind mouse dragging event to Canvas
        self.my_canvas.bind("<B1-Motion>", self.paint)
    
    def paint(self, event):
        """Create an oval of radius 4 around the mouse position"""

        x1, y1 = (event.x - 4), (event.y - 4)
        x2, y2 = (event.x + 4), (event.y + 4)

        self.my_canvas.create_oval(x1,y1,x2,y2, fill = "black")

def main():
    PaintBox().mainloop()

if __name__ == "__main__":
    main()