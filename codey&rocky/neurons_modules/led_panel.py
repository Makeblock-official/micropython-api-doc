from global_object import neurons_engine_o
from codey_global_board import *
import binascii
from struct import pack, unpack

LEDMATRIX_TYPE = 0x65
LEDMATRIX_SUBTYPE = 0x04

LEDMATRIX_SET_ALL = 0x01
LEDMATRIX_SET_SINGLE = 0x02
LEDMATRIX_SET_PANEL = 0x03
LEDMATRIX_SET_ANIMATION = 0x04
LEDMATRIX_SHOW_ANIMATION = 0x05
LEDMATRIX_SHOW_STRING = 0x06

def __sting_to_bytes(string):
    hex_data = binascii.unhexlify(string)
    return hex_data

def set_all(red_value, green_value, blue_value, index = 1):
    if type_check(red_value, int, float) and \
       type_check(green_value, int, float) and type_check(blue_value, int, float):
        red_value = int(num_range_check(red_value, 0, 255))
        green_value = int(num_range_check(green_value, 0, 255))
        blue_value = int(num_range_check(blue_value, 0, 255))
        neurons_engine_o.send(LEDMATRIX_TYPE, LEDMATRIX_SUBTYPE, [LEDMATRIX_SET_SINGLE, \
                              0, red_value, green_value, blue_value], int(index))

def set_pixel(pos_x, pos_y, red_value, green_value, blue_value, index = 1):
    if type_check(pos_x, int, float) and type_check(pos_y, int, float) and type_check(red_value, int, float) and \
       type_check(green_value, int, float) and type_check(blue_value, int, float):
        if pos_x > 7 or pos_x < 0 or pos_y > 7 or pos_y < 0:
            return
        red_value = int(num_range_check(red_value, 0, 255))
        green_value = int(num_range_check(green_value, 0, 255))
        blue_value = int(num_range_check(blue_value, 0, 255))
        led_id = pos_y * 8 + pos_x + 1
        neurons_engine_o.send(LEDMATRIX_TYPE, LEDMATRIX_SUBTYPE, [LEDMATRIX_SET_SINGLE, \
                              led_id, red_value, green_value, blue_value], int(index))

def show_image(image_code, mode = 0, index = 1):
    if type_check(mode, int, float) and type_check(image_code, list, tuple):
        mode = int(num_range_check(mode, 0, 3))

        neurons_engine_o.send(LEDMATRIX_TYPE, LEDMATRIX_SUBTYPE, [LEDMATRIX_SET_PANEL, \
                              mode, len(image_code)] + list(image_code), int(index))

def set_animation(frame_index, data, index = 1):
    if type_check(frame_index, int, float) and type_check(data, list, tuple):
        frame_index = int(num_range_check(frame_index, 0, 3))

        neurons_engine_o.send(LEDMATRIX_TYPE, LEDMATRIX_SUBTYPE, [LEDMATRIX_SET_ANIMATION, \
                              frame_index, len(data)] + list(data), int(index))

def show_animation(frame_speed, mode, index = 1):
    if type_check(frame_speed, int, float) and type_check(mode, int, float):
        frame_speed = int(num_range_check(frame_speed, 0, 2))
        mode = int(num_range_check(mode, 0, 3))

        neurons_engine_o.send(LEDMATRIX_TYPE, LEDMATRIX_SUBTYPE, [LEDMATRIX_SHOW_ANIMATION, \
                              frame_speed, mode], int(index))

def show_string(red_value, green_value, blue_value, data, index = 1):
    if type_check(red_value, int, float) and type_check(green_value, int, float) \
       and type_check(blue_value, int, float):
        data = str(data)
        red_value = int(num_range_check(red_value, 0, 255))
        green_value = int(num_range_check(green_value, 0, 255))
        blue_value = int(num_range_check(blue_value, 0, 255))
        char_num = len(data)
        data = list(map(ord, list(data)))
        neurons_engine_o.send(LEDMATRIX_TYPE, LEDMATRIX_SUBTYPE, [LEDMATRIX_SHOW_STRING, \
                              red_value, green_value, blue_value, char_num] + data, int(index))

def clear(index = 1):
    neurons_engine_o.send(LEDMATRIX_TYPE, LEDMATRIX_SUBTYPE, [LEDMATRIX_SET_SINGLE, \
                          0, 0, 0, 0], int(index))