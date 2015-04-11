#!/usr/bin/python           # This is server.py file

import sys
import socket

s = socket.socket()
host = '192.168.1.102'
port = 3284
s.bind((host, port))
s.listen(5)
print 'Listening for a connection...'
c, addr = s.accept()
print 'Accepted connection from', addr
while True:
    data = c.recv(1024)
    print 'Server received from client', addr, ':', data
    if (data == 'DISCONNECT'):
        c.send('Thank you for using the server!')
        print 'Closing connection to', addr
        c.close()
        break
