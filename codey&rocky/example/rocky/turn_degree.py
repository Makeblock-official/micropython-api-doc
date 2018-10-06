import codey
import rocky
import time
import event


@event.button_a_pressed
def button_a_cb():
    rocky.turn_right_by_degree(90)
    time.sleep(2)
    rocky.turn_right_by_degree(-90)

@event.button_b_pressed
def button_b_cb():
    rocky.turn_right_by_degree(90, 80)
    time.sleep(2)
    rocky.turn_right_by_degree(-90, 80)

@event.greater_than(50, "sound_sensor")
def sound_greater_cb():
    rocky.turn_right_by_degree(90)
    time.sleep(2)
    rocky.turn_right_by_degree(-90)
