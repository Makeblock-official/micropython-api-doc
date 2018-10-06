import codey
import time
import random
import rocky
import event
import neurons

@event.start
def start_cb():
    while True:
        if neurons.funny_touch.is_blue_touched():
            print("blue touched")
        if neurons.funny_touch.is_red_touched():
            print("red touched")
        if neurons.funny_touch.is_green_touched():
            print("green touched")
        if neurons.funny_touch.is_yellow_touched():
            print("yellow touched")
        
        time.sleep(0.1)
