'''
How to program in Python - Chapter 8
Keyboard events demonstration.
'''

from tkinter import *


class KeyDemo(Frame):
    """Demonstrate keystroke events"""

    def __init__(self):
        """Create two Labels and bind keystroke events"""

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Demonstrating Keystroke Events")
        self.master.geometry("350x100")

        self.message1 = StringVar()
        self.line1 = Label(self, textvariable=self.message1)
        self.message1.set("Type any key or shift")
        self.line1.pack()

        self.message2 = StringVar()
        self.line2 = Label(self, textvariable=self.message2)
        self.message2.set("")
        self.line2.pack()

        # binding any key
        self.master.bind("<KeyPress>", self.key_pressed)
        self.master.bind("<KeyRelease>", self.key_released)

        # binding specific key
        self.master.bind("<KeyPress-Shift_L>", self.shift_pressed)
        self.master.bind("<KeyRelease-Shift_L>", self.shift_released)

    def key_pressed(self, event):
        '''Key pressed callback'''
        self.message1.set("Key pressed: " + event.char)
        self.message2.set("This key is not left shift")

    def key_released(self, event):
        '''Key released callback'''
        self.message1.set("Key released: " + event.char)
        self.message2.set("This key is not left shift")

    def shift_pressed(self, event):
        '''shift pressed callback'''
        self.message1.set("Shift pressed")
        self.message2.set("This key is left shift")

    def shift_released(self, event):
        '''shift released callback'''
        self.message1.set("Shift released")
        self.message2.set("This key is left shift")


def main():
    '''Main function'''
    KeyDemo().mainloop()


if __name__ == "__main__":
    main()