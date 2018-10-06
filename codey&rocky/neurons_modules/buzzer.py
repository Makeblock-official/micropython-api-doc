from global_object import neurons_engine_o
from codey_global_board import *
import time
import math

BUZZER_TYPE = 0x66
BUZZER_SUBTYPE = 0x02

BUZZER_PLAY = 0x01

class buzzer():
    def __init__(self):
        self.note_tempo = 60

    def __off(self, index = 1):
        neurons_engine_o.send(BUZZER_TYPE, BUZZER_SUBTYPE, [BUZZER_PLAY, 0, 0], int(index))
    
    def play_tone(self, frequency, beat = None, index = 1, duty = 50):
        if type_check(frequency, int, float) and ( beat == None or type_check(beat, int, float)):
            if frequency <= 0:
                self.__off()
                return
            if beat != None:
                if beat <= 0:
                    self.__off()
                    return
    
        frequency = num_range_check(frequency, 0, 5000)
        if beat == None:
            neurons_engine_o.send(BUZZER_TYPE, BUZZER_SUBTYPE, [BUZZER_PLAY, frequency, duty], int(index))
        else:
            neurons_engine_o.send(BUZZER_TYPE, BUZZER_SUBTYPE, [BUZZER_PLAY, frequency, duty], int(index))
            time.sleep(beat * (60 / self.note_tempo))
            neurons_engine_o.send(BUZZER_TYPE, BUZZER_SUBTYPE, [BUZZER_PLAY, 0, 0], int(index))
    
    def play_note(self, note, beat = None, index = 1):
        if (not type_check(beat, int, float)) and beat != None:
            return
        if beat != None:
            if beat <= 0:
                self.__off()
                return
    
        if type_check(note, int, float):
            if note <= 0:
                return
            note = num_range_check(note, 0, 127) 
    
            freq = MIDI_NOTE_NUM0 * math.pow(NOTE_FREQUENCE_RATIO, note)
    
        elif type_check(note, str):
            if note in node_table:
                freq = node_table[note]
            else:
                print_dbg("not found the node", note)
                return
    
        if beat == None:
            neurons_engine_o.send(BUZZER_TYPE, BUZZER_SUBTYPE, [BUZZER_PLAY, freq, 50], int(index))
        else:
            neurons_engine_o.send(BUZZER_TYPE, BUZZER_SUBTYPE, [BUZZER_PLAY, freq, 50], int(index))
            time.sleep(beat * (60 / self.note_tempo))
            neurons_engine_o.send(BUZZER_TYPE, BUZZER_SUBTYPE, [BUZZER_PLAY, 0, 0], int(index))
    
    def rest(self, number, index = 1):
        if not type_check(number, int, float):
            return
        time.sleep(number * (60 / self.note_tempo))
    
    @property
    def tempo(self):
        return round(self.note_tempo)

    @tempo.setter
    def tempo(self, value):
        if not type_check(value, int, float):
            return
        value = num_range_check(value, 6, 600)
        self.note_tempo = value