import codey
import rocky
import time
import event

@event.start
def start_cb():
    print("start event successed")
    while True:
        codey.display.show(codey.ir.receive_remote_code()[1])
