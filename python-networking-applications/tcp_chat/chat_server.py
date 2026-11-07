"""
    chat_server.py
    jessica soler
    4/16/25
"""

import socket

# accept connections from this computer only
SERVER_IP = "127.0.0.1"

# port to listen on (65525< non-privileged port >1023)
# listening server port
PORT = 8081

def main():
    # create a socket object
    server_socket = socket.socket(
        socket.AF_INET,       # TCP/IPv4 address
        socket.SOCK_STREAM   # create TCP transport layer socket
    )
    
    # bind socket to a tuple (IP address, port address)
    server_socket.bind((SERVER_IP, PORT))
    
    # start server socket listener, waiting for connection
    server_socket.listen()
    print(f"Listening for incoming connections on port {PORT} . . .")
    
    # accept a connection from a client, return socket object and IP address
    connection, address = server_socket.accept()
    print(f"Connection from: {address}")
    
    while True:
        # recieve data into a 1024 byte buffer
        data = connection.recv(1024).decode("utf-8")
        
        if (data == "q"):
            # close the current client connection
            connection.close()
            print("Client disconnected")
            print(f"Listening for incoming connections on port {PORT} . . .")
            
            # ready for a new client connection
            connection, address = server_socket.accept()
            print(f"Connection from: {address}")
        else:
            # print the client message
            print(f">> {data}")
            
            # get a message from the user
            message = input("Server>> ")
            
            # send message to client
            connection.send(message.encode("utf-8"))
            
            
main()