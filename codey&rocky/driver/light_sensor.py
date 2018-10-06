from global_object import light_o
VAL_TO_SENSOR = 100 / 4095  # range to 0 to 100
class light_sensor():
    def __init__(self):
        pass
        
    def get_value(self):
        return round(light_o.value() * VAL_TO_SENSOR, 1)