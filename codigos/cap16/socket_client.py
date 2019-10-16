# Python Journey - Chapter 16
# Set up a client via sockets

import socket

HOST = "127.0.0.1"
PORT = 5000
counter = 0

# step 1: create a socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# step 2: connect the socket
my_socket.connect((HOST, PORT))
print("connected to the server")

# step 3: process connection
server_message = my_socket.recv(1024)

while server_message != "SERVER>>> TERMINATE":

    if not server_message:
        break

    print(server_message)
    client_message = input("CLIENT>>> ")
    my_socket.send("CLIENT>>> " + client_message)
    server_message = my_socket.recv(1024)
    
print("Connection terminated")
my_socket.close()

