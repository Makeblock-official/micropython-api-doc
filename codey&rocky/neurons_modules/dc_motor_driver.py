from global_object import neurons_engine_o
from codey_global_board import *
DMOTOR_TYPE = 0x62
DMOTOR_SUBTYPE = 0x02

def set_power(speed, ch = 0, index = 1):
    if type_check(ch, int, float) and type_check(speed, int, float):
        ch = num_range_check(ch, 0, 2)
        speed = num_range_check(speed, -100, 100)
        if ch == 0:
            neurons_engine_o.send(DMOTOR_TYPE, DMOTOR_SUBTYPE, [ch + 1, speed, speed], int(index))
        else:
            neurons_engine_o.send(DMOTOR_TYPE, DMOTOR_SUBTYPE, [ch + 1, speed], int(index))
