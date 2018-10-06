import codey
import time

codey.led.show(2555,255,255)
time.sleep(2)
codey.led.off()
time.sleep(2)
while True:
    codey.led.set_red(255)
    time.sleep(1)
    codey.led.set_green(255)
    time.sleep(1)
    codey.led.set_blue(255)
    time.sleep(1)
    codey.led.off()
    time.sleep(1)