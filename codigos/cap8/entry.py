'''
How to program in Python - Chapter 8
Entry components and event binding demonstration.
'''

from tkinter import *
from tkinter.messagebox import *


class EntryDemo(Frame):
    """Demonstrate Entrys and Event binding"""

    def __init__(self):
        """Create, pack and bind events to four Entrys"""

        Frame.__init__(self)
        self.pack(expand="yes", fill="both")
        self.master.title("Testing entry component")
        self.master.geometry("350x100")  # width x length

        self.frame1 = Frame(self)
        self.frame1.pack(pady=5)

        self.text1 = Entry(self.frame1, name="text1")

        # bind the Entry component to event
        self.text1.bind("<Return>", self.showContents)
        self.text1.pack(side="left", padx=5)

        self.text2 = Entry(self.frame1, name="text2")
        self.text2.insert(INSERT, "Enter text here")
        self.text2.bind("<Return>", self.showContents)
        self.text2.pack(side="left", padx=5)

        self.frame2 = Frame(self)
        self.frame2.pack(pady=5)

        self.text3 = Entry(self.frame2, name="text3")
        self.text3.insert(INSERT, "Uneditable text field")

        # prohibit user from altering text in Entry component text3
        self.text3.config(state=DISABLED)
        self.text3.bind("<Return>", self.showContents)
        self.text3.pack(side=LEFT, padx=5)

        # text in Entry component text4 appears as *
        self.text4 = Entry(self.frame2, name="text4", show="*")
        self.text4.insert(INSERT, "Hidden text")
        self.text4.bind("<Return>", self.showContents)
        self.text4.pack(side=LEFT, padx=5)
    def showContents(self, event):
        """Display the contents of the Entry"""

        # acquire name of Entry component that generated event
        theName = event.widget.winfo_name()

        # acquire contents of Entry component that generated event
        theContents = event.widget.get()
        showinfo("Message", theName + ": " + theContents)


def main():
    '''Main function'''
    EntryDemo().mainloop()


if __name__ == "__main__":
    main()
