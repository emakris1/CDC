#!/usr/bin/python

import time
from pymavlink import mavutil
from GoProController import GoProController
from Detector import Detector

# open connection and wait for heartbeat
mvlnk = mavutil.mavlink_connection(device='/dev/ttyUSB0', baud=57600)

while True:
    mvlnk.param_fetch_one(name='HEARTBEAT')
    msg = mvlnk.recv_match(type='HEARTBEAT', blocking=True, timeout=2)
    print msg

    mvlnk.param_fetch_one(name='MISSION_CURRENT')
    msg = mvlnk.recv_match(type='MISSION_CURRENT', blocking=True, timeout=2)
    print msg

    mvlnk.param_fetch_one(name='NAV_CONTROLLER_OUTPUT')
    msg = mvlnk.recv_match(type='NAV_CONTROLLER_OUTPUT', blocking=True, timeout=2)
    print msg
