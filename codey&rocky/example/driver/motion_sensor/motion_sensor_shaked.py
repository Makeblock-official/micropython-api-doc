import codey
import time

while True:
    if codey.motion_sensor.is_shaked():
        print("shake_strength:", end = "")
        print(codey.motion_sensor.get_shake_strength())