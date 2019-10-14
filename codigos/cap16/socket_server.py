# Python Journey - Chapter 16
# Set up a server via sockets

import socket

HOST = "127.0.0.1"
PORT = 5000
counter = 0

# step 1: create a socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# step 2: bind the socket
my_socket.bind((HOST, PORT))

while 1:
    # step 3: prepare for a connection
    print("wating for connection")
    my_socket.listen(1)


    # step 4: wait for and accept a connection
    connection, address = my_socket.accept()
    counter += 1
    print("connection", counter, "received from:", address[0])

    # step 5: process connection
    connection.send("SERVER>>> Connection successfully")
    client_message = connection.recv(1024)

    while client_message != "CLIENT>>> TERMINATE":

        if not client_message:
            break

        print(client_message)
        server_message = input("SERVER>>> ")
        connection.send("SERVER>>> " + server_message)
        client_message = connection.recv(1024)
    
    # step 6: close connection
    print("Connection terminat")
    connection.close()

