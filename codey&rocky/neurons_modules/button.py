from global_object import neurons_engine_o
from codey_global_board import *
BUTTON_TYPE = 0x64
BUTTON_SUBTYPE = 0x02
BUTTON_IS_PRESSED = 0x01

def is_pressed(index = 1):
    ret = neurons_engine_o.read(BUTTON_TYPE, BUTTON_SUBTYPE, [BUTTON_IS_PRESSED], int(index))
    if ret:
        return bool(ret[0])
    else:
        return False

def set_report_mode(mode, time, index = 1):
    pass