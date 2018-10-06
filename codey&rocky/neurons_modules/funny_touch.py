from global_object import neurons_engine_o
from codey_global_board import *
FUNNY_TOUCH_TYPE = 0x64
FUNNY_TOUCH_SUBTYPE = 0x04

FUNNY_TOUCH_READ = 0x01

def __get_touched_value(index, touch_id = 0):
    ret = neurons_engine_o.read(FUNNY_TOUCH_TYPE, FUNNY_TOUCH_SUBTYPE, [FUNNY_TOUCH_READ], int(index))
    if ret:
        return bool(ret[0] & (1 << touch_id))
    else:
        return False 

def is_blue_touched(index = 1):
    return __get_touched_value(index, 0)

def is_red_touched(index = 1):
    return __get_touched_value(index, 2)

def is_green_touched(index = 1):
    return __get_touched_value(index, 3)

def is_yellow_touched(index = 1):
    return __get_touched_value(index, 1)

def set_report_mode(mode, time, index = 0):
    pass
    
