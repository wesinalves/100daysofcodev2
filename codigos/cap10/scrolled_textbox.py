# Python Journey - Chapter 10
# Copying selected text from one text area to another.

from tkinter import *
import Pmw

class CopyTextWindow(Frame):
    """Demonstrate ScrolledTexts"""

    def __init__( self ):
        """Create two ScrolledTexts and a Button"""

        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand = YES, fill = BOTH)
        self.master.title("ScrolledText Demo")

        # create scrolled text box with word wrap enabled
        self.text1 = Pmw.ScrolledText(self, text_width = 25, text_height = 12, text_wrap = WORD,
                        hscrollmode = "static", vscrollmode = "static")
        self.text1.pack(side = LEFT, expand = YES, fill = BOTH, padx = 5, pady = 5)

        self.copyButton = Button(self, text = "Copy >>>", command = self.copyText)
        self.copyButton.pack(side = LEFT, padx = 5, pady = 5)

        # create uneditable scrolled text box
        self.text2 = Pmw.ScrolledText(self, text_width = 25, text_height = 12, text_wrap = WORD,
                        hscrollmode = "static", vscrollmode = "static", text_state = DISABLED)
        self.text2.pack(side = LEFT, expand = YES, fill = BOTH, padx = 5, pady = 5)

    def copyText(self):
        """Set the text in the second ScrolledText"""

        self.text2.settext(self.text1.get(SEL_FIRST, SEL_LAST))
    
def main():
    CopyTextWindow().mainloop()

if __name__ == "__main__":
    main()


