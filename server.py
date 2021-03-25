import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("Server will start on host:", host)
port = 9999
s.bind((host, port))
s.listen(3)
print('Waiting for connections')
conn, addr = s.accept()
print("Connected with", addr)
while 1:
    message = input("Server: ").encode()
    conn.send(message)
    incoming_msg = conn.recv(1024).decode()
    print("Server:", incoming_msg)
