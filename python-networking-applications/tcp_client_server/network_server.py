"""
    network_server.py
    jessica soler
    4/7/25
    simple network server
"""

# python built in socket library
import socket
from binascii import hexlify

# accept connections from this computer only
SERVER_IP = "127.0.0.1"

# port to listen on (non-privileged prots are > 1023)
# listening server port
PORT = 8801

def main():
    # create a socket object
    server_socket = socket.socket(
        socket.AF_INET,        # TCP/IP v4 address
        socket.SOCK_STREAM,    # create TCP transport layer socket
    )
    
    # bind scoket to a tuple (IP Address, Port Address)
    server_socket.bind((SERVER_IP, PORT))
    
    # start server socket listener, waiting for a connection
    server_socket.listen()
    print(f"Listening for incomming connections on {PORT} . . . ")
    
    while True:
        # accept a connection
        # return socket object and IP address
        connection, client_address = server_socket.accept()
        
        # print returned socket info for debugging
        print(connection)
        
        print(f"Connection from: {client_address}")
        
        # send message to client, encode string to bytestream
        # for transmission over the network
        connection.send("You are connected".encode("utf-8"))
        
        # recieve data into a 1024 byte buffer
        data = connection.recv(1024)
        print(f"THe client is connected")
        
        if data:
            # if the server receives data
            # display bystream data
            binary = hexlify(data).decode()
            print(binary)
            
            # convert bytestream to text/string
            message = data.decode("utf-8")
            print(message)
            
            # close the connection
            connection.close()
            print("Client disconnected")
            print(f"Listening for incoming connections on {PORT} . . .")
            
main()