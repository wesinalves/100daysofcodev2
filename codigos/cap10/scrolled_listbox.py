# Python Journey- Chapter 3
# ScrolledListBox used to select image.

from tkinter import *
import Pmw

class ImageSelection(Frame):
    """List of available images and an area to display them"""

    def __init__( self, images ):
        """Create list of PhotoImages and Label to display them"""

        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Select an image")
        

        self.photos = []

        # add PhotoImage objects to list photos
        for item in images:
            self.photos.append(PhotoImage(file = item))

        # create scrolled list box with vertical scrollbar
        self.listBox = Pmw.ScrolledListBox(self, items = images,
                    listbox_height = 3, vscrollmode = "static",
                    selectioncommand = self.switchImage)
        self.listBox.pack(side = LEFT, expand = YES, fill = BOTH, padx = 5, pady = 5)

        self.display = Label(self, image = self.photos[0])
        self.display.pack(padx = 5, pady = 5)
    
    def switchImage(self):
        """Change image in Label to current selection"""

        # get tuple containing index of selected list item
        chosenPicture = self.listBox.curselection()

        # configure label to display selected image
        if chosenPicture:
            choice = int(chosenPicture[0])
            self.display.config(image = self.photos[choice])

def main():
    images = ["seya.png", "yoga.png","shiryu.png", "shun.png", "ikki.png"]
    ImageSelection(images).mainloop()

if __name__ == "__main__":
    main()