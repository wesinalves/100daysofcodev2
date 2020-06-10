'''
How to program in Python - Chapter 8
# Check button demonstration.
'''
from tkinter import *


class CheckFont(Frame):
    """An area of text with Checkbutton controlled font"""

    def __init__(self):
        """Create an Entry and two Checkbuttons"""

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Checkbutton Demo")

        self.frame1 = Frame(self)
        self.frame1.pack()

        self.text = Entry(self.frame1, width=40, font="Arial 10")
        self.text.insert(INSERT, "Watch the font style change")
        self.text.pack(padx=5, pady=5)

        self.frame2 = Frame(self)
        self.frame2.pack()

        # create boolean variable
        self.bold_on = BooleanVar()

        # create "Bold" checkbutton
        self.check_bold = Checkbutton(self.frame2, text="Bold",
                                      variable=self.bold_on, command=self.change_font)
        self.check_bold.pack(side=LEFT, padx=5, pady=5)

        # create boolean variable
        self.italic_on = BooleanVar()

        # create "Italic" checkbutton
        self.check_italic = Checkbutton(self.frame2, text="Italic",
                                        variable=self.italic_on, command=self.change_font)
        self.check_italic.pack(side=LEFT, padx=5, pady=5)

    def change_font(self):
        """Change the font based on selected Checkbuttons"""

        desired_font = "Arial 10"

        if self.bold_on.get():
            desired_font += " bold"

        if self.italic_on.get():
            desired_font += " italic"

        self.text.config(font=desired_font)


def main():
    """Main function"""
    CheckFont().mainloop()


if __name__ == "__main__":
    main()
