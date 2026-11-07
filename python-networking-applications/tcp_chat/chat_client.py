"""
    chat_client.py
    jessica soler
    4/16/25
"""

# python built in socket library
import socket

# use 127.0.0.1 or localhost if you are running the server program
# on the same computer you are running the client program
# change the IP address if the server program is on another computer
SERVER_IP = "127.0.0.1"

# specify the destination port
PORT = 8081

def main():
    # create a socket object
    client_socket = socket.socket(
        socket.AF_INET,       # TCP/IPv4 address
        socket.SOCK_STREAM   # create TCP transport layer socket
    )
    
    # connect to the server on the specified IP address and port
    client_socket.connect((SERVER_IP, PORT))
    
    while True:
        # get a message from the user
        message = input("Client>> ")
        
        if (message == "q"):
            # send byte encoded message to server
            client_socket.send(message.encode("utf-8"))
            
            client_socket.close()
            quit()
            
        else:
            
            # send byte encoded message to server
            client_socket.send(message.encode("utf-8"))
            
            # recieve response from server
            message = client_socket.recv(1024)
            
            # print decoded byte message
            print(f">> {message.decode('utf-8')}")
            
main()