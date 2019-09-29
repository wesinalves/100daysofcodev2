# Python Journey - Chapter 14
# Create, read, update and delete records in database

import psycopg2
from tkinter import *
from tkinter.messagebox import *
import Pmw

class Film(Frame):
    """GUI Database Address Book Frame"""

    def __init__(self):
        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Films for rental.")

        self.buttons = Pmw.ButtonBox(self, padx = 0)
        self.buttons.grid(columns = 2)
        self.buttons.add("Find", command = self.find_film)
        self.buttons.add("Add", command = self.add_film)
        self.buttons.add("Update", command = self.update_film)
        self.buttons.add("Clear", command = self.clear_content)
        self.buttons.add("Help", command = self.help, width = 14)
        self.buttons.alignbuttons()

        # list of fields in an address record
        fields = ["film_id", "title", "description", "release_year", 
                    "lenguage_id", "rental_duration", "rental_rate", "length",
                    "replacement_cost", "rating", "last_updatd", "special_features", "full_text"]
        
        # dictionary with Entry components for values, keyed by
        # corresponding addresses table field names
        self.entries = {}
        self.IDEntry = StringVar()
        self.IDEntry.set("")

        # create entries for each field
        for i in range(len(fields)):
            label = Label(self, text = fields[i] + ":")
            label.grid(row = i + 1, column = 0)
            entry = Entry(self, name = fields[i].lower(), font = "Courier  12")
            entry.grid(row = 1, column = 1, sticky = W+E+N+S, padx = 5)
        
            # user cannot type in ID field
            if fields[i] == "film_id":
                entry.config(state = DISABLED, textvariable = self.IDEntry, bg = "gray")
            
            # add entry field to dictionary
            key = fields[i].replace(" ", " ")
            key = key.upper()
            self.entries[key] = entry
            