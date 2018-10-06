from global_object import neurons_engine_o
from codey_global_board import *
RGB_SCRIPT_TYPE = 0x65
RGB_SCRIP_SUBTYPE = 0x03

RGB_SCRIP_SET = 0x01
RGB_SCRIP_SET_MODE = 0x02

# black   0x00
# red     0x01
# orange  0x02
# yellow  0x03
# green   0x04
# cyan    0x05
# blue    0x06
# purple  0x07
# white   0x08
color_dict = {"black": 0, "red": 1, "orange": 2, "yellow": 3, "green" : 4,\
               "cyan": 5, "blue": 0x06, "purple": 7, "white": 8}
def set_single(led_id, red_value, green_value, blue_value, index = 1):
    if type_check(led_id, int, float) and type_check(red_value, int, float) and \
       type_check(green_value, int, float) and type_check(blue_value, int, float):
        led_id = int(num_range_check(led_id, 1, 127))
        red_value = int(num_range_check(red_value, 0, 255))
        green_value = int(num_range_check(green_value, 0, 255))
        blue_value = int(num_range_check(blue_value, 0, 255))

        neurons_engine_o.send(RGB_SCRIPT_TYPE, RGB_SCRIP_SUBTYPE, [RGB_SCRIP_SET, led_id, red_value, green_value, blue_value], int(index))

def set_all(red_value, green_value, blue_value, index = 1):
    if type_check(red_value, int, float) and type_check(green_value, int, float) \
       and type_check(blue_value, int, float):
        red_value = int(num_range_check(red_value, 0, 255))
        green_value = int(num_range_check(green_value, 0, 255))
        blue_value = int(num_range_check(blue_value, 0, 255))
        neurons_engine_o.send(RGB_SCRIPT_TYPE, RGB_SCRIP_SUBTYPE, [RGB_SCRIP_SET, 0, red_value, green_value, blue_value], int(index))

def set_effect(mode, change_speed, data, index = 1):
    # add parameters checking here
    if type_check(mode, int, float) and type_check(change_speed, int, float)\
       and type_check(data, list, tuple):

        mode = int(num_range_check(mode, 0, 5))
        change_speed = int(num_range_check(change_speed, 0, 8))
        data = list(data)
        for i in range(len(data)):
            if type(data[i]) == str:
                if data[i] in color_dict:
                    data[i] = color_dict[i]

        neurons_engine_o.send(RGB_SCRIPT_TYPE, RGB_SCRIP_SUBTYPE, [RGB_SCRIP_SET_MODE, mode, change_speed, len(data)] + list(data), int(index))

# clear() --- rgb_strip.set_mode(0, 0, 16, [])