from global_object import battery_o
class battery():
    def __init__(self):
        pass

    def get_voltage(self):
        return battery_o.battery_vol()

    def get_percentage(self):
        return battery_o.battery_cap()