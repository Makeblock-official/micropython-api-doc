# -*- coding: utf-8 -*-
import codey
import neurons
import event
import time

neurons.servo_driver.set_angle(0, 0)
time.sleep(1)

@event.button_a_pressed
def on_button_a_pressed():
    print("button a event successed")
    neurons.servo_driver.set_angle(100, 1)

@event.button_b_pressed
def on_button_b_pressed():
    print("button b event successed")
    neurons.servo_driver.set_angle(100, 2)

@event.button_c_pressed
def on_button_c_pressed():
    print("button c event successed")
    neurons.servo_driver.set_angle(100, 0)