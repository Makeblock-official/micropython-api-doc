import codey
import time

codey.display.show("ffffff")
codey.display.show("123")
time.sleep(1)
codey.display.show("12345", 3, 1)
codey.display.set_pixel(True, 1, 1)
image = "ffffffffff000000000000000000000000"
codey.display.show_image(image, pos_x = 3, pos_y = 4)
time.sleep(1)
codey.display.clear()
codey.display.animation(1, True)
print("[1, 1]:", codey.display.get_pixel(1, 1))
codey.display.show("12:28")
while True:
    codey.display.toggle_pixel(7, 2)
    codey.display.toggle_pixel(7, 4)
    time.sleep(1)