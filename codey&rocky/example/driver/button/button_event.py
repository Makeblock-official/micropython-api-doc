import codey
import event

@event.button_a_pressed
def on_button_a_pressed():
    print("button A is pressed")

@event.button_b_pressed
def on_button_b_pressed():
    print("button B is pressed")

@event.button_c_pressed
def on_button_c_pressed():
    print("button C is pressed")