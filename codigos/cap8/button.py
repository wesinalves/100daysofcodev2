'''
How to program in python - Chapter 8
Button demonstration.
'''
from tkinter import *
from tkinter.messagebox import *


class PlainAndFancy(Frame):
    """Create one plain and one fancy button"""

    def __init__(self):
        """Create two buttons, pack them and bind events"""

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Buttons example")

        # create button with text
        self.plain_button = Button(self, text="Plain Button",
                                   command=self.pressed_plain)
        self.plain_button.bind("<Enter>", self.rollover_enter)
        self.plain_button.bind("<Leave>", self.rollover_leave)
        self.plain_button.pack(side=LEFT, padx=5, pady=5)

        # create button with image
        self.my_image = PhotoImage(file="button.png")
        self.fancy_button = Button(
            self, image=self.my_image, command=self.pressed_fancy)
        self.fancy_button.bind("<Enter>", self.rollover_enter)
        self.fancy_button.bind("<Leave>", self.rollover_leave)
        self.fancy_button.pack(side=LEFT, padx=5, pady=5)

    def pressed_plain(self):
        '''Plain button callback'''
        showinfo("Message", "You pressed: Plain Button")

    def pressed_fancy(self):
        '''Fancy button callback'''
        showinfo("Message", "You pressed: Fancy Button")

    def rollover_enter(self, event):
        '''rollover enter callback'''
        event.widget.config(relief=GROOVE)

    def rollover_leave(self, event):
        '''rollover leave callback'''
        event.widget.config(relief=RAISED)


def main():
    '''Main function'''
    PlainAndFancy().mainloop()


if __name__ == "__main__":
    main()
