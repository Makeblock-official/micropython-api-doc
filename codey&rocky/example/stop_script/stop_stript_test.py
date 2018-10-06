import codey
import rocky
import time
import event

@event.start
def start_cb():
    while True:
        print("start cb executing...")
        time.sleep(1)
        print("stop this script")
        codey.stop_this_script()

@event.button_a_pressed
def button_a_cb():
    codey.stop_other_scripts()
    while True:
        print("button a event")

@event.button_b_pressed
def button_b_cb():
    codey.stop_other_scripts()
    while True:
        print("button b event")

@event.button_c_pressed
def button_c_cb():
    codey.stop_all_scripts()

