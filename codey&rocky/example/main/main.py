import codey
import time
import random
import rocky
import event

rage = 0
t = 0
@event.start
def on_start_callback():
    global rage, t
    rage = 0
    t = 0.02
    codey.display.show_image('00000808080800000000080808080000')
    time.sleep(1)
    codey.display.show_image('00001018181000000000101818100000')
    time.sleep(1)
    codey.display.show_image('00000808080800000000080808080000')
    time.sleep(0.5)
    codey.display.show_image('00001018181000000000101818100000')
    time.sleep(float(t))
    codey.display.show_image('0000181c1c1800000000181c1c180000')
    time.sleep(float(t))
    codey.display.show_image('0000181c1c1800000000181c1c180000')
    time.sleep(float(t))
    codey.display.show_image('0000183c3c1800000000183c3c180000')
    time.sleep(float(t))
    codey.display.show_image('00001c3e3e1c000000001c3e3e1c0000')
    time.sleep(float(t))
    while True:
        codey.display.show_image('00003c7e7e3c000000003c7e7e3c0000')
        for count in range(int(random.randint(200, 600))):
            time.sleep(0.01)

        codey.display.show_image('0000181c1c1800000000181c1c180000')
        for count2 in range(int(random.randint(0, 5))):
            time.sleep(0.01)

        codey.display.show_image('00000808080800000000080808080000')
        for count3 in range(int(random.randint(10, 30))):
            time.sleep(0.01)

        codey.display.show_image('0000183c3c1800000000183c3c180000')
        for count4 in range(int(random.randint(0, 5))):
            time.sleep(0.01)

@event.button_a_pressed
def on_button_callback():
    global rage, t
    if rage > random.randint(3, 5):
        rage = 0
        time.sleep(0.5)
        codey.display.show_image('00003c1e0e0400000000040e1e3c0000')
        rocky.backward(20, 0.4)
        rocky.backward(100, 0.01)
        rocky.forward(100, 0.2)
        rocky.backward(100, 0.01)
        time.sleep(0.1)
        codey.speaker.play_melody('angry.wav')
        time.sleep(0.5)
        codey.display.show_image('00003c7e7e3c000000003c7e7e3c0000')

    else:
        time.sleep(0.4)
        codey.display.show_image('000c18181c0c000000000c1c18180c00')
        codey.speaker.play_melody('laugh.wav')
        rocky.turn_left(70, 0.05)
        codey.display.show_image('00183030381800000000183830301800')
        rocky.turn_right(70, 0.05)
        codey.display.show_image('000c18181c0c000000000c1c18180c00')
        rocky.turn_left(70, 0.05)
        rocky.turn_right(70, 0.05)
        time.sleep(0.3)
        codey.display.show_image('00183030381800000000183830301800')
        time.sleep(0.1)
        codey.display.show_image('00003c7e7e3c000000003c7e7e3c0000')
        rage = (rage if isinstance(rage, int) or isinstance(rage, float) else 0) + 1

@event.button_b_pressed
def on_button1_callback():
    global rage, t
    if rage > random.randint(3, 5):
        rage = 0
        time.sleep(0.5)
        codey.display.show_image('00003c1e0e0400000000040e1e3c0000')
        rocky.backward(20, 0.4)
        rocky.backward(100, 0.01)
        rocky.forward(100, 0.2)
        rocky.backward(100, 0.01)
        time.sleep(0.1)
        codey.speaker.play_melody('angry.wav')
        time.sleep(0.5)
        codey.display.show_image('00003c7e7e3c000000003c7e7e3c0000')

    else:
        time.sleep(0.4)
        codey.display.show_image('000c18181c0c000000000c1c18180c00')
        codey.speaker.play_melody('laugh.wav')
        rocky.turn_right(70, 0.05)
        codey.display.show_image('00183030381800000000183830301800')
        rocky.turn_left(70, 0.05)
        codey.display.show_image('000c18181c0c000000000c1c18180c00')
        rocky.turn_right(70, 0.05)
        rocky.turn_left(70, 0.05)
        time.sleep(0.3)
        codey.display.show_image('00183030381800000000183830301800')
        time.sleep(0.1)
        codey.display.show_image('00003c7e7e3c000000003c7e7e3c0000')
        rage = (rage if isinstance(rage, int) or isinstance(rage, float) else 0) + 1

@event.button_c_pressed
def on_button2_callback():
    global rage, t
    if rage > random.randint(3, 5):
        rage = 0
        time.sleep(0.5)
        codey.display.show_image('00003c1e0e0400000000040e1e3c0000')
        rocky.backward(20, 0.4)
        rocky.backward(100, 0.01)
        rocky.forward(100, 0.2)
        rocky.backward(100, 0.01)
        time.sleep(0.1)
        codey.speaker.play_melody('angry.wav')
        time.sleep(0.5)
        codey.display.show_image('00003c7e7e3c000000003c7e7e3c0000')

    else:
        time.sleep(0.5)
        codey.display.show_image('00081c3c3c3820000020383c3c1c0800')
        time.sleep(0.5)
        codey.speaker.play_melody('sad.wav')
        codey.display.show_image('00040e1e1e1c100000101c1e1e0e0400')
        rocky.backward(50, 0.1)
        codey.display.show_image('00081c3c3c3820000020383c3c1c0800')
        time.sleep(0.3)
        codey.display.show_image('00183c3c7c7820000020787c3c3c1800')
        time.sleep(0.1)
        codey.display.show_image('00003c7e7e3c000000003c7e7e3c0000')
        rage = (rage if isinstance(rage, int) or isinstance(rage, float) else 0) + 2


