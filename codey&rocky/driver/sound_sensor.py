from global_object import microphone_o
from codey_global_board import num_range_check

VAL_TO_SENSOR = 100 / 4095  # range to 0 to 100

# light and sound sensor value range
def __sound_sensor_value_scale(val):
    tem = val * 1.34 - 3
    tem = num_range_check(tem, 0.0, 100.0)
    return tem

class sound_sensor():
    def __init__(self):
        pass

    def get_loudness(self):
        return round(__sound_sensor_value_scale(microphone_o.value() * VAL_TO_SENSOR), 1)