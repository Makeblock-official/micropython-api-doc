import codey
import rocky
import time
import event

@event.start
def start_cb():
    codey.stop_other_scripts()
    while True:
        codey.display.show(rocky.color_ir_sensor.get_reflected_infrared())

@event.button_a_pressed
def button_a_cb():
    codey.stop_other_scripts()
    while True:
        codey.display.show(rocky.color_ir_sensor.get_light_strength())

@event.button_b_pressed
def button_b_cb():
    codey.stop_other_scripts()
    while True:
        codey.display.show(rocky.color_ir_sensor.get_greyness())


@event.button_c_pressed
def button_c_cb():
    codey.stop_other_scripts()
    while True:
        codey.display.show(rocky.color_ir_sensor.get_reflected_light())
