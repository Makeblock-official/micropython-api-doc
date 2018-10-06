import codey
import time

while True:
    gyroscope_x = codey.motion_sensor.get_gyroscope("x")
    gyroscope_y = codey.motion_sensor.get_gyroscope("y")
    gyroscope_z = codey.motion_sensor.get_gyroscope("z")
    print("gyroscope_x:", end = "")
    print(gyroscope_x, end = "")
    print("   ,gyroscope_y:", end = "")
    print(gyroscope_y, end = "")
    print("   ,gyroscope_z:", end = "")
    print(gyroscope_z)
    time.sleep(0.05)