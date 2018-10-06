import codey
import rocky
import time
import event


@event.button_a_pressed
def button_a_cb():
    print("button a event successed")
    codey.ir.learn()
    codey.led.show(0, 100, 0)

@event.button_b_pressed
def button_a_cb():
    print("button b event successed")
    while True:
        codey.ir.send_learned_result()

@event.button_c_pressed
def button_c_cb():
    print("button b event successed")
    while True:
        codey.display.show(codey.ir.receive())