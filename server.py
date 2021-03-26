import socket
import sys
import time
from datetime import datetime, date
import hashlib

class Block:
    def __init__(self, blocknumber, prev_hash, time_stamp, message):
        self.blocknumber = blocknumber
        self.message = message
        self.prev_hash = prev_hash
        self.time_stamp = time_stamp
        hash = str(blocknumber) + message + prev_hash + time_stamp
        self.block_hash = hashlib.sha256(hash.encode()).hexdigest()

now = datetime.now()
now = now.strftime("%H:%M:%S") 
today = date.today()
today =  today.strftime("%d/%m/%Y") 
time_stamp = (today + " " +now)
genesis_block = Block(0, hashlib.sha256("Block-Chat".encode()).hexdigest(), time_stamp, "Secure Chat Application is Live!")
# print(genesis_block.message)

s = socket.socket()
host = socket.gethostname()
print("Server will start on host:", host)
port = 9999
s.bind((host, port))
s.listen(3)
print('Waiting for connections')
conn, addr = s.accept()
print("Connected with", addr)
blocknumber = 1
prev_hash = genesis_block.block_hash
while 1:
    message = input("Server: ").encode()
    now = datetime.now()
    now = now.strftime("%H:%M:%S")        # Current time
    today = date.today()
    today =  today.strftime("%d/%m/%Y")   # Current date
    time_stamp = (today + " " +now)
    new_block = Block(blocknumber, prev_hash, time_stamp, message.decode("utf-8"))
    blocknumber+=1
    prev_hash = new_block.block_hash
    print(new_block.blocknumber, new_block.prev_hash, new_block.time_stamp, new_block.message, new_block.block_hash)
    conn.send(message)
    incoming_msg = conn.recv(1024).decode()
    print("Client:", incoming_msg)
