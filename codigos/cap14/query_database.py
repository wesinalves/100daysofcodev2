# Python Journey - Chapter 14
# Connecting postgre database
# Displays results returned by a query

import psycopg2
from tkinter import *
from tkinter.messagebox import *
import Pmw

class QueryWindow(Frame):
    """Gui database query frame"""

    def __init__(self):
        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Enter Query, Click Submit to See Results.")
        self.master.geometry("512x512")

        # scrolled text pane for query string
        self.query = Pmw.ScrolledText(self, text_height = 8)
        self.query.pack(fill = X)

        # button to submit the query
        self.submit = Button(self, text = "Submit the query", 
                        command = self.submit_query)
        self.submit.pack(fill = X)

        # frame to display query results
        self.frame = Pmw.ScrolledFrame(self, hscrollmode = 'static', 
                    vscrollmode = 'static')
        self.frame.pack(expand = YES, fill = BOTH)

        self.panes = Pmw.PanedWidget(self.frame.interior(), orient = "horizontal")
        self.panes.pack(expand = YES, fill = BOTH)

    def submit_query(self):
        """Execute user-entered query agains database"""

        try:
            conn = psycopg2.connect("dbname=dvdrental user=postgres password=root")
            cursor = conn.cursor()
            cursor.execute(self.query.get())
        except psycopg2.OperationalError as error:
            error_message = "Error %d \n%s" % (error[0],error[1])
            showerror("Error", error_message)
            return
        else:
            data = cursor.fetchall()
            fields = cursor.description
            cursor.close()
            conn.close()
        
        # clear results of last query
        self.panes.destroy()
        self.panes = Pmw.PanedWidget(self.frame.interior(), orient = "horizontal")
        self.panes.pack(expand = YES, fill = BOTH)

        # create pane and label for each field
        for item in fields:
            item0 = item[0].split("_")
            item0 = "".join(item0)
            self.panes.add(item0)
            label = Label(self.panes.pane(item0), text = item[0], relief = RAISED)
            label.pack(fill = X)
        
        # enter results into panes, using labels
        for entry in data:
            for i in range(len(entry)):
                item0 = "".join(fields[i][0].split("_"))
                label = Label(self.panes.pane(item0), text = str(entry[i]),
                        anchor = W, relief = GROOVE, bg = "white")
                label.pack(fill = X)

        self.panes.setnaturalsize()
    

def main():
    QueryWindow().mainloop()

if __name__ == "__main__":
    main()




