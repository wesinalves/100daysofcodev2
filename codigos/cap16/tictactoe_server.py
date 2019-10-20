# Python Journey - Chapter 16
# Class TicTacToeServer maintains a game of Tic-Tac-Toe
# for two clients, each managed by a Player thread.

import socket
import threading

class Player(threading.Thread):
    "Thread used to manage each Tic-Tac-Toe client individually"

    def __inint__(self, connection, server, number):
        "Initialize thread and setup variables"

        threading.Thread.__init__( self )

        if number == 0:
            self.mark = "X"
        else:
            self.mark = "O"
        
        self.connection = connection
        self.server = server
        self.number = number
    
    def other_play_moved(self, location):
        self.connection.send("Opponent moved")
        self.connection.send(str(location))

    def run(self):
        # Play the game
        
        self.connection.display("Player %s connected." % self.mark)
        self.connection.send(self.mark)
        self.connection.send("%s connected." % self.mark)

        # wait for another player to arrive
        if self.mark == "X":
            self.connection.send( "Waiting for another player..." )
            self.server.gameBeginEvent.wait()
            self.connection.send("Other player connected. Your move.")
        else:
            self.server.gameBeginEvent.wait()
            self.connection.send("Wating the first move")
        
        # play game
        while not self.server.gameOver():
            location = self.connection.recv(2)

            if not location:
                break

            if self.server.validMove(int(location), self.number):
                self.server.display("loc: " + location)
                self.connection.send("Valid move.")
            else:
                self.connection.send("Invalid move. Try again.")
        
        self.connection.close()
        self.server.display("Game Over.")
        self.server.display("Connection close.")
