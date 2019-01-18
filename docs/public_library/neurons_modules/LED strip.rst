:mod:`led_strip` --- LED Strip Driver
=============================================

.. module:: led_strip
    :synopsis: LED Strip Driver

The main functionality and function of the ``led_strip`` module

Function
----------------------

.. function:: set_single(index, red_value, green_value, blue_value)

   Set color of each light on the LED Strip, parameters：

    - *index* Set the light order No, the parameter range is ``1 ~ the value of total lights on the LED Strip``。
    - *red_value* Set LED red value, the parameter range is ``0 ~ 255``, 0 means no red color, 255 means the brightest red color.
    - *green_value* Set LED green value, the parameter range is ``0 ~ 255``, 0 means no green color, 255 means the brightest green color.
    - *blue_value* Set LED blue value, the parameter range is ``0 ~ 255``, 0 means no blue color, 255 means the brightest blue color.

.. function:: set_all(red_value, green_value, blue_value)

   Set color for all lights, parameters：

    - *red_value* Set LED red value, the parameter range is ``0 ~ 255``, 0 means no red color, 255 means the brightest red color.
    - *green_value* Set LED green value, the parameter range is ``0 ~ 255``, 0 means no green color, 255 means the brightest green color.
    - *blue_value* Set LED blue value, the parameter range is ``0 ~ 255``, 0 means no blue color, 255 means the brightest blue color.

.. function:: set_effect(mode, speed, list)

   Set effect of the LED Strip, parameters：

    - *mode* effect mode, the parameter range is ``0 ~ 5``

      0： means static mode: lights status keep the last setting。

      1： means rolling mode: the front N lights turn on firstly as the setting color, then the N lights move to 2~N+1 and the first one turns off, then 3~N+2 and first two lights turn off, just like below picture:

      .. image:: img/2.png

      2： means repeat mode: the front N lights turn on firstly as the setting color, and rest lights will copy that status until the last light, just like below picture:

      .. image:: img/3.png

      3： means marquee mode: N light turn on and then move repeatedly at a setting speed, as below picture:

      .. image:: img/4.png

      4： means breathing mode: the lights change at the speed of human breath, that is they turn on/off each three seconds.

      5： means gradient mode: all lights on the strip change their color gradually to the new setting color in a specific setting time.

    - *speed* dynamic change speed, the parameter range is ``0 ~ 8``, 0 means the slowest speed and 8 is the fastest(It only works when there is dynamic change setting of lights status).

    - *list* changeable parameter list, the parameter range is ``0 ~ 8``，the first parameter means the first light color, the second parameter means the second light color, and so on; And color parameters are as below: ``black(0x00)``, ``red(0x01)``, ``orange(0x02)``, ``yellow(0x03)``, ``green(0x04)``, ``cray(0x05)``, ``blue(0x06)``, ``purple(0x07)`` and ``while(0x08)``.

Sample Code：
------------

.. code-block:: python

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
