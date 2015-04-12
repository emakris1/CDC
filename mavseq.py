#!/usr/bin/python

import time
from pymavlink import mavutil
from GoProController import GoProController
from Detector import Detector

MIN_WP_SEQ = 2
MAX_WP_SEQ = 4

# open gopro connection
gpc = GoProController(device_name='wlan1')
gpc.connect('SARSGoPro', 'sarsgopro')
det = Detector()

# open mavlink connection
mvlnk = mavutil.mavlink_connection(device='/dev/ttyUSB0', baud=57600)

# create an array to store all pulled images
imgs = []

# fetch the initial sequence number
mvlnk.param_fetch_one(name='MISSION_CURRENT')
msg_seq = mvlnk.recv_match(type='MISSION_CURRENT', blocking=True, timeout=1)
current_seq = msg_seq.seq
print 'Starting Sequence Number: ' + str(current_seq)

# loop until we've made it past the takeoff sequence
in_takeoff_seq = True
while in_takeoff_seq:
    mvlnk.param_fetch_one(name='MISSION_CURRENT')
    msg_seq = mvlnk.recv_match(type='MISSION_CURRENT', blocking=True, timeout=1)
    current_seq = msg_seq.seq
    if current_seq < MIN_WP_SEQ:
        print 'Waiting until takeoff has finished... Current Sequence: ' + str(current_seq)
    else:
        in_takeoff_seq = False
        print 'Takeoff finished! Current Sequence: ' + str(current_seq)

# loop through waypoint sequences until we reach the landing sequence
failed = False
in_waypoint_seq = True
while not failed and in_waypoint_seq:
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
        imgs.append(img)
        print('Image download succeeded!')
    else:
        failed = True
        print('Image download failed. Abort mission.')

    # wait for the sequence number to increment
    incremented = False
    while not incremented:
        mvlnk.param_fetch_one(name='MISSION_CURRENT')
        msg_seq = mvlnk.recv_match(type='MISSION_CURRENT', blocking=True, timeout=1)
        if current_seq == msg_seq.seq:
            print 'Waiting for sequence number to increment...'
        else:
            current_seq = msg_seq.seq
            incremented = True
            print 'Sequence number incremented! Current Sequence Number: ' + str(current_seq)

    if current_seq > MAX_WP_SEQ:
        in_waypoint_seq = False
        print 'All waypoints visited!'

# run the object detection the images
if not failed:
    print 'Running object detection..'
    found = False
    for img in imgs:
        if(det.detect(img)):
            found = True
            print('Object detected at waypoint ' + str(imgs.index(img) + 1) + '!')
            break

    if not found:
        print('Object not detected.')
