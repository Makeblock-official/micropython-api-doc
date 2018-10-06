from global_object import neurons_engine_o
from codey_global_board import *
SERVO_TYPE = 0x62
SERVO_SUBTYPE = 0x03

def set_angle(position, ch = 0, index = 1):
    if type_check(ch, int, float) and type_check(position, int, float):
        ch = num_range_check(ch, 0, 2)
        position = num_range_check(position, 0, 180)
        if ch == 0:
            neurons_engine_o.send(SERVO_TYPE, SERVO_SUBTYPE, [ch + 1, position, position], int(index))
        else:
            neurons_engine_o.send(SERVO_TYPE, SERVO_SUBTYPE, [ch + 1, position], int(index))