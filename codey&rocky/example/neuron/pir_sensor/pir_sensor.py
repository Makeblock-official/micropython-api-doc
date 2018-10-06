import codey
import time
import random
import rocky
import event
import neurons

@event.start
def start_cb():
    while True:
        print(neurons.pir_sensor.is_activated())
        time.sleep(0.2)
