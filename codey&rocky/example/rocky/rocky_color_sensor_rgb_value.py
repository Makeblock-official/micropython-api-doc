import codey
import rocky
import time
import event


@event.button_a_pressed
def button_a_cb():
    while True:
        print("red: ", rocky.color_ir_sensor.get_red())
        print("green: ", rocky.color_ir_sensor.get_green())
        print("blue: ", rocky.color_ir_sensor.get_blue())
        print("")
        time.sleep(0.1)