import codey
import rocky
import time
import event

# @event.button_a_pressed
# def button_a_cb():
#     print("button a event successed")
#     codey.broadcast('hello')

# @event.button_b_pressed
# def button_b_cb():
#     print("button b event successed")

# @event.button_c_pressed
# def button_c_cb():
#     print("button c event successed")

# @event.start
# def start_cb():
#     print("start event successed")

# @event.shaked
# def shaked_cb():
#     print("shaked event successed")

# @event.received("hello")
# def received_cb():
#     print("broadcast received event successed")

# @event.tilted_left
# def tilted_left_cb():
#     print("tilted left event successed")

# @event.tilted_right
# def tilted_right_cb():
#     print("tilted right event successed")

# @event.ears_up
# def ears_up_cb():
#     print("ears up event successed")

# @event.ears_down
# def ears_down_cb():
#     print("ears down event successed")

# @event.ir_received("hello")
# def ir_received_cb():
#     print("ir received event successed")

@event.greater_than(20, "sound_sensor")
def sound_sensor_cb():
    print("sound sensor greater event successed")

@event.greater_than(5, "timer")
def timer_cb():
    print("timer greater event successed")

@event.less_than(30, "light_sensor")
def light_sensor_cb():
    print("light sensor event successed")