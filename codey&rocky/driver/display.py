from codey_global_board import *
from global_object import display_o
import re
import time
import binascii

COLUMN_ID_MAX = 15
LINE_ID_MAX = 7 

def __sting_to_bytes(string):
    hex_data = binascii.unhexlify(string)
    return hex_data

def __get_image(image_string):
    temp_list = [0] * 16
    if len(image_string) < 32:  # 16 *2
        image_string = image_string + '0' * (32- len(image_string))
    if len(image_string) > 32:  # 16 *2
        image_string = image_string[0:32]
    return list(__sting_to_bytes(image_string))

class display():
    def __init__(self):
        pass

    def show_image(self, image, pos_x = 0, pos_y = 0, time_s = None):
        if (not type_check(pos_x, int, float)) or (not type_check(pos_y, int, float)):
            return
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        if pos_x > 15 or pos_x < -15 or pos_y > 7 or  pos_y < -7:
            display_o.clean()
            
        temp_list = [0] * 16

        if type_check(image, list):
            for i in range(len(image) if len(image) < 16 else 16):
                temp_list[i] = image[i]
            display_o.faceplate_show(pos_x, pos_y, *image)

        elif type_check(image, str):
            temp_list = __get_image(image)
        if time_s == None:
            display_o.faceplate_show(pos_x, pos_y, *temp_list)
        elif type_check(time_s, int, float):
            if time_s <= 0:
                return
            display_o.faceplate_show_with_time(pos_x, pos_y, int(time_s * 1000), *temp_list)

    def show(self, var, pos_x = None, pos_y = None, wait = True):
        if var == '':
            self.clear()
            return

        if pos_x != None or pos_y != None:
            if pos_x == None:
                pos_x = 0
            if pos_y == None:
                pos_y = 0

            if (not type_check(pos_x, int, float)) or (not type_check(pos_y, int, float)):
                return
            pos_x = int(pos_x)
            pos_y = int(pos_y)
            display_o.chars_show(pos_x, pos_y, str(var))
        else:
            if type_check(var, int, float):
                ret = int_value_scale_check(var)
                if ret == 1:
                    var = 2147 #2^31 = 2147483648
                elif ret == 2:
                    var = -21474

            if type_check(var, bool):
                if var == True:
                    display_o.string_show('true', wait)
                elif var == False:
                    display_o.string_show('false', wait)

            elif type_check(var, str):
                temp =  re.match(r"\d?\d:\d\d?", var)
                if len(var) >= 3 and temp != None:
                    temp = temp.group(0)
                    display_o.time_show_2(temp, len(temp))
                else:
                    display_o.string_show(var, wait) # 1: to_stop, 0: not to_stop

            elif type_check(var, int):
                display_o.number_show(str(var))

            elif type_check(var, float): # python str(0.000009) equal 9.00000e-06
                if var < 0.001 and var > 0: 
                    if len(str(var)) == 3:
                        display_o.number_show("0.0")
                    elif len(str(var)) == 4:
                        display_o.number_show("0.00")
                    else:
                        display_o.number_show("0.000")
                elif var < 0 and var > -0.01:
                    if len(str(var)) == 4:
                        display_o.number_show("-0.0")
                    else:
                        display_o.number_show("-0.00")
                else:
                    if var < 0:
                        var -= 0.005
                    elif var > 0:
                        var += 0.0005

                    var = str(var)
                    if len(var) > 5:
                        var = var[0 : 5]
                    z_num = 0
                    if '.' in var:
                        while True:
                            if var[-1 - z_num] == '0':
                                z_num += 1
                            else:
                                break
                    if z_num == 0:
                        display_o.number_show(var)
                    elif var[-1 - z_num] == '.':
                        display_o.number_show(var[0 : len(var) - z_num + 1])
                    else:
                        display_o.number_show(var[0 : len(var) - z_num])
            else:
                display_o.string_show(str(var), wait) # 1: to_stop, 0: not to_stop

    def set_pixel(self, pos_x, pos_y, status):
        if (not type_check(pos_x, int, float)) or (not type_check(pos_y, int, float)):
            return

        pos_x = int(pos_x)
        pos_y = int(pos_y)
        if pos_x < 0 or pos_x > 15 or pos_y < 0 or pos_y > 7:
            return  
        if status:
            display_o.pixel_control(pos_x, pos_y, 1)
        else:
            display_o.pixel_control(pos_x, pos_y, 0)

    def get_pixel(self, pos_x, pos_y):
        if (not type_check(pos_x, int, float)) or (not type_check(pos_y, int, float)):
            return False
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        if pos_x < 0 or pos_x > 15 or pos_y < 0 or pos_y > 7:
            return  False
        return display_o.get_pixel(pos_x, pos_y)

    def toggle_pixel(self, pos_x, pos_y):
        if (not type_check(pos_x, int, float)) or (not type_check(pos_y, int, float)):
            return
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        if pos_x < 0 or pos_x > 15 or pos_y < 0 or pos_y > 7:
            return      
        display_o.pixel_invert(pos_x, pos_y)

    def clear(self):
        display_o.clean()

    def animation(self, animation_name, to_stop = False):
        face_dict = {"cat": 0, "dog": 0, "test": 0, "happy": 1, "cry": 2, "dispirited": 3, "angry": 4, "fear": 5} 
        if type_check(animation_name, int):
            animation_name = num_range_check(animation_name, 0, 5)
            display_o.animation_show(animation_name, int(to_stop))
        elif type_check(animation_name, str):
            if animation_name in face_dict:
                display_o.animation_show(face_dict[animation_name], int(to_stop))
            else:
                print_dbg("not found this animation")