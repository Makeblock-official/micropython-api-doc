import codey
import time

codey.speaker.play_melody("hello", True)
codey.display.show("hello")
codey.display.clear()

codey.speaker.play_note(48, 1)
codey.speaker.rest(1)
codey.display.show("note")
codey.display.clear()
codey.speaker.play_note("C4", 1)
codey.speaker.rest(1)
codey.display.show("C4")
codey.display.clear()
codey.speaker.play_tone(1000, 2)
codey.speaker.rest(1)
codey.display.show("tone")
codey.display.clear()
print("tempo:", end = "")
print(codey.speaker.tempo)
codey.speaker.play_note("C4", 1)
codey.speaker.rest(1)
codey.speaker.tempo = 120
codey.speaker.volume = 20
codey.speaker.play_note("C4", 1)
codey.speaker.rest(1)