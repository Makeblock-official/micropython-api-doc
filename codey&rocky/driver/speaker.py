from global_object import speaker_o
from codey_global_board import *
import time

DEFAULT_TEMPO = 60

class speaker():
    def __init__(self):
        self.tempo_value = DEFAULT_TEMPO

    def stop_sounds(self):
        speaker_o.stop_all()
    
    def set_volume(self, value):
        if not type_check(value, int, float):
            return
        value = num_range_check(value, 0, 100)
        speaker_o.set_volume(value) 

    def get_volume(self):
        return round(speaker_o.get_volume())

    def change_volume(self, value):
        speaker_o.change_volume(value)

    @property
    def volume(self):
        return self.get_volume()

    @volume.setter
    def volume(self, value):
        self.set_volume(value)

    def set_tempo(self, value):
        if not type_check(value, int, float):
            return
        value = num_range_check(value, 6, 600)  
        self.tempo_value = value

    def change_tempo(self, value):
        if not type_check(value, int, float):
            return
        value = self.tempo_value + value 
        value = num_range_check(value, 6, 600)  
        self.tempo_value = value

    def get_tempo(self):
        return round(self.tempo_value)

    @property
    def tempo(self):
        return self.get_tempo()

    @tempo.setter
    def tempo(self, value):
        self.set_tempo(value)

    def play_melody(self, sound_name, wait = False, off_t = 0.05):
        if not type_check(sound_name, str):
            return

        if sound_name[-4 : ] != ".wav":
            sound_name_t = sound_name + ".wav"
        else:
            sound_name_t = sound_name
        if not wait:
            speaker_o.play(sound_name_t)
            if off_t != None:
                time.sleep(off_t) 
        else:
            speaker_o.play_to_stop(sound_name_t)

    def play_melody_until_done(self, sound_name, wait = True, off_t = 0.05):
        self.play_melody(sound_name, wait, off_t)

    def play_note(self, note, beat = None):
        if (not type_check(beat, int, float)) and beat != None:
            return
        if beat != None:
            if beat <= 0:
                self.stop_sounds()
                return

        if type_check(note, int, float):
            if note <= 0:
                return
            note = num_range_check(note, 0, 127) 

            freq = MIDI_NOTE_NUM0 * pow(NOTE_FREQUENCE_RATIO, note)

        elif type_check(note, str):
            if note in node_table:
                freq = node_table[note]
            else:
                print_dbg("not found the node", note)
                return
        if beat == None:
            speaker_o.play_note(int(freq), 3600 * 1000)
        else:
            speaker_o.play_note_to_stop(int(freq), int(beat * (60 / self.tempo_value) * 1000)) # to ms


    def play_tone(self, frequency, time_ms = None):
        if type_check(frequency, int, float) and (time_ms == None or type_check(time_ms, int, float)):
            if frequency <= 0:
                self.stop_sounds()
                return
            if time_ms != None:
                if time_ms <= 0:
                    self.stop_sounds()
                    return

            frequency = num_range_check(frequency, 0, 5000) 
            if time_ms == None:
                speaker_o.play_note(int(frequency), 3600 * 1000)
            else:
                speaker_o.play_note_to_stop(int(frequency), int(time_ms * 1000)) 

    def rest(self, beat):
        if not type_check(beat, int, float):
            return 
        time.sleep(beat * (60 / self.tempo_value))