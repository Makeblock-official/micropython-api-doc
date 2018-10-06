from codey_global_board import *
from global_object import rocky_straight_move_o
from global_object import motion_sensor_o
from global_object import neurons_engine_o
import time
import math
#import neurons.neurons_engine_map as neurons_engine_map
ROCKY_TYPE = 0x63
ROCKY_SUBTYPE = 0x10

FUNC_GET_RGB = 0x01
FUNC_GET_COLOR = 0x02
FUNC_GET_LIGHTNESS = 0x03
FUNC_GET_GREY = 0x04
FUNC_GET_LIGHT_REFLECTION = 0x05
FUNC_GET_IR_REFLECTION = 0x06
FUN_IS_IN_GREY = 0x07
FUN_IS_BARRIER = 0x08
FUNC_SET_COLOR = 0x09
FUNC_GET_MOTOR_CURRENT = 0x0a

FUNC_STOP = 0x0C
FUNC_FORWARD = 0x0D
FUNC_BACKWARD = 0x0E
FUNC_RIGHT = 0x0F
FUNC_LEFT = 0x10
FUNC_DRIVE = 0x11

FUNC_LEFT_DIFF = 0x12
FUNC_RIGHT_DIFF = 0x13
FUNC_SINGLE_DRIVE = 0x14


color_dict = {"white": 0, "purple": 1, "red": 2, \
              "orange": 3, "yellow": 4, "green": 5, \
              "cyan":6 , "blue": 7, "pink": 8, \
              "black": 9, "gold": 10 \
             }
# now this varibale just for rotate function
rocky_stop_flag = False
def stop(index = 1):
    global rocky_stop_flag
    rocky_stop_flag = True
    rocky_straight_move_o.set_rocky_straight_move_flag(False);
    rocky_straight_move_o.set_rocky_target_speed(0);
    neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_FORWARD, 0], int(index))

def forward(speed, t = None, straight = False, index = 1):
    if type_check(speed, int, float) and type_check(straight, bool) and type_check(index, int, float) and (type_check(t, int, float) or t == None):
        if type_check(t, int, float):
           if t <= 0:
               return
        speed = num_range_check(speed, -100, 100)

        if(straight == False):
            rocky_straight_move_o.set_rocky_straight_move_flag(False);
            if speed < 0:
                # neu.neu_send("ROCKY","back", [-speed], int(index))
                neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_BACKWARD, -speed], int(index))
            else:
                # neu.neu_send("ROCKY","forward", [speed], int(index))
                neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_FORWARD, speed], int(index))
        else:
            if(speed == 0):
                rocky_straight_move_o.set_rocky_straight_move_flag(False);
                rocky_straight_move_o.set_rocky_target_speed(0);
            else:
                rocky_straight_move_o.set_rocky_target_speed(speed);
                rocky_straight_move_o.init_rocky_angle();
                rocky_straight_move_o.set_rocky_straight_move_flag(True);
        if t != None:
            time.sleep(t)
            stop()
            if (straight == True):
                rocky_straight_move_o.set_rocky_straight_move_flag(False);

def backward(speed, t = None, straight = False, index = 1):
    if type_check(speed, int, float) and type_check(straight, bool) and type_check(index, int, float) and (type_check(t, int, float) or t == None):
        if type_check(t, int, float):
           if t <= 0:
               return
        speed = num_range_check(speed, -100, 100)

        if(straight == False):
            rocky_straight_move_o.set_rocky_straight_move_flag(False);
            if speed < 0:
                # neu.neu_send("ROCKY","forward", [-speed], int(index))
                neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_FORWARD, -speed], int(index))
            else:
                # neu.neu_send("ROCKY","back", [speed], int(index))
                neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_BACKWARD, speed], int(index))
        else:
            if(speed == 0):
                rocky_straight_move_o.set_rocky_straight_move_flag(False);
                rocky_straight_move_o.set_rocky_target_speed(0);
            else:
                rocky_straight_move_o.set_rocky_target_speed(-speed);
                rocky_straight_move_o.init_rocky_angle();
                rocky_straight_move_o.set_rocky_straight_move_flag(True);
        if t != None:
            time.sleep(t)
            stop()
            if (straight == True):
                rocky_straight_move_o.set_rocky_straight_move_flag(False);

def turn_left(speed, t = None, index = 1):
    if type_check(speed, int, float) and type_check(index, int, float) and (type_check(t, int, float) or t == None):
        if type_check(t, int, float):
           if t <= 0:
               return
        speed = num_range_check(speed, -100, 100)
        if speed < 0:
            # neu.neu_send("ROCKY", "right", [-speed], int(index))
            neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_RIGHT, -speed], int(index))
        else:
            # neu.neu_send("ROCKY","left", [speed], int(index))
            neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_LEFT, speed], int(index))
        if t != None:
            time.sleep(t)
            stop()

def turn_right(speed, t = None, index = 1):
    if type_check(speed, int, float) and type_check(index, int, float) and (type_check(t, int, float) or t == None):
        if type_check(t, int, float):
           if t <= 0:
               return
        speed = int(num_range_check(speed, -100, 100))
        if speed < 0:
            # neu.neu_send("ROCKY", "left", [-speed], int(index))
            neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_LEFT, -speed], int(index))
        else:
            # neu.neu_send("ROCKY","right", [speed], int(index))
            neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_RIGHT, speed], int(index))
        if t != None:
            time.sleep(t)
            stop()

