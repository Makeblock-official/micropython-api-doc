import codey
import event

def loop():
    while True:
        if codey.button_a.is_pressed():
            print("button A is pressed")
        if codey.button_b.is_pressed():
            print("button B is pressed")
        if codey.button_c.is_pressed():
            print("button C is pressed")

@event.start
def start_callback():
    loop()