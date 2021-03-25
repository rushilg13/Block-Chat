import socket
import sys
import time

s = socket.socket()
host = input("Please enter host name: ")
port = 9999
s.connect((host, port))
print("Connected to Server")
while 1:
    incoming_msg = s.recv(1024).decode()
    print("Server:", incoming_msg)
    msg = input("Client: ").encode()
    s.send(msg)