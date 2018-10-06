from global_object import infrared_o
from global_object import ir_learning_o
from codey_global_board import *
import time

class ir():
    def __init__(self):
        pass

    def receive(self):
        ir_list_t = infrared_o.value()
        if ir_list_t == None:
            return ''

        if type_check(ir_list_t, list):
            ir_len_t = len(ir_list_t)
            ir_str_t = ''
            if ir_len_t == 0:
                return ''
            elif ir_list_t[0] != ord('\n'):
                return ''
            elif ir_len_t > 1:
                for i in range(1, ir_len_t):
                    try:
                        if ir_list_t[i] == ord('\n'):
                            break 
                        else:
                            ir_str_t = chr(ir_list_t[i]) + ir_str_t
                    except:
                        return ir_str_t  

                return ir_str_t 
            else:
                return ''
        elif type_check(ir_list_t, int):
            return ir_list_t

    def send(self, sstr):
        if type(sstr) != str: 
            sstr = str(sstr) + '\n'
        else:
            if(sstr[-1] != '\n'):
                sstr += '\n'
        infrared_o.send(0, sstr)

    def start_learning(self):
        ir_learning_o.start()

    def stop_learning(self):
        ir_learning_o.stop()

# we can store 16 items mostly 
    def save_learned_result(self, index = 1):
        if not type_check(index, int, float):
            return
        index = num_range_check(index, 0, 15)
        
        ir_learning_o.save_as_index(index)

    def send_learned_result(self, index = 1):
        if not type_check(index, int, float):
            return
        index = num_range_check(index, 0, 15)

        ir_learning_o.send_index(int(index))

    def learn(self, time_s = 3):
        if not type_check(time_s, int, float):
            return
        if time_s <= 0:
            return

        self.start_learning()
        time.sleep(time_s)
        self.stop_learning()
        self.save_learned_result()

    def receive_remote_code(self):
        ir_char = infrared_o.get_char()
        if ir_char == None:
            ir_char = [0, 0]
        return ir_char

