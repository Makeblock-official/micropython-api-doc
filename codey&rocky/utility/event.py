import _thread
import time
from utility.common import *
from global_object import *
from codey_global_board import *
import makeblock

MP_THREAD_EXECUTING = 0
MP_THREAD_WAIT_TO_RESTART = 1
MP_THREAD_RESTARTED = 2
MP_THREAD_FATAL_ERROR = 3

EVENT_THREAD_DEFAULT_STACK_SIZE = int(1024 * 4.5)
EVENT_THREAD_DEFAULT_PRIORITY = 1

EVENT_STATUS_FATAL_ERROR = -1
EVENT_STATUS_READY = 1

events_info = [None] * event_complement_o.EVE_MAX_NUM

def __is_event_id_valid(eve_id):
    if eve_id >= 0 and eve_id < event_complement_o.EVE_MAX_NUM:
        return True
    else:
        return False

def __event_info_set(eve_id, value):
    global events_info
    if __is_event_id_valid(eve_id):
        events_info[eve_id] = value

class event_class(object):
    def __init__(self, event_type, trigger_type, user_cb, user_para = 0, \
                 stack_size = EVENT_THREAD_DEFAULT_STACK_SIZE, priority = EVENT_THREAD_DEFAULT_PRIORITY):
        self.eve_id = event_complement_o.event_register(event_type, trigger_type, user_para)
        if __is_event_id_valid(self.eve_id):
            self.user_cb = user_cb
            self.user_para = user_para
            self.stack_size = stack_size
            self.priority = priority
            self.event_status = EVENT_STATUS_READY
        else:
            self.user_cb = None
            self.user_para = None
            self.stack_size = None
            self.priority = None
            self.event_status = EVENT_STATUS_FATAL_ERROR
            print("event register failed")

    def is_event_valid(self):
        if __is_event_id_valid(self.eve_id) and self.event_status != EVENT_STATUS_FATAL_ERROR:
            return True
        else:
            return False

class event_operation(object):
    def __init__(self, event_class):
        self.eve_id = event_class.eve_id
        self.cb = event_class.user_cb
        self.stack_size = event_class.stack_size
        self.priority = event_class.priority

    def __event_cb_task(self):
        # only call this function once at the top of thread function
        thread_id = stop_threads_o.add_thread()
        while True:
            event_complement_o.clear_sync(self.eve_id)
            KeyboardInterrupt_flag = False
            try:
                while True:
                    if __is_event_id_valid(self.eve_id):
                        stop_threads_o.set_thread_sta(thread_id, MP_THREAD_RESTARTED)
                        if event_complement_o.wait_trigger(self.eve_id) == True:
                            # Call user callback function
                            if function_type_check(self.cb):
                                stop_threads_o.set_thread_sta(thread_id, MP_THREAD_EXECUTING)
                                self.cb()
                            event_complement_o.clear_sync(self.eve_id)
                        else:
                            continue
                    else:
                        time.sleep(10)
            # if error occured in the callback, the sema RAM will be freed, 
            # but other function will still use this sema, then a fatal system error happend
            # catch the exception and make this task never out is a temporary solution
            except KeyboardInterrupt:
                # it's a proactive error, restart the thread only
                # we make tiis exception a reserved one
                stop_threads_o.set_thread_sta(thread_id, MP_THREAD_RESTARTED)
                print("restart the thread proactively", "id is", self.eve_id)
                KeyboardInterrupt_flag = True

            # when error occured, set the item in event_sema_list to None, 
            # idicating that this callback had been destroyed
            if not KeyboardInterrupt_flag:
                stop_threads_o.set_thread_sta(thread_id, MP_THREAD_FATAL_ERROR)
                if __is_event_id_valid(self.eve_id):
                    __event_info_set(self.eve_id, None)
                print("event:", self.eve_id, "error occured:")
                print("free the memory of this callback")
                break

    def __event_execute_cb(self):
        _thread.stack_size(self.stack_size)
        _thread.start_new_thread(self.__event_cb_task, ())
  
    def event_listening_start(self):
        self.__event_execute_cb()

