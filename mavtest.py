#!/usr/bin/python

from pymavlink import mavutil

# open mavlink connection
mvlnk = mavutil.mavlink_connection(device='/dev/ttyUSB0', baud=57600)

# fetch the initial sequence number
while True:
    msg = mvlnk.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout=1)
    print 'GPS Lat: ' + str(msg.lat)
    print 'GPS Long: ' + str(msg.lon)
    print 'Heading: ' + str(msg.hdg / 100.0)
    print 'Altitude: ' + str(msg.relative_alt / 1000.0)
    print 'Velocity (X): ' + str(msg.vx)
    print 'Velocity (Y): ' + str(msg.vy)
    print 'Velocity (Z): ' + str(msg.vz)
