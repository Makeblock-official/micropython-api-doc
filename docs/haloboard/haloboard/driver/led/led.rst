:mod:`led` --- Onboard RGB LED
=============================================

.. module:: led
    :synopsis: Onboard RGB LED

``led`` The main functionality and functions of the module

Function
----------------------

.. function:: show_single(led_id, r, g, b)

  Set the color and parameters of a single RGB LED light, parameter:
- *led_id*  - The number of a single LED, the parameter range is 1-12, the corresponding position is as shown below:
.. image:: img/1.png

- *r* - The value of the red component of full-color LED, the parameter range is 0 ~ 255, 0 is no red component, 255 is the brightest red component.
- *g* - The value of the green component of full-color LED, the parameter range is 0 ~ 255, 0 is no green component, 255 is the brightest green component.
- *b* - The value of the blue component of full-color LED, the parameter range is 0 ~ 255, 0 is no blue component, 255 is the brightest blue component.

  Corresponding table of common color RGB:
    .. image:: img/2.png

.. function:: show_all(r, g, b)

  Set all RGB LED lights to the same color.

- *r* - The value of the red component of full-color LED, the parameter range is 0 ~ 255, 0 is no red component, 255 is the brightest red component.
- *g* - The value of the green component of full-color LED, the parameter range is 0 ~ 255, 0 is no green component, 255 is the brightest green component.
- *b* - The value of the blue component of full-color LED, the parameter range is 0 ~ 255, 0 is no blue component, 255 is the brightest blue component.

.. function:: off_all()

  Turn off all LED lights.

.. function:: clear()

  Turn off all LED lights and turn on the out sign.

.. function:: off_single(led_id)

  Extinguishing single RGB LED, parameters:
- *led_id* - The number of a single LED, the parameter range is 1-12.

.. function:: show_ring(color_str, offset=0)

  Set 12 RGB leds as the corresponding color. Parameters:
- *color_str* - String type, string format should be "color1, color2, color3, color4",
                Where colorx is "red"/"green"/"blue"/"yellow"/"cyan"/"purple"/"white"/"orange"/"black/"gray" color characters separated by a single space,When the number of colors is greater than 12, it will be truncated into 12.
- *offset* - Value type, value range 0-12.

.. function:: ring_graph(percentage)

  Percentage displayed by the status of LED ring, parameters:
- *percentage* - Value type, value range 0-100.

.. function:: meteor_effect()

  Display meteor Lighting effects.

.. function:: rainbow_effect()

  Display rainbow Lighting effects.
  
.. function:: spoondrift_effect()

  Display rainbow spoondrift effects.
    
.. function:: firefly_effect()

  Display rainbow firefly effects.
  
.. function:: show_animation(name)

  Display default light effect, block type, parameters:
- *name* - The name of default light effect ，there four：spoondrift, meteor, rainbow, firefly。

Sample Code 1：
----------------------

.. code-block:: python

	import haloboard
	import time

	haloboard.led.show_single(1, 255, 255,255)
	time.sleep(2)
	haloboard.led.show_single(2, 255, 0, 0)
	time.sleep(2)
	haloboard.led.show_single(3, 0, 255, 0)
	time.sleep(2)
	haloboard.led.show_single(4, 0, 0, 255)
	time.sleep(2)
	haloboard.led.show_all(255, 255, 255)
	time.sleep(2)
	while True:
	    haloboard.led.off_single(1)
	    time.sleep(1)
	    haloboard.led.show_single(1, 255, 0, 0)
	    time.sleep(1)

Sample Code 2：
----------------------

.. code-block:: python

  import haloboard
  import time

  haloboard.led.show_single(1, 255, 255,255)
  time.sleep(2)
  haloboard.led.show_single(2, 255, 0, 0)
  time.sleep(2)
  haloboard.led.show_single(3, 0, 255, 0)
  time.sleep(2)
  haloboard.led.show_single(4, 0, 0, 255)
  time.sleep(2)
  haloboard.led.show_all(255, 255, 255)
  time.sleep(2)
  while True:
      haloboard.led.off_single(1)
      time.sleep(1)
      haloboard.led.show_single(1, 255, 0, 0)
      time.sleep(1)

Sample Code 3：
----------------------

.. code-block:: python

  import haloboard 
  import time
  import random

  while True:
      for i in range(101):
          haloboard.led.ring_graph(i)
          time.sleep(0.1)
          print(i)

      for i in range(101):
          haloboard.led.ring_graph(100 - i)
          time.sleep(0.1)
          print(i)

      for i in range(13):
          haloboard.led.show_ring("green blue yellow purple cyan white green blue yellow purple cyan white", i)
          time.sleep(0.5)

Sample Code 4：
----------------------

.. code-block:: python

  import haloboard
  import time
  import event

  @event.touchpad0_active
  def on_touchpad0_active():
      haloboard.stop_other_scripts()
      while True:
          haloboard.led.show_animation('spoondrift')

  @event.touchpad1_active
  def on_touchpad1_active():
      haloboard.stop_other_scripts()
      while True:
          haloboard.led.show_animation('meteor')

  @event.touchpad2_active
  def on_touchpad2_active():
      haloboard.stop_other_scripts()
      while True:
          haloboard.led.show_animation('rainbow')

  @event.touchpad3_active
  def on_touchpad3_active():
      haloboard.stop_other_scripts()
      while True:
          haloboard.led.show_animation('firefly')
