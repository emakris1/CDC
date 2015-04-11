#!/usr/bin/python

import time
from pymavlink import mavutil
from GoProController import GoProController
from Detector import Detector

# open connection and wait for heartbeat
mvlnk = mavutil.mavlink_connection(device='/dev/ttyUSB0', baud=57600)

stop = raw_input("Press enter to continue: ")

mvlnk.set_mode('GUIDED')
mvlnk.param_fetch_one(name='COMMAND_ACK')
msg = mvlnk.recv_match(type='COMMAND_ACK', blocking=True, timeout=3)
print msg # result 0 means accepted

mvlnk.mav.mission_item_send(mvlnk.target_system, mvlnk.target_component, seq, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z)
mvlnk.param_fetch_one(name='COMMAND_ACK')
msg = mvlnk.recv_match(type='COMMAND_ACK', blocking=True, timeout=3)
print msg # result 0 means accepted

# GPS COORDINATE
# 28.6284332275391
# -81.2000427246094

# def mission_item_send(self, target_system, target_component, seq, frame, command, current, autocontinue, param1, param2, param3, param4, x, y, z):
#                 '''
#                 Message encoding a mission item. This message is emitted to announce
#                 the presence of a mission item and to set a mission
#                 item on the system. The mission item can be either in
#                 x, y, z meters (type: LOCAL) or x:lat, y:lon,
#                 z:altitude. Local frame is Z-down, right handed (NED),
#                 global frame is Z-up, right handed (ENU). See also
#                 http://qgroundcontrol.org/mavlink/waypoint_protocol.
#
#                 target_system             : System ID (uint8_t)
#                 target_component          : Component ID (uint8_t)
#                 seq                       : Sequence (uint16_t)
#                 frame                     : The coordinate system of the MISSION. see MAV_FRAME in mavlink_types.h (uint8_t)
#                 command                   : The scheduled action for the MISSION. see MAV_CMD in common.xml MAVLink specs (uint16_t)
#                 current                   : false:0, true:1 (uint8_t)
#                 autocontinue              : autocontinue to next wp (uint8_t)
#                 param1                    : PARAM1 / For NAV command MISSIONs: Radius in which the MISSION is accepted as reached, in meters (float)
#                 param2                    : PARAM2 / For NAV command MISSIONs: Time that the MAV should stay inside the PARAM1 radius before advancing, in milliseconds (float)
#                 param3                    : PARAM3 / For LOITER command MISSIONs: Orbit to circle around the MISSION, in meters. If positive the orbit direction should be clockwise, if negative the orbit direction should be counter-clockwise. (float)
#                 param4                    : PARAM4 / For NAV and LOITER command MISSIONs: Yaw orientation in degrees, [0..360] 0 = NORTH (float)
#                 x                         : PARAM5 / local: x position, global: latitude (float)
#                 y                         : PARAM6 / y position: global: longitude (float)
#                 z                         : PARAM7 / z position: global: altitude (float)
# 
