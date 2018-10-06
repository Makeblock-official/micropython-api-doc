import codey
import time
import random
import rocky
import event
import neurons

@event.start
def start_cb():
    while True:
        print(neurons.soil_moisture.get_value())
        time.sleep(0.2)
