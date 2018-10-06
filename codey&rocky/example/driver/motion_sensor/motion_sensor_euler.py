import codey
import time

while True:
    roll = codey.motion_sensor.get_roll()
    pitch = codey.motion_sensor.get_pitch()
    yaw = codey.motion_sensor.get_yaw()
    print("roll:", end = "")
    print(roll, end = "")
    print("   ,pitch:", end = "")
    print(pitch, end = "")
    print("   ,yaw:", end = "")
    print(yaw)
    time.sleep(0.05)