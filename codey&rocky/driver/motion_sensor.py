from codey_global_board import *
from global_object import motion_sensor_o

PITCH_ID = 1
YAW_ID = 2
ROLL_ID = 3

AXIS_X_ID = 2
AXIS_Y_ID = 1
AXIS_Z_ID = 3

TILE_LEFT_ID = 1
TILE_RIGHT_ID = 2
TILT_EARS_DOWN_ID = 3
TILT_EARS_UP_ID = 4

SCREEN_UP_ID = 0
SCREEN_DOWN_ID = 1 
UPRIGHT_ID = 2

class motion_sensor():
    def __init__(self):
        pass

    def get_roll(self):
        ret = motion_sensor_o.get_attitude(ROLL_ID)
        return round(int(ret))

    def get_pitch(self):
        ret = motion_sensor_o.get_attitude(PITCH_ID)
        return round(int(ret))

    def get_yaw(self):
        ret = motion_sensor_o.get_attitude(YAW_ID)
        while ret < 0:
            ret = ret + 360
        while ret > 360:
            ret = ret % 360 
        return round(int(ret))

    def get_rotation(self, axis):
        axis_index = 0
        if type_check(axis, str):
            if axis == 'x':
                axis_index = AXIS_X_ID
            elif axis == 'y':
                axis_index = AXIS_Y_ID
            elif axis == 'z':
                axis_index = AXIS_Z_ID
            else:
                return 0
        elif type_check(axis, int):
            axis_index = axis
            if axis_index > 3:
                return 0

        # to 0 - 360
        ret = motion_sensor_o.get_rotation(axis_index)
        return round(int(ret))

    def reset_rotation(self, axis = "all"):
        axis_index = 0
        if type_check(axis, str):
            if axis == 'x':
                axis_index = AXIS_X_ID
            elif axis == 'y':
                axis_index = AXIS_Y_ID
            elif axis == 'z':
                axis_index = AXIS_Z_ID
            elif axis == "all":
                axis_index = 255
            else:
                return
        motion_sensor_o.reset_rotate_angle(axis_index)

    def is_shaked(self):
        if motion_sensor_o.is_shaked():
            return True
        else:
            return False

    def get_shake_strength(self):
        strength = motion_sensor_o.shake_strength()
        strength = num_range_check(strength, 0, 100)
        return strength

    def is_tilted_left(self):
        ret = motion_sensor_o.tilt()
        if ret & (1 << TILE_LEFT_ID):
            return True
        else:
            return False

    def is_tilted_right(self):
        ret = motion_sensor_o.tilt()
        if ret & (1 << TILE_RIGHT_ID):
            return True
        else:
            return False

    def is_ears_up(self):
        ret = motion_sensor_o.tilt()
        if ret & (1 << TILT_EARS_UP_ID):
            return True
        else:
            return False

    def is_ears_down(self):
        ret = motion_sensor_o.tilt()
        if ret & (1 << TILT_EARS_DOWN_ID):
            return True
        else:
            return False

    def is_display_up(self):
        ret = motion_sensor_o.screen_orientation()
        if ret & (1 << SCREEN_UP_ID):
            return True
        else:
            return False

    def is_display_down(self):
        ret = motion_sensor_o.screen_orientation()
        if ret & (1 << SCREEN_DOWN_ID):
            return True
        else:
            return False

    def is_upright(self):
        ret = motion_sensor_o.screen_orientation()
        if ret & (1 << UPRIGHT_ID):
            return True
        else:
            return False

    def get_acceleration(self, axis):
        axis_index = 0
        sign = 1
        if type_check(axis, str):
            if axis == 'x':
                axis_index = AXIS_X_ID
                sign = 1
            elif axis == 'y':
                axis_index = AXIS_Y_ID
                sign = -1
            elif axis == 'z':
                axis_index = AXIS_Z_ID
                sign = -1
            else:
                return 0
        elif type_check(axis, int):
            axis_index = num_range_check(axis, 1, 3)
        else:
            return 0
            
        temp_value = motion_sensor_o.get_raw_data()

        return sign * int(temp_value[axis_index - 1] * 0.98) / 10  # make the value only one number after point

    def get_gyroscope(self, axis):
        axis_index = 0
        sign = 1
        if type_check(axis, str):
            if axis == 'x':
                axis_index = AXIS_X_ID
                sign = -1
            elif axis == 'y':
                axis_index = AXIS_Y_ID
                sign = 1
            elif axis == 'z':
                axis_index = AXIS_Z_ID
                sign = 1
            else:
                return 0
        elif type_check(axis, int):
            axis_index = num_range_check(axis, 1, 3)
        else:
            return 0
        
        temp_value = motion_sensor_o.get_raw_data()
        return sign * int(temp_value[3 + axis_index - 1])