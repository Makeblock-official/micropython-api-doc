:mod:`led` --- Onboard RGB LED
=============================================

.. module:: led
    :synopsis: Onboard RGB LED

``led`` The main functionality and function of the led module

Function
----------------------

.. function:: show(r,g,b)

   Set the displayed color of the RGB LED, parameter：

    - *r* refers to the value of red component, parameter range is ``0 ~ 255``，0 with no red component and 255 the highest red component.
    - *g* refers to the value of green component, parameter range is ``0 ~ 255``，0 with no green component and 255 the highest green component.
    - *b* refers to the value of blue component, parameter range is ``0 ~ 255``，0 with no blue component and 255 the highest blue component.

.. function:: set_red(val)

   Set the red color value of the RGB LED, parameter：

    - *val* refers to the value of red component, parameter range is ``0 ~ 255``，0 with no red component and 255 the highest red component.

.. function:: set_green(val)

   Set the green color value of the RGB LED, parameter：

    - *val* refers to the value of green component, parameter range is ``0 ~ 255``，0 with no green component and 255 the highest green component.

.. function:: set_blue(val)

   Set the blue color value of the RGB LED, parameter：

    - *val* refers to the value of blue component, parameter range is ``0 ~ 255``，0 with no blue component and 255 the highest blue component.

.. function:: off()

   Turn off the RGB LED

Sample Code：
----------------------

.. code-block:: python
 
  import codey
  import time
 
  codey.led.show(255,255,255)
  time.sleep(2)
  codey.led.off()
  time.sleep(2)
  while True:
      codey.led.set_red(255)
      time.sleep(1)
      codey.led.set_green(255)
      time.sleep(1)
      codey.led.set_blue(255)
      time.sleep(1)
      codey.led.off()
      time.sleep(1)