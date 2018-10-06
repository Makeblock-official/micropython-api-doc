from codey_global_board import *
from global_object import *
from makeblock import super_var
import math
import time

from driver.button import button as button_t
button_a = button_t(1)
button_b = button_t(2)
button_c = button_t(3)

from driver.battery import battery as battery_t
battery = battery_t()

from driver.display import display as display_t
display = display_t()

from driver.ir import ir as ir_t
ir = ir_t()

from driver.led import led as led_t
led = led_t()

from driver.light_sensor import light_sensor as light_sensor_t
light_sensor = light_sensor_t()

from driver.sound_sensor import sound_sensor as sound_sensor_t
sound_sensor = sound_sensor_t()

from driver.motion_sensor import motion_sensor as motion_sensor_t
motion_sensor = motion_sensor_t()

from driver.potentiometer import potentiometer as potentiometer_t
potentiometer = potentiometer_t()

from driver.speaker import speaker as speaker_t
speaker = speaker_t()

from driver.wifi import wifi as wifi_t
wifi = wifi_t()

# for message advance
def broadcast(sstr, wait = False):    
    time.sleep(0.02)  
    message_o.message_advance(sstr)

# super_var
def set_variable(name, value):
    if type_check(value, int):
        value = int_value_scale(value)

    s_var = super_var(name) 
    if (s_var):
        return s_var.set_value(value) 
    else:
        return False

def get_variable(name):
    g_var = super_var(name)
    if (g_var):
        return g_var.get_value()
    else:
        return None

# stop threads
def stop_this_script():
    stop_threads_o.stop_this_thread()

def stop_other_scripts():
    stop_threads_o.stop_other_threads()

def stop_all_scripts():
    stop_threads_o.stop_all_threads()

# neurons block check
def has_neuron_connected():
    if neurons_engine_o.get_block_num() != 0:
        return True
    else:
        return False

def is_rocky_connected():
    block_num = neurons_engine_o.get_block_num()
    if block_num == 0:
        return False

    info = neurons_engine_o.get_block_info()
    for i in range(block_num):
        if info[i][1 : 3] == [0x63, 0x10]:
            return True
    return False

def get_timer():
    return int(timer_t() * 10) / 10

def reset_timer():
    reset_timer_t()

# debug
def debug_out():
    start_dbg_out()

def stop_debug_out():
    stop_dbg_out()


# reset timer and seed random module
import random
random.seed(int(potentiometer_o.value() + microphone_o.value() + light_o.value()))

reset_timer()