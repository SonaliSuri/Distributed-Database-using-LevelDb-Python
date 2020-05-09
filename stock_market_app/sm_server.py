#!/usr/bin/python3           
import socket                                         
import plyvel
import sys
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)
arguments = len(sys.argv) - 1
if arguments < 1:
    print('Enter the path to db')
    exit()

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    msg = clientsocket.recv(1024)
    path = sys.argv[2]
    opendb = 1
    try:
        db = plyvel.DB(path, create_if_missing=True)
    except:
        continue


    msg = db.get(msg)
    db.close()
    
    if not msg:
        print("Value does not exist")
        clientsocket.send(b'None')
        continue

    clientsocket.send(bytes(msg))
    clientsocket.close()
