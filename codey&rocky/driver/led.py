from global_object import led_o
from codey_global_board import *

RGB_RED_INDEX = 0
RGB_GREEN_INDEX = 1
RGB_BLUE_INDEX = 2

class led():
    def __init__(self):
        pass

    def show(self, r, g, b):
        if (not type_check(r, int, float)) or (not type_check(g, int, float)) or (not type_check(b, int, float)):
            return
        r = num_range_check(r, 0, 255)
        g = num_range_check(g, 0, 255)
        b = num_range_check(b, 0, 255)
        led_o.set_color(int(r), int(g), int(b))

    def set_red(self, val):
        if (not type_check(val, int, float)):
            return    
        val = num_range_check(val, 0, 255)
        led_o.set_r_g_b(int(val), RGB_RED_INDEX)

    def set_green(self, val):
        if (not type_check(val, int, float)):
            return    
        val = num_range_check(val, 0, 255)
        led_o.set_r_g_b(int(val), RGB_GREEN_INDEX)

    def set_blue(self, val):
        if (not type_check(val, int, float)):
            return    
        val = num_range_check(val, 0, 255)
        led_o.set_r_g_b(int(val), RGB_BLUE_INDEX)

    def off(self):
        led_o.set_color(0, 0, 0)