######################################################################################
def event_trigger(eve_type, parameter = None):
    event_complement_o.trigger_by_type(eve_type, parameter)

def event_register(event_type, trigger_type, user_cb, user_para = 0, stack_size = EVENT_THREAD_DEFAULT_STACK_SIZE):
    global events_info
    event = event_class(event_type, trigger_type, user_cb, user_para, stack_size)
    if event.is_event_valid():
        __event_info_set(event.eve_id, event)
    elif __is_event_id_valid(event.eve_id):
        __event_info_set(event.eve_id, None)
        print("event register failed, id is valid")
    else:
        print("event register failed")

def event_system_start():
    for item in events_info:
        if item != None:
            ope = event_operation(item)
            ope.event_listening_start()
    event_complement_o.trigger_enable()


# define decorator
def button_a_pressed(callback):
    event_register(event_complement_o.EVENT_BUTTON1_PRESS, event_complement_o.TRIGGER_CONTINUOUS_BY_VALUE_TRUE, callback, None)

def button_b_pressed(callback):
    event_register(event_complement_o.EVENT_BUTTON2_PRESS, event_complement_o.TRIGGER_CONTINUOUS_BY_VALUE_TRUE, callback, None)

def button_c_pressed(callback):
    event_register(event_complement_o.EVENT_BUTTON3_PRESS, event_complement_o.TRIGGER_CONTINUOUS_BY_VALUE_TRUE, callback, None)

def start(callback):
    event_register(event_complement_o.EVE_SYSTEM_LAUNCH, event_complement_o.TRIGGER_ALWAYS_WITH_NO_PARAMETER, callback, None)

def shaked(callback):
    event_register(event_complement_o.EVENT_SHAKE, event_complement_o.TRIGGER_ONCE_BY_VALUE_TRUE, callback, None)

def received(msgstr):
    def decorator(callback):
        if not type_check(msgstr, str):
            msgstr = str(msgstr)
        event_register(event_complement_o.EVE_MESSAGE, event_complement_o.TRIGGER_BY_STRING_MATCHING, callback, msgstr)
    return decorator

def tilted_left(callback):
    event_register(event_complement_o.EVENT_TILT_LEFT, event_complement_o.TRIGGER_ONCE_BY_VALUE_TRUE, callback, None)

def tilted_right(callback):
    event_register(event_complement_o.EVENT_TILT_RIGHT, event_complement_o.TRIGGER_ONCE_BY_VALUE_TRUE, callback, None)

def ears_up(callback):
    event_register(event_complement_o.EVENT_TILT_BACK, event_complement_o.TRIGGER_ONCE_BY_VALUE_TRUE, callback, None)

def ears_down(callback):
    event_register(event_complement_o.EVENT_TILT_FORWARD, event_complement_o.TRIGGER_ONCE_BY_VALUE_TRUE, callback, None)

def ir_received(ir_str):
    def decorator(callback):
        if not type_check(ir_str, str):
            ir_str = str(ir_str)
        event_register(event_complement_o.EVENT_IR_RECEIVED_STR , event_complement_o.TRIGGER_BY_STRING_MATCHING, callback, ir_str)
    return decorator

def greater_than(threshold, type_str):
    def decorator(callback):
        if not type_check(threshold, int, float):
            return
        if threshold < 0:
            threshold = 0

        if type_str == "sound_sensor":
            event_register(event_complement_o.EVENT_SOUND_OVER, event_complement_o.TRIGGER_ONCE_BY_VALUE_LARGER, callback, threshold)
        elif type_str == "timer":
            event_register(event_complement_o.EVE_TIME_OVER, event_complement_o.TRIGGER_ONCE_BY_VALUE_LARGER, callback, threshold)
    return decorator

def less_than(threshold, type_str):
    def decorator(callback):
        if not type_check(threshold, int, float):
            return
        if threshold < 0:
            threshold = 0

        if type_str == "light_sensor":
            event_register(event_complement_o.EVENT_LIGHT_UNDER, event_complement_o.TRIGGER_ONCE_BY_VALUE_SMALLER, callback, threshold)

    return decorator