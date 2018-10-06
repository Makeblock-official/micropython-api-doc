import codey
import rocky
import time
import event

@event.start
def start_cb():
    codey.stop_other_scripts()
    while True:
        codey.display.show(rocky.color_ir_sensor.is_obstacle_ahead())

@event.button_a_pressed
def button_a_cb():
    rocky.color_ir_sensor.set_led_color("red")
    time.sleep(1)
    rocky.color_ir_sensor.set_led_color("green")
    time.sleep(1)
    rocky.color_ir_sensor.set_led_color("blue")
    time.sleep(1)    
    rocky.color_ir_sensor.set_led_color("yellow")
    time.sleep(1)
    rocky.color_ir_sensor.set_led_color("purple")
    time.sleep(1)
    rocky.color_ir_sensor.set_led_color("cyan")
    time.sleep(1)
    rocky.color_ir_sensor.set_led_color("white")
    time.sleep(1)
    rocky.color_ir_sensor.set_led_color("black")
