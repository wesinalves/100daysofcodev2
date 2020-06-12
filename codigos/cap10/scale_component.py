'''
How to program in Journey - Chapter 10
Scale component demonstration.
'''

from tkinter import *


class ScaleDemo(Frame):
    """Create Canvas with a circle controlled by a Scale"""

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Scale demo program")
        self.master.geometry("220x270")

        # create Scale
        self.control = Scale(self, from_=0, to=200, orient=HORIZONTAL,
                             command=self.update_circle)
        self.control.pack(side=BOTTOM, fill=X)
        self.control.set(10)

        # create Canvas and draw circle
        self.display = Canvas(self, bg="white")
        self.display.pack(expand=YES, fill=BOTH)

    def update_circle(self, scale_value):
        """Delete the circle, determine new size, draw again"""

        end = int(scale_value) + 10
        self.display.delete("circle")
        self.display.create_oval(10, 20, end, end, fill="red", tags="circle")


def main():
    '''Main function'''
    ScaleDemo().mainloop()


if __name__ == "__main__":
    main()
