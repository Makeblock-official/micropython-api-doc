:mod:`color_ir_sensor` --- Color IR Sensor
=============================================

.. module:: color_ir_sensor
    :synopsis: Color IR Sensor

The main functionality and function of the ``color_ir_sensor`` module

Color infrared sensor description
----------------------

.. image:: img/1.png

As shown in the figure, the sensors in front of the rocky are

- White LED：light white to achieve detecting the visible light reflection intensity on the surface of the object with using visible light sensor.
- Visible Light Sensor：detect the visible light intensity.
- RGB LED：light LED with specific RGB value to achieve recognizing the color with using the visible light sensor.
- Infrared Light Sensor：detect the infrared light intensity
- IR Transmitter：transmit infrared light to achieve detecting the infrared light reflection intensity on the surface of the object with using the infrared light sensor.

Function
----------------------

.. function:: get_red()

   Get the size of the red color component of the color sensor, parameter range is ``0 ~ 100``.

.. function:: get_green()

   Get the size of the green color component of the color sensor, parameter range is ``0 ~ 100``.

.. function:: get_blue()

   Get the size of the blue color component of the color sensor, parameter range is ``0 ~ 100``.

.. function:: is_color(color_str)

   Judge whether a matching color is detected, parameters：

    - *color_str* color type, including ``red, green, blue, yellow, cyan, purple, white, black``, the corresponding parameter is ``red``, ``green``, ``blue``, ``yellow``, ``cyan``, ``purple``, ``white``, ``black``. Return value is boolean, ``Ture`` represents color matching, ``False`` represents the colors do not match.

.. function:: get_light_strength()

   Get the ambient light intensity detected by the visible light sensor, parameter range is ``0 ~ 100``.

.. function:: get_greyness()

   Get the grayscale value detected by the visible light sensor (using RGB LED and visible light sensor), parameter range is ``0 ~ 100``.

.. function:: get_reflected_light()

   Get the visible light reflection intensity detected by the visible light sensor, parameter range is ``0 ~ 100``.

.. function:: get_reflected_infrared()

   Get the infrared light reflection intensity detected by the infrared light receiving tube, parameter range is ``0 ~ 100``.

.. function:: is_obstacle_ahead()

   Detect if there are obstacles in front, the return value is boolean, ``Ture`` represents obstacles, ``False`` represents no obstacles.

.. function:: set_led_color(color_name)

   Set color for the RGB LED light of the color sensor, parameters：

    - *color_name* including ``red, green, blue, yellow, cyan, purple, white, black``, the corresponding parameter is ``red``, ``green``, ``blue``, ``yellow``, ``cyan``, ``purple``, ``white``, ``black``.

Sample Code：
------------

.. code-block:: python

  import codey
  import rocky
  
  while True:
      if rocky.color_ir_sensor.is_obstacle_ahead():
          rocky.color_ir_sensor.set_led_color('white')
      else:
      	rocky.color_ir_sensor.set_led_color('black')