import codey
import time
import random
import rocky
import event
import neurons

@event.start
def start_cb():
    codey.display.show("sha")
    while True:
        print(neurons.gyro_sensor.is_shaked())
        time.sleep(0.2)

# @event.button_a_pressed
# def on_button_a__callback():
#     codey.stop_other_scripts()
#     codey.display.show("ax")
#     while True:
#         print(neurons.gyro_sensor.get_acceleration('x'))
#         time.sleep(0.2)

# @event.button_b_pressed
# def on_button_b_callback():
#     codey.stop_other_scripts()
#     codey.display.show("ay")
#     while True:
#         print(neurons.gyro_sensor.get_acceleration('y'))
#         time.sleep(0.2)

# @event.button_c_pressed
# def on_button_c_callback():
#     codey.stop_other_scripts()
#     codey.display.show("az")
#     while True:
#         print(neurons.gyro_sensor.get_acceleration('z'))
#         time.sleep(0.2)

# @event.button_a_pressed
# def on_button_a_callback():
#     codey.stop_other_scripts()
#     codey.display.show("gx")
#     while True:
#         print(neurons.gyro_sensor.get_gyroscope('x'))
#         time.sleep(0.05)

# @event.button_b_pressed
# def on_button_b_callback():
#     codey.stop_other_scripts()
#     codey.display.show("gy")
#     while True:
#         print(neurons.gyro_sensor.get_gyroscope('y'))
#         time.sleep(0.05)

# @event.button_c_pressed
# def on_button_c_callback():
#     codey.stop_other_scripts()
#     codey.display.show("gz")
#     while True:
#         print(neurons.gyro_sensor.get_gyroscope('z'))
#         time.sleep(0.05)

@event.button_a_pressed
def on_button_a_callback():
    codey.stop_other_scripts()
    codey.display.show("pit")
    while True:
        print(neurons.gyro_sensor.get_pitch())
        time.sleep(0.05)

@event.button_b_pressed
def on_button_b_callback():
    codey.stop_other_scripts()
    codey.display.show("rol")
    while True:
        print(neurons.gyro_sensor.get_roll())
        time.sleep(0.05)

@event.button_c_pressed
def on_button_c_callback():
    codey.stop_other_scripts()
    codey.display.show("yaw")
    while True:
        print(neurons.gyro_sensor.get_yaw())
        time.sleep(0.05)