def drive(left_power, right_power, index = 1): # not support now
    if (not type_check(left_power, int, float)) or (not type_check(right_power, int, float)):
        return
    if left_power < 0:
        left_dir = 1
        left_power = -left_power
    else:
        left_dir = 0

    if right_power < 0:
        right_dir = 0
        right_power = -right_power
    else:
        right_dir = 1
    left_power = num_range_check(left_power, -100, 100)
    right_power = num_range_check(right_power, -100, 100)    
    # neu.neu_send("ROCKY","drive", [left_dir, left_power, right_dir, right_power], int(index))
    neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_DRIVE, left_dir, left_power, right_dir, right_power], int(index))

## test rocky turn a fixed angle
def turn_right_by_degree(angle, speed = 40, index = 1):
    global rocky_stop_flag
    if (not type_check(angle, int, float)) or (not type_check(speed, int, float)):
        return
    if angle < 0:
        turn_left_by_degree(-angle, speed)
        return
    speed = math.fabs(speed)
    angle_a = 50
    now_angle = motion_sensor_o.get_attitude(2)
    turn_angle = angle * math.cos(angle_a / 180 * 3.1415926)
    dis_angle = now_angle - turn_angle

    rocky_stop_flag = False
    while True: 
        delt = motion_sensor_o.get_attitude(2) - dis_angle
        if delt >= 5:
            drive(speed, -speed)
        if delt < 5 and delt > 2:
            drive(speed * 0.5, -speed * 0.5)
        elif delt < 1:
            break
        if rocky_stop_flag:
            rocky_stop_flag = False
            break
    drive(0, 0)

def turn_left_by_degree(angle, speed = 40, index = 1):
    global rocky_stop_flag
    if (not type_check(angle, int, float)) or (not type_check(speed, int, float)):
        return
    if angle < 0:
        turn_right_by_degree(-angle, speed)
        return
    speed = math.fabs(speed)
    angle_a = 50 
    now_angle = motion_sensor_o.get_attitude(2)
    turn_angle = angle * math.cos(angle_a / 180 * 3.1415926)
    dis_angle = now_angle + turn_angle

    rocky_stop_flag = False
    while True: 
        delt = motion_sensor_o.get_attitude(2) - dis_angle
        if delt <= -5:
            drive(-speed, speed)
        if delt > -5 and delt < -2:
            drive(-speed * 0.5, speed * 0.5)
        elif delt > -1:
            break
        if rocky_stop_flag:
            rocky_stop_flag = False
            break
    drive(0, 0)

class color_ir_sensor():
    def __init__(self):
        pass

    def get_red(self, index = 1):
        # ret = neu.neu_read("ROCKY", "val_rgb", [], int(index))
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_RGB], int(index))
        if(ret == None):
            print_dbg("rgb command received none")
            return 0
        else:
            return ret[0]

    def get_green(self, index = 1):
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_RGB], int(index))
        if(ret == None):
            return 0
        else:
            return ret[1]

    def get_blue(self, index = 1):
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_RGB], int(index))
        if(ret == None):
            return 0
        else:
            return ret[2]

    # this function is baed on function color
    # don't use a indepedend id
    def is_color(self, color_str, index = 1):
        color_id = -1
        if color_str in color_dict:
            color_id = color_dict[color_str]
        else:
            print_dbg("not found the color", color_str)
            return False

        # ret == neu.neu_read("ROCKY", "color", [], int(index)):
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_COLOR], int(index))
        if color_id  == ret[0]:
            return True
        else:
            return False

    def get_light_strength(self, index = 1):
        # ret = neu.neu_read("ROCKY", "val_lightness", [], int(index))
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_LIGHTNESS], int(index))      
        if ret != None:
            return ret[0]
        else:
            return 0
        
    def get_greyness(self, index = 1):
        # ret = neu.neu_read("ROCKY", "val_grey", [], int(index))
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_GREY], int(index))              
        if ret != None:
            return ret[0]
        else:
            return 0

    def get_reflected_light(self, index = 1):
        # ret = neu.neu_read("ROCKY", "val_light_reflect", [], int(index))
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_LIGHT_REFLECTION], int(index)) 
        if ret != None:
            return ret[0]
        else:
            return 0

    def get_reflected_infrared(self, index = 1):
        # ret = neu.neu_read("ROCKY", "val_ir_reflect", [], int(index))
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_IR_REFLECTION], int(index)) 
        if ret != None:
            return ret[0]
        else:
            return 0

    def is_obstacle_ahead(self, index = 1):
        # ret = neu.neu_read("ROCKY", "is_barrier", [], int(index))
        ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUN_IS_BARRIER], int(index)) 
        if ret[0] == 1:
            return True
        else:
            return False

    def set_led_color(self, color_name, index = 1):
        dict = {"red":[1,0,0], "green":[0,1,0], "blue":[0,0,1],\
                "yellow":[1,1,0], "purple":[1,0,1], "cyan":[0,1,1],\
                "white":[1,1,1], "black":[0,0,0]
                }
        if not type_check(color_name, str):
            return
        if color_name in dict:
            val = dict[color_name]
            # neu.neu_send("ROCKY", "set_rgb", val, int(index)) 
            ret = neurons_engine_o.send(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_SET_COLOR] + val, int(index)) 
                
# just for a temporary usage
def verify_color_sensor():
    neurons_engine_o.send_special(0xf0, 0xff, 0x63, 0x10, 0x6f, 0x61, 0xf7)

def get_motor_current(direc, index = 1):
    # ret = neu.neu_read("ROCKY", "val_motor_current", 1, [])
    ret = neurons_engine_o.read(ROCKY_TYPE, ROCKY_SUBTYPE, [FUNC_GET_MOTOR_CURRENT], int(index)) 
    if ret != None:
        if direc == 'left':
            return ret[0]
        elif direc == 'right':
            return ret[1]
        else:
            return 0
    else:
        return 0

# make color ir sensor a seperate module
color_ir_sensor = color_ir_sensor()