"""
    network_client.py
    jessica soler
    4/7/25
    simple network client
"""

# python built in socket library
import socket
from binascii import hexlify
from time import sleep

# use 127.0.0.1 if you are running the server program
# on the same computer you are running the client program
# change the IP address if the server program
# is on a different computer
SERVER_IP = "127.0.0.1"

# specify the destination port
PORT = 8801

def main():
    # create TCP IPv4 socket
    client_socket = socket.socket(
        socket.AF_INET,        # TCP/IP v4 address
        socket.SOCK_STREAM,    # create TCP transport layer socket
    )
    
    message = f"Hello Server, I have connected on port {PORT}"
    
    # convert unicode utf-8 string to byte data type
    data = message.encode("utf-8")
    # display bytestream data
    binary = hexlify(data).decode()
    print(binary)
    
    # connect to the server on the specified IP address and port
    client_socket.connect((SERVER_IP, PORT))
    
    # send the bytestream
    client_socket.send(data)
    # print the message string to confirm transmission
    print(message)
    
    # pause to allow communicaiton to finish
    sleep(1)
    
    # close the connection
    client_socket.close()
    print("Message sent. Connection closed.")
    
main()