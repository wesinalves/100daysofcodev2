# Python Journey - Chapter 16
# Simple web browser example

from tkinter import *
import Pmw
from urllib.request import urlopen
from urllib.parse import urlparse

class WebBrowser(Frame):
    "A simple web browser"

    def __init__(self):
        
        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand = YES, fill = BOTH)
        self.master.title("A simple web browser")
        self.master.geometry("600x400")

        self.address = Entry(self)
        self.address.pack(fill = X, padx = 5, pady = 5)
        self.address.bind("<Return>", self.get_page)

        self.contents = Pmw.ScrolledText(self, text_state = DISABLED)
        self.contents.pack(expand = YES, fill = BOTH, padx = 5, pady = 5)
    
    def get_page(self, event):
        "Parse the URL, add addressing scheme and retrieve file"

        "parse the url"
        my_url = event.widget.get()
        components = urlparse(my_url)
        self.contents.text_state = NORMAL

        # if addressing scheme not specified, use http
        if components[0] == "":
            my_url = "http://" + my_url

        # connect and retrieve the file
        try:
            temp_file = urlopen(my_url)
            self.contents.settext(temp_file.read())
        except IOError as error:
            self.contents.settext("Error finding file")
            print(error)
        
        self.contents.text_state = DISABLED

def main():
    WebBrowser().mainloop()

if __name__ ==  "__main__":
    main()


