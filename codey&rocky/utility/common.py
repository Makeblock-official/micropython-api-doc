import math
from struct import pack, unpack
########################################
# function type check
# warning!!!:  may not work
def __function_type():
    pass

def function_type_check(func):
    if type(func) == type(__function_type):
        return True
    else:
        return False
