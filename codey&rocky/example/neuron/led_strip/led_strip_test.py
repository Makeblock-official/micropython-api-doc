# -*- coding: utf-8 -*-
import codey
import neurons
import event
import time

neurons.led_strip.set_all(0, 0, 255)
time.sleep(1)

@event.button_a_pressed
def on_button_a_pressed():
    print("button a event successed")
    neurons.led_strip.set_all(0, 0, 0)
    neurons.led_strip.set_single(1, 255, 0, 0)
    time.sleep(1)
    neurons.led_strip.set_all(0, 0, 0)
    neurons.led_strip.set_single(2, 255, 0, 0)
    time.sleep(1)
    neurons.led_strip.set_all(0, 0, 0)
    neurons.led_strip.set_single(3, 255, 0, 0)
    time.sleep(1)

@event.button_b_pressed
def on_button_b_pressed():
    print("button b event successed")
    neurons.led_strip.set_effect(0, 8, (1,6,8,1,6,8,1,6,8))
    time.sleep(3)
    neurons.led_strip.set_effect(1, 8, (1,6,8,1,6,8,1,6,8))
    time.sleep(3)
    neurons.led_strip.set_effect(2, 8, (1,6,8,1,6,8,1,6,8))
    time.sleep(3)
    neurons.led_strip.set_effect(3, 8, (1,6,8,1,6,8,1,6,8))
    time.sleep(3)
    neurons.led_strip.set_effect(4, 8, (1,6,8,1,6,8,1,6,8))
    time.sleep(3)
    neurons.led_strip.set_effect(5, 8, (1,6,8,1,6,8,1,6,8))
    time.sleep(3)

@event.button_c_pressed
def on_button_c_pressed():
    print("button c event successed")
    neurons.led_strip.set_effect(0, 5, (1,1,1,1,1,1,1,1,1))
    time.sleep(3)
    neurons.led_strip.set_effect(1, 5, (1,1,1,1,1,1,1,1,1))
    time.sleep(3)
    neurons.led_strip.set_effect(2, 5, (1,1,1,1,1,1,1,1,1))
    time.sleep(3)
    neurons.led_strip.set_effect(3, 5, (1,1,1,1,1,1,1,1,1))
    time.sleep(3)
    neurons.led_strip.set_effect(4, 5, (1,1,1,1,1,1,1,1,1))
    time.sleep(3)
    neurons.led_strip.set_effect(5, 5, (1,1,1,1,1,1,1,1,1))
    time.sleep(3)