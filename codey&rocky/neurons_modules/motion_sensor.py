from global_object import neurons_engine_o
from codey_global_board import *
MOTION_SENSOR_TYPE = 0x63
MOTION_SENSOR_SUBTYPE = 0x06

MOTION_SENDOR_IS_SHAKE = 0x01
MOTION_SENDOR_ACC_X = 0x02
MOTION_SENDOR_ACC_Y = 0x03
MOTION_SENDOR_ACC_Z = 0x04
MOTION_SENDOR_GYRO_X = 0x05
MOTION_SENDOR_GYRO_Y = 0x06
MOTION_SENDOR_GYRO_Z = 0x07
MOTION_SENDOR_PITCH = 0x08
MOTION_SENDOR_ROLL = 0x09
MOTION_SENDOR_YAW = 0x0A

def is_shaked(index = 1):
    ret = neurons_engine_o.read(MOTION_SENSOR_TYPE, MOTION_SENSOR_SUBTYPE, [MOTION_SENDOR_IS_SHAKE], int(index))
    if ret:
        return bool(ret[0])
    else:
        return False

def get_acceleration(axis, index = 1):
    axis_id = 0

    if axis == "x":
        axis_id = 0
    elif axis == "y":
        axis_id = 1
    elif axis == "z":
        axis_id = 2
    else:
        return 0
    
    ret = neurons_engine_o.read(MOTION_SENSOR_TYPE, MOTION_SENSOR_SUBTYPE, [MOTION_SENDOR_ACC_X + axis_id], int(index))
    if ret:
        return ret[0]
    else:
        return 0

def get_gyroscope(axis, index = 1):
    axis_id = 0

    if axis == "x":
        axis_id = 0
    elif axis == "y":
        axis_id = 1
    elif axis == "z":
        axis_id = 2
    else:
        return 0
    
    ret = neurons_engine_o.read(MOTION_SENSOR_TYPE, MOTION_SENSOR_SUBTYPE, [MOTION_SENDOR_GYRO_X + axis_id], int(index))
    if ret:
        return ret[0]
    else:
        return 0

def get_pitch(index = 1):
    ret = neurons_engine_o.read(MOTION_SENSOR_TYPE, MOTION_SENSOR_SUBTYPE, [MOTION_SENDOR_PITCH], int(index))
    if ret:
        return ret[0]
    else:
        return 0
        
def get_roll(index = 1):
    ret = neurons_engine_o.read(MOTION_SENSOR_TYPE, MOTION_SENSOR_SUBTYPE, [MOTION_SENDOR_ROLL], int(index))
    if ret:
        return ret[0]
    else:
        return 0
        
def get_yaw(index = 1):
    ret = neurons_engine_o.read(MOTION_SENSOR_TYPE, MOTION_SENSOR_SUBTYPE, [MOTION_SENDOR_YAW], int(index))
    if ret:
        return ret[0]
    else:
        return 0
