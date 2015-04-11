#!/usr/bin/python

import time
from pymavlink import mavutil
from GoProController import GoProController
from Detector import Detector

# open connection and wait for heartbeat
mvlnk = mavutil.mavlink_connection(device='/dev/ttyUSB0', baud=57600)

while True:
    # i = 2
    # mvlnk.waypoint_set_current_send(i)
    mvlnk.param_fetch_one(name='MISSION_CURRENT')
    msg_seq = mvlnk.recv_match(type='MISSION_CURRENT', blocking=True, timeout=1)
    print msg_seq
    # i += 1
    stop = raw_input("Enter to continue")
    if stop == 'q':
        break
