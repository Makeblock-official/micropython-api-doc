import codey
import time

while True:
    acceleration_x = codey.motion_sensor.get_acceleration("x")
    acceleration_y = codey.motion_sensor.get_acceleration("y")
    acceleration_z = codey.motion_sensor.get_acceleration("z")
    print("acceleration_x:", end = "")
    print(acceleration_x, end = "")
    print("   ,acceleration_y:", end = "")
    print(acceleration_y, end = "")
    print("   ,acceleration_z:", end = "")
    print(acceleration_z)
    time.sleep(0.05)