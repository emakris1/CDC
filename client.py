#!/usr/bin/python

import sys, socket, string, time

host = '192.168.1.1'
port = 7277

s = socket.socket()
s.connect((host, port))
s.send('s')
time.sleep(0.50)
msg = s.recv(2**10)
print msg
s.close()

s = socket.socket()
s.connect((host, port))
s.send('p')
time.sleep(0.50)
msg = s.recv(2**10)
print msg
s.close()

s = socket.socket()
s.connect((host, port))
s.send('d')
time.sleep(0.50)
msg = s.recv(2**10)
print msg
s.close()

s = socket.socket()
s.connect((host, port))
s.send('a')
time.sleep(0.50)
msg = s.recv(2**10)
print msg
s.close()

s = socket.socket()
s.connect((host, port))
s.send('o')
time.sleep(0.50)
msg = s.recv(2**10)
print msg
s.close()

s = socket.socket()
s.connect((host, port))
s.send('h')
time.sleep(0.50)
msg = s.recv(2**10)
print msg
s.close()
