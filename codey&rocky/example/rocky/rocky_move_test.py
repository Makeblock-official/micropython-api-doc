import codey
import rocky
import time
import event


rocky.forward(20)
time.sleep(1)
rocky.forward(-20)
time.sleep(1)
rocky.backward(-20)
time.sleep(1)
rocky.backward(20)
time.sleep(1)
rocky.turn_left(20)
time.sleep(1)
rocky.turn_left(-20)
time.sleep(1)
rocky.turn_right(-20)
time.sleep(1)
rocky.turn_right(20)
time.sleep(1)

rocky.forward(20, 1)
rocky.forward(-20, 1)
rocky.backward(-20, 1)
rocky.backward(20, 1)
rocky.turn_left(20, 1)
rocky.turn_left(-20, 1)
rocky.turn_right(-20, 1)
rocky.turn_right(20, 1)

rocky.forward(20, 2, straight = True)
rocky.forward(-20, 2, straight = True)
rocky.backward(-20, 2, straight = True)
rocky.backward(20, 2, straight = True)