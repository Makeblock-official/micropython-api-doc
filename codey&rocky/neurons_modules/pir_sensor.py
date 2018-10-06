from global_object import neurons_engine_o
from codey_global_board import *
PIR_TYPE = 0x63
PIR_SUBTYPE = 0x0C
PIR_READ = 0x01
        
def is_activated(index = 1):
    ret = neurons_engine_o.read(PIR_TYPE, PIR_SUBTYPE, [PIR_READ], int(index))
    if ret:
        return bool(ret[0])
    else:
        return False
        
def set_report_mode(mode, time, index = 1):
    pass