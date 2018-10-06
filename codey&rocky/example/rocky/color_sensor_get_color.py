import codey
import rocky
import time
import event

@event.button_a_pressed
def button_a_cb():
    while True:
        if rocky.color_ir_sensor.is_color("red"):
            codey.led.show(100, 0, 0)
        elif rocky.color_ir_sensor.is_color("green"):
            codey.led.show(0, 100, 0)
        elif rocky.color_ir_sensor.is_color("blue"):
            codey.led.show(0, 0, 100)
        elif rocky.color_ir_sensor.is_color("yellow"):
            codey.led.show(100, 100, 0)
        elif rocky.color_ir_sensor.is_color("purple"):
            codey.led.show(100, 0, 100)
        elif rocky.color_ir_sensor.is_color("cyan"):
            codey.led.show(0, 100, 100)
        elif rocky.color_ir_sensor.is_color("white"):
            codey.led.show(100, 100, 100)
        elif rocky.color_ir_sensor.is_color("black"):
            codey.led.show(0, 0, 0)