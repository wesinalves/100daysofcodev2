'''
How to program in Python - Chapter 8
Label demonstration.
'''

from tkinter import *


class LabelDemo(Frame):
    """Demonstrate Labels"""

    def __init__(self):
        """Create three Labels and pack them"""

        Frame.__init__(self)  # initializes Frame object

        # frame fills all available space
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Labels")

        self.Label1 = Label(self, text="Label with text")

        # resize frame to accommodate Label
        self.Label1.pack()

        self.Label2 = Label(self, text="Labels with text and a bitmap")

        # insert Label against left side of frame
        self.Label2.pack(side=LEFT)

        # using default bitmap image as label
        self.Label3 = Label(self, bitmap="warning")
        self.Label3.pack(side=LEFT)


def main():
    '''Main Function'''
    LabelDemo().mainloop()  # starts event loop


if __name__ == "__main__":
    main()
