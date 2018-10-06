from global_object import neurons_engine_o
from codey_global_board import *
SOIL_MOISTURE_TYPE = 0x63
SOIL_MOISTURE_SUBTYPE = 0x08

SOIL_MOISTURE_READ = 0x01

def get_value(index = 1):
    ret = neurons_engine_o.read(SOIL_MOISTURE_TYPE, SOIL_MOISTURE_SUBTYPE, [SOIL_MOISTURE_READ], int(index))
    if ret:
        return ret[0]
    else:
        return 0

def set_report_mode(mode, time, index = 1):
    pass