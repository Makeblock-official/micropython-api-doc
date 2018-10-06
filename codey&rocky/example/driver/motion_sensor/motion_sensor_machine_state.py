import codey
import time

while True:
    if codey.motion_sensor.is_tilted_left():
        print("tilted_left")
    if codey.motion_sensor.is_tilted_right():
        print("tilted_right")
    if codey.motion_sensor.is_ears_up():
        print("ears_up")
    if codey.motion_sensor.is_ears_down():
        print("ears_down")
    if codey.motion_sensor.is_display_up():
        print("display_up")
    if codey.motion_sensor.is_display_down():
        print("display_down")
    if codey.motion_sensor.is_upright():
        print("upright")