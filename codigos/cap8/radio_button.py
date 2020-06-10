'''
How to program in Python - Chapter 8
Radio Button demonstration.
'''

from tkinter import *


class RadioFont(Frame):
    """An area of text with Radiobutton controlled font"""

    def __init__(self):
        """Create an Entry and two Radiobuttons"""

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Radiobutton Demo")

        self.frame1 = Frame(self)
        self.frame1.pack()

        self.text = Entry(self.frame1, width=40, font="Arial 10")
        self.text.insert(INSERT, "Watch the font style change")
        self.text.pack(padx=5, pady=5)

        self.frame2 = Frame(self)
        self.frame2.pack()

        font_selections = ["Plain", "Bold", "Italic", "Bold/Italic"]

        self.chosen_font = StringVar()

        # initial selection
        self.chosen_font.set(font_selections[0])

        # create group of Radiobutton components with same variable
        for style in font_selections:
            abutton = Radiobutton(self.frame2, text=style,
                                  variable=self.chosen_font, value=style,
                                  command=self.change_font)
            abutton.pack(side=LEFT, padx=5, pady=5)

    def change_font(self):
        """Change the font based on selected Checkbuttons"""

        desired_font = "Arial 10"

        if self.chosen_font.get() == "Bold":
            desired_font += " bold"
        elif self.chosen_font.get() == "Italic":
            desired_font += " italic"
        elif self.chosen_font.get() == "Bold/Italic":
            desired_font += " bold italic"
        self.text.config(font=desired_font)


def main():
    '''Main function'''
    RadioFont().mainloop()


if __name__ == "__main__":
    main()
