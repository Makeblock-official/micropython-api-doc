import codey
import rocky
import time
import event

@event.start
def start_cb():
    print("start event successed")
    while True:
        codey.display.show(codey.ir.receive())

# @event.button_a_pressed
# def button_a_cb():
#     print("button a event successed")
#     codey.ir.start_learning()
#     codey.led.show(100, 0, 0)

# @event.button_b_pressed
# def button_b_cb():
#     print("button b event successed")
#     codey.ir.stop_learning()
#     codey.ir.save_learned_result(2)
#     codey.led.show(0, 100, 0)


# @event.button_c_pressed
# def button_c_cb():
#     print("button c event successed")
#     codey.ir.send_learned_result(1)

@event.button_a_pressed
def button_a_cb():
    print("button a event successed")
    codey.ir.send_learned_result(1)

@event.button_b_pressed
def button_b_cb():
    print("button b event successed")
    codey.ir.send_learned_result(2)
