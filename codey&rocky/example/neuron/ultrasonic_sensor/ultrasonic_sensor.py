import codey
import time
import random
import rocky
import event
import neurons

@event.start
def start_cb():
    while True:
        print(neurons.ultrasonic_sensor.get_distance())
        time.sleep(0.2)
