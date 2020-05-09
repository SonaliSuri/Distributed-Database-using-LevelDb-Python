#!/usr/bin/python3

import socket
import sys
from threading import Thread


from raft.client import DistributedDict
from threading import Thread
d=DistributedDict('127.0.0.1',5254)
def t1():
    try:
        stck='STX'
        price=59
        d1 = DistributedDict('127.0.0.1', 5254)
        d1[stck] = price
        print('Value inserted successfully into the database')
    except:
        print('t1 error')

t1()


if len(sys.argv) < 3:
    print("pass three ports")
    exit()
    
port1 = int(sys.argv[1])
port2 = int(sys.argv[2])
port3 = int(sys.argv[3])


# create a socket object
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

monitor_val = b'59'
# connection to hostname on the port.
s1.connect((host, port1))
s2.connect((host, port2))
s3.connect((host, port3))

#stck=input('Enter the stock code ')
stck='STX'
s1.send(str.encode(stck))
s2.send(str.encode(stck))
s3.send(str.encode(stck))

# Receive no more than 1024 bytes
msg1 = s1.recv(1024)                                     
if monitor_val == msg1:
    print("s1 monitor is sane")
else:
    print("s1 server is faulty");

msg2 = s2.recv(1024)


if monitor_val == msg2:
    print("s2 monitor is sane")
else:
    print("s2 server is faulty");

msg3 = s3.recv(1024)                                     
if monitor_val == msg3:
    print("s3 monitor is sane")
else:
    print("s3 server is faulty");

s1.close()
s2.close()
s3.close()

