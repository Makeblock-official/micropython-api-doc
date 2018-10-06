from global_object import neurons_engine_o
from codey_global_board import *
ULTRASONIC_MOISTURE_TYPE = 0x63
ULTRASONIC_MOISTURE_SUBTYPE = 0x03

ULTRASONIC_READ = 0x01
def get_distance(index = 1):
    ret = neurons_engine_o.read(ULTRASONIC_MOISTURE_TYPE, ULTRASONIC_MOISTURE_SUBTYPE, [ULTRASONIC_READ], int(index))
    if ret:
        return int(ret[0])
    else:
        return 0

def set_report_mode(mode, time, index = 1):
    pass