'''
How to program in Python - Chapter 10
# Popup menu demonstration.
'''

from tkinter import *
import Pmw
import sys


class PopupMenuDemo(Frame):
    """Demonstrate popup menus"""

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Popup menu demonstration")
        self.master.geometry("300x200")

        # create and pack a frame with initial white background
        self.frame1 = Frame(self, bg='white')
        self.frame1.pack(expand=YES, fill=BOTH)

        # create a menu without packing it
        self.menu = Menu(self.frame1, tearoff=0)

        colors = ['White', 'Blue', 'Yellow', 'Red']
        self.selected_color = StringVar()
        self.selected_color.set(colors[0])

        for item in colors:
            self.menu.add_radiobutton(label=item, variable=self.selected_color,
                                      command=self.change_background)

        self.frame1.bind("<Button-3>", self.popup_menu)

    def popup_menu(self, event):
        """Add the Menu to the Frame"""

        self.menu.post(event.x_root, event.y_root)

    def change_background(self):
        """Change the Frame background color"""

        self.frame1.config(bg=self.selected_color.get())


def main():
    '''Main function'''
    PopupMenuDemo().mainloop()


if __name__ == "__main__":
    main()
