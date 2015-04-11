#!/usr/bin/python

import time
from pymavlink import mavutil
from GoProController import GoProController
from Detector import Detector

MIN_SEQ = 2
MAX_SEQ = 4

# open gopro connection
gpc = GoProController(device_name='wlan1')
gpc.connect('SARSGoPro', 'sarsgopro')
# det = Detector()

# open mavlink connection
mvlnk = mavutil.mavlink_connection(device='/dev/ttyUSB0', baud=57600)

# create an array to store all pulled images
imgs = []

# fetch the initial sequence number
mvlnk.param_fetch_one(name='MISSION_CURRENT')
msg_seq = mvlnk.recv_match(type='MISSION_CURRENT', blocking=True, timeout=1)
current_seq = msg_seq.seq
print 'Starting Sequence Number: ' + str(current_seq)

# loop until the sequence number increments past the takeoff sequence
while current_seq < MIN_SEQ:
    mvlnk.param_fetch_one(name='MISSION_CURRENT')
    msg_seq = mvlnk.recv_match(type='MISSION_CURRENT', blocking=True, timeout=1)
    current_seq = msg_seq.seq
    print 'Waiting until waypoint sequence is reached... Current Sequence: ' + str(current_seq)

# loop until the sequence number increments to the landing sequence
while current_seq <= MAX_SEQ:
   # wait until we've reached the waypoint
    mvlnk.param_fetch_one(name='NAV_CONTROLLER_OUTPUT')
    msg_nav = mvlnk.recv_match(type='NAV_CONTROLLER_OUTPUT', blocking=True, timeout=1)
    while msg_nav.wp_dist > 0:
        mvlnk.param_fetch_one(name='NAV_CONTROLLER_OUTPUT')
        msg_nav = mvlnk.recv_match(type='NAV_CONTROLLER_OUTPUT', blocking=True, timeout=1)
        print 'Waypoint Distance: ' + str(msg_nav.wp_dist)
    print 'Waypoint reached!'

    # wait 3 seconds, then capture an image from the GoPro
    print 'Waiting 3 seconds...'
    time.sleep(3)
    img = gpc.getImage('SARSGoPro', 'sarsgopro')
    if img:
        print('Image downloaded succeeded!')
        imgs.append(img)
    else:
        print('Image download failed.')
        imgs.append(None)

    mvlnk.param_fetch_one(name='MISSION_CURRENT')
    msg_seq = mvlnk.recv_match(type='MISSION_CURRENT', blocking=True, timeout=1)

    # wait for the sequence number to increment
    while current_seq == msg_seq:
    if current_seq != msg_seq.seq:
        current_seq = msg_seq.seq
        print 'Current Sequence: ' + str(msg_seq.seq)

 
