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
        self.buttons.add("Clear", command = self.clear_contents)
        self.buttons.add("Help", command = self.help, width = 14)
        self.buttons.alignbuttons()

        # list of fields in an address record
        fields = ["film_id", "title", "description", "release_year", 
                    "lenguage_id", "rental_duration", "rental_rate", "length",
                    "replacement_cost", "rating", "last_updated", "special_features", "full_text"]
        
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
        
    def add_film(self):
        """Add film record to database"""

        if self.entries["title"].get() != " " and self.entries["description"].get() != " ":
            # create INSERT query command
            query = """INSERT INTO film (title, description, release_year, 
                    lenguage_id, rental_duration, rental_rate, length,
                    replacement_cost, rating, last_updated, special_features, full_text)
                    VALUES (""" + "'%s', " * 12 % \
                    (
                        self.entries["title"].get(),
                        self.entries["description"].get(),
                        self.entries["release_year"].get(),
                        self.entries["lenguage_id"].get(),
                        self.entries["rental_duration"].get(),
                        self.entries["rental_rate"].get(),
                        self.entries["length"].get(),
                        self.entries["replacement_cost"].get(),
                        self.entries["rating"].get(),
                        self.entries["last_updated"].get(),
                        self.entries["especial_features"].get(),
                        self.entries["full_text"].get()
                    )
            query = query[:-2] + ")" 

            # open connection, retrieve cursor and execute query
            try:
                conn = psycopg2.connect("dbname=dvdrental user=postgres password=root")
                cursor = conn.cursor()
                cursor.execute(query)
            except psycopg2.OperationalError as error:
                error_message = "Error %d: \n%s" % (error[0], error[1])
                showerror("Error", error_message)
            else:
                cursor.close()
                conn.close()
                self.clear_contents()
        else:
            showwarning("Missing fields", "Please enter name")
        
    def find_film(self):
        """Query database for address record and display results"""

        if self.entries["title"].get() != " ":
            # create SELECT query
            query = "SELECT * FROM film " + \
                    "WHERE title = '" + \
                    self.entries["title"].get() + "'"
            
            # open connection, retrieve cursor and execute query
            try:
                conn = psycopg2.connect("dbname=dvdrental user=postgres password=root")
                cursor = conn.cursor()
                cursor.execute(query)
            except psycopg2.OperationalError as error:
                error_message = "Error %d: \n%s" % (error[0], error[1])
                showerror("Error", error_message)
                self.clear_contents()
            else:
                results = cursor.fetchall()
                fields = cursor.description

                if not results:
                    showinfo("not found", "nonexisting records")
                else:
                    self.clear_contents()

                    #display results
                    for i in range(len(fields)):
                        if fields[i][0] == 'film_id':
                            self.IDEntry.set(str(results[0][i]))
                        else:
                            self.entries[fields[i][0]].insert(INSERT, str(results[0][i]))
                
                cursor.close()
                conn.close()
        
        else:
            showwarning( "Missing fields", "Please enter last name" )
    
    def update_film(self):
        """Update address record in database"""

        if self.entries["film_id"].get():

            # create UPDATE query command
            entry_items = self.entries.items()
            query = "UPDATE film SET"

            for key, value in entry_items:

                if key != "film_id":
                    query += " %s='%s'," % (key, value.get())
                else:
                    query = query[:-1] + "WHERE film_id = " + self.IDEntry.get()
            

            # open connection, retrieve cursor and execute query
            try:
                conn = psycopg2.connect("dbname=dvdrental user=postgres password=root")
                cursor = conn.cursor()
                cursor.execute(query)
            except psycopg2.OperationalError as error:
                error_message = "Error %d: \n%s" % (error[0], error[1])
                showerror("Error", error_message)
                self.clear_contents()
            else:
                showinfo( "database updated", "Database Updated." )
                cursor.close()
                conn.close()
            
        else:
            showwarning("No ID specified", """
                You may only update an existing record.
                Use Find to locate the record,
                then modify the information and press Update.""")
    
    def clear_contents(self):
        """Clear GUI panel"""

        for entry in self.entries.values:
            entry.delete(0,END)
        
        self.IDEntry.set(" ")
    
    def help(self):
        "Display help message to user"

        showinfo("Help", """Click Find to locate a record.
            Click Add to insert a new record.
            Click Update to update the information in a record.
            Click Clear to empty the Entry fields.\n""")

def main():
    Film().mainloop()

if __name__ == "__main__":
    main()



            
                
            