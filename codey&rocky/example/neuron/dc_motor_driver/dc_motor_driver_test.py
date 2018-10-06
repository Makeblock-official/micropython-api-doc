# -*- coding: utf-8 -*-
import codey
import neurons
import event

@event.button_a_pressed
def on_button_a_pressed():
    print("button a event successed")
    neurons.dc_motor_driver.set_power(100, 1)

@event.button_b_pressed
def on_button_b_pressed():
    print("button b event successed")
    neurons.dc_motor_driver.set_power(100, 2)

@event.button_c_pressed
def on_button_c_pressed():
    print("button c event successed")
    neurons.dc_motor_driver.set_power(100, 0)
    neurons.dc_motor_driver.set_power(100, 1, 2)