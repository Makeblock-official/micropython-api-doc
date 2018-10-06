from global_object import potentiometer_o

VAL_TO_SENSOR = 100 / 4095  # range to 0 to 100

class potentiometer():
    def __init__(self):
        pass

    def get_value(self):
        return round(potentiometer_o.value() * VAL_TO_SENSOR)