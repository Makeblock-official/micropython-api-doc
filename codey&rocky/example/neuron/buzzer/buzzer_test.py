import codey
import time
import neurons


codey.display.show("hello")

neurons.buzzer.play_note(48, 1)
neurons.buzzer.rest(1)
codey.display.show("note")
codey.display.clear()
neurons.buzzer.play_note("C4", 1)
neurons.buzzer.rest(1)
codey.display.show("C4")
codey.display.clear()
neurons.buzzer.play_tone(1000, 2)
neurons.buzzer.rest(1)
codey.display.show("tone")
codey.display.clear()

while True:
    neurons.buzzer.tempo = 60
    print("tempo:", end = "")
    print(neurons.buzzer.tempo)
    neurons.buzzer.play_note("C4", 1)
    neurons.buzzer.rest(2)
    neurons.buzzer.tempo = 240
    neurons.buzzer.play_note("C4", 1)
    neurons.buzzer.rest(2)