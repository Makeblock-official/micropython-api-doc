import codey
import time

while True:
    rotation_x = codey.motion_sensor.get_rotation("x")
    rotation_y = codey.motion_sensor.get_rotation("y")
    rotation_z = codey.motion_sensor.get_rotation("z")
    print("rotation_x:", end = "")
    print(rotation_x, end = "")
    print("   ,rotation_y:", end = "")
    print(rotation_y, end = "")
    print("   ,rotation_z:", end = "")
    print(rotation_z)
    time.sleep(0.05)