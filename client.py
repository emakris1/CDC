#!/usr/bin/python

import sys, socket, time

host = '192.168.1.1'
port = 7277

s = socket.socket()
s.connect((host, port))
print "Connected"
for i in range (1,7):
    s.send(str(i))
    time.sleep(0.05)
    data = s.recv(1024)
    print data,
s.close()
print "Disconnected"
