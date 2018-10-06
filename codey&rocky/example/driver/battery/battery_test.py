import codey
import time

while True:
    print("voltage:")
    print(codey.battery.get_voltage())
    print("percentage:")
    print(codey.battery.get_percentage())
    time.sleep(1)