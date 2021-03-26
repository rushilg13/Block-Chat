import socket
import sys
import time
from datetime import datetime, date
import hashlib
import numpy as np

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
genesis_block = Block(0, hashlib.sha256("Block-Chat".encode()).hexdigest(), time_stamp, "Secure Chat Application for client is Live!")

s = socket.socket()
host = input("Please enter host name: ")
port = 9999
s.connect((host, port))
print("Connected to Server")
blocknumber = 1
prev_hash = genesis_block.block_hash
while 1:
    blockchain_b = s.recv(20480000)
    blockchain = list(bytes(blockchain_b))
    incoming_msg = s.recv(5096).decode()
    print("Server:", incoming_msg)
    msg = input("Client: ").encode()
    now = datetime.now()
    now = now.strftime("%H:%M:%S")        # Current time
    today = date.today()
    today =  today.strftime("%d/%m/%Y")   # Current date
    time_stamp = (today + " " +now)
    new_block = Block(blocknumber, prev_hash, time_stamp, msg.decode("utf-8"))
    blockchain.append(new_block)
    blockchain_b = np.array(blockchain)
    blockchain_b.tobytes()
    blocknumber+=1
    prev_hash = new_block.block_hash
    s.send(blockchain_b)
    s.send(msg)