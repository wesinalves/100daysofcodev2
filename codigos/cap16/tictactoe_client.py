# Python Journey - Chapter 16
# Client for Tic-Tac-Toe program

import socket
import threading
from tkinter import *
import Pmw

class TicTacToeClient(Frame, threading.Thread):
    "Client that plays a game of Tic-Tac-Toe"

    def __init__(self):

        threading.Thread.__init__( self )
        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Tic-Tac-Toe Client")
        self.master.geometry("250x325")

        self.id = Label(self, anchor = W)
        self.id.grid(columnspan = 3, sticky = W+E+N+S)
        self.board = []

        # create and add all buttons to the board
        for i in range(9):
            newButton = Button(self, font = "Courier 20 bold",
                            height = 1, width = 1, relief = GROOVE,name = str( i ))
            newButton.bind("<Button-1>", self.sendClickedSquare)
            self.board.append(newButton)
        
        current = 0

        # display all buttons in 3x3 grid
        for i in range(1, 4):
            for j in range(3):
                self.board[ current ].grid(row = i, column = j,sticky = W+E+N+S)
                current += 1
        
        # area for server messages
        self.display = Pmw.ScrolledText(self, text_height = 10,
            text_width = 35, vscrollmode = "static" )
        
        self.display.grid(row = 4, columnspan = 3)

        self.start() # run thread
    
    def run(self):
        "Control thread that allows continuous update of the display"

        HOST = "127.0.0.1"
        PORT = 5000

        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((HOST, PORT))

        # first get player’s mark ( X or O )
        self.my_mark = self.connection.recv(2)
        self.id.config(text = 'You are player "%s"' % self.my_mark)

        self.my_turn = 0

        # receive messages sent to client
        while 1:
            message = self.connection.recv(34)

            if not message:
                break
            
            self.process_message(message)
        
        self.connection.close()
        self.display.insert(END, "Game over.\n")
        self.display.insert(END, "Connection closed.\n")
        self.display.insert(END)
    
    def process_message(self, message):
        "Interpret server message and perform necessary actions"

        if message == "Valid move.":
            self.display.insert(END, "Valid move, please wait.\n")
            self.display.yview(END)
            self.boad[self.current_square].config(text = self.my_mark, bg = "white")
        elif message == "Invalid move, try again.":
            self.display.insert(END, message + "\n")
            self.display.yview(END)
            self.my_turn = 1
        elif message == "Opponent moved.":
            location = int(self.connection.recv(2))

            if self.my_mark == "X":
                self.board[location].config(text = "O", bg = "gray")
            else:
                self.board[location].config(text = "X", bg = "gray")
            
            self.display.insert(END, message + " Your turn.\n")
            self.display.yview(END)
            self.my_turn = 1
        elif message == "Other player connected. Your move.":
            self.display.insert(END, message + "\n")
            self.display.yview(END)
            self.my_turn = 1
        else:
            self.display.insert(END, message + "\n")
            self.display.yview(END)
    
    def sendClickedSquare(self, event):
        "Send attempted move to server"

        if self.my_turn:
            name = event.widget.winfo_name()
            self.current_square = int(name)
            self.connection.send(name)
            self.my_turn = 0

def main():
    TicTacToeClient().mainloop()

if __name__ == "__main__":
    main()



