# -*- coding: utf-8 -*-
import codey
import neurons
import event
import time

neurons.led_panel.clear()
neurons.led_panel.set_all(0, 0, 255)
time.sleep(1)
neurons.led_panel.clear()

@event.button_a_pressed
def on_button_a_pressed():
    print("button a event successed")
    neurons.led_panel.set_pixel(0, 0, 255, 0, 0)
    time.sleep(1)
    neurons.led_panel.set_pixel(4, 4, 255, 0, 0)
    time.sleep(1)
    neurons.led_panel.set_pixel(7, 7, 255, 0, 0)
    time.sleep(1)
    neurons.led_panel.set_pixel(0, 6, 255, 0, 0)
    time.sleep(1)

@event.button_b_pressed
def on_button_b_pressed():
    print("button b event successed")
    neurons.led_panel.show_image([1,6,8,0,0,0,1,6,8],0)
    time.sleep(1)
    neurons.led_panel.show_image([1,1,1,1,1,1,1,1,1],1)
    time.sleep(1)
    neurons.led_panel.show_image([6,6,6,6,6,6,6,6,6],2)
    time.sleep(1)
    neurons.led_panel.show_image([8,8,8,8,8,8,8,8,8],3)
    time.sleep(1)

@event.button_c_pressed
def on_button_c_pressed():
    print("button c event successed")
    neurons.led_panel.set_animation(0, (1,6,8,1,6,8,0,0,0))
    neurons.led_panel.set_animation(1, (6,6,6,6,6,6,6,6,6))
    neurons.led_panel.set_animation(2, [6,6,6,6,6,6,6,6,6])
    neurons.led_panel.set_animation(3, (8,8,8,8,8,8,8,8,8))
    neurons.led_panel.show_animation(1, 2)
    time.sleep(6)
    neurons.led_panel.show_string(255, 0, 0, "hello")
    time.sleep(4)
    neurons.led_panel.show_string(255, 0, 0, (100))
    time.sleep(4)
    neurons.led_panel.show_string(255, 0, 0, (1,2,3))
    time.sleep(4)