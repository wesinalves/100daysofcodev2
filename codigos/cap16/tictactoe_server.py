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

class TicTacToeServer:
    "Server that maintains a game of Tic-Tac-Toe for two clients"

    def __init__(self):

        HOST = ""
        PORT = 5000

        self.board = []
        self.current_player = 0
        self.turn_condition = threading.Condition()
        self.gameBeginEvent = threading.Event()

        for i in range(9):
            self.board.append(None)
        
        # setup server socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.display("Server awaiting connections...")
    
    def execute(self):
        "Play the game--create and start both Player threads"

        self.players = []

        for i in range(2):
            self.server.listen(1)
            connection, address = self.server.accept()
            self.players.append(Player(connection, self, i))
            self.players[-1].start()
        
    def display(self, message):
        print(message)
    
    def validMove(self, location, player):
        "Determine if a move is valid--if so, make move"

        # only one move can be made at a time
        self.turn_condition.acquire()

        while player != self.current_player:
            self.turn_condition.wait()
        
        if not self.isOccupied(location):

            if self.current_player == 0:
                self.board[location] = "X"
            else:
                self.board[location] = "O"
            
            self.current_player = (self.current_player + 1) % 2
            self.players[self.current_player].other_play_moved(location)
            self.turn_condition.notify()
            self.turn_condition.release()
            return 1
        else:
            self.turn_condition.notify()
            self.turn_condition.release()
            return 0
    
    def isOccupied(self, location):
        return self.board[location] # an empty space is None
    
    def gameOver(self):
        "Determine if the game is over"

        #place code here testing for a game winner
        # left as an exercise for the reader

        return 0
    
def main():
    TicTacToeServer().execute()

if __name__ == "__main__":
    main()


