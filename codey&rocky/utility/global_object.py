# makeblock lib import
from makeblock import button_board
from makeblock import light_sensor_board
from makeblock import sound_sensor_board
from makeblock import potentiometer_board
from makeblock import gyro_board
from makeblock import music
from makeblock import rmt_board
from makeblock import rgbled_board
from makeblock import ledmatrix

from makeblock import ir_learning
from makeblock import battery_check
from makeblock import neurons_engine
from makeblock import super_var
from makeblock import message_board
from makeblock import codey_eve
from makeblock import wlan
from makeblock import hardware_version
from makeblock import stop_threads
from makeblock import rocky_straight_move
from makeblock import ble_controller
from makeblock import calibration_fun

from makeblock import online

# the two modules below are functions, not classes 
from makeblock import timer_t
from makeblock import reset_timer_t

button_o = button_board()
light_o = light_sensor_board()
potentiometer_o = potentiometer_board()
microphone_o = sound_sensor_board()
motion_sensor_o = gyro_board()
speaker_o = music()
infrared_o = rmt_board()
ir_learning_o = ir_learning()
led_o = rgbled_board()
display_o = ledmatrix()

battery_o = battery_check()
neurons_engine_o = neurons_engine()
message_o = message_board()
event_complement_o = codey_eve()
wlan_o = wlan()
hardware_version_o = hardware_version()
stop_threads_o = stop_threads()
rocky_straight_move_o = rocky_straight_move()
ble_controller_o = ble_controller()
calibration_fun_o = calibration_fun()

online_o = online()