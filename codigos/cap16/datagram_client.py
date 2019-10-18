# Python Journey - Chapter 16
# Set up a client via datagrams

import socket

HOST = "127.0.0.1"
PORT = 5000
counter = 0

# step 1: create a socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:

    # step 2: send a packet
    packet = input("Packet>>>")
    print("\nSending packet containing:", packet)
    my_socket.sendto(packet, (HOST,PORT))
    print("Packet sent\n")

    # step 3: receive packet back from server
    packet, address = my_socket.recvfrom(1024)
    
    print("Packet received")
    print("From host: ", address[0])
    print("Host port: ", address[1])
    print("Length: ", len(packet))
    print("Containing")
    print("\t" + packet + "\n")

my_socket.close()






