# dic = {'A': 1, 'B': 2, 'C': 3}

from global_object import button_o
class button():
    def __init__(self, button_id):
        self.id = button_id

    def is_pressed(self):
        return bool(button_o.value(self.id))