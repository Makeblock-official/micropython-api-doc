:mod:`led_panel` --- RGB LED Panel
=============================================

.. module:: led_panel
    :synopsis: RGB LED Panel

The main functionality and function of the ``led_panel`` module

Function
----------------------

.. function:: set_all(red_value, green_value, blue_value)

   Set and display color of all lights on the panel, parameters：

    - *red_value* Set LED red value, the parameter range is ``0 ~ 255``, 0 means no red color, 255 means the brightest red color.
    - *green_value* Set LED green value, the parameter range is ``0 ~ 255``, 0 means no green color, 255 means the brightest green color.
    - *blue_value* Set LED blue value, the parameter range is ``0 ~ 255``, 0 means no blue color, 255 means the brightest blue color.

.. function:: set_pixel(x, y, red_value, green_value, blue_value)

   Set color for each pixel on the panel, parameters：

    - *x* pixel's X position on the panel, the parameter range is ``0 ~ 7``.
    - *y* pixel's Y position on the panel, the parameter range is ``0 ~ 7``.
    - *red_value* Set LED red value, the parameter range is ``0 ~ 255``, 0 means no red color, 255 means the brightest red color.
    - *green_value* Set LED green value, the parameter range is ``0 ~ 255``, 0 means no green color, 255 means the brightest green color.
    - *blue_value* Set LED blue value, the parameter range is ``0 ~ 255``, 0 means no blue color, 255 means the brightest blue color.

.. function:: show_image(list, mode = 0)

   Set the display content as image parameter mode, parameters：

    - *list* changeable parameter list, each value ranges is ``0 ~ 8``， the first parameter means the first light color, the second parameter means the second light color, and so on. And color parameters are as below: ``black(0x00)``, ``red(0x01)``, ``orange(0x02)``, ``yellow(0x03)``, ``green(0x04)``, ``cray(0x05)``, ``blue(0x06)``, ``purple(0x07)`` and ``while(0x08)``.
    - *mode* contents displaying mode, the parameter range is ``0 ~ 3``

     0：means emerging mode, setting image will display directly.

     1：means erase mode, original image disappear gradually and new setting image will display gradually and vertically.

     2：means left moving mode, original image moves to the left and disappear gradually and new setting image will move to the left until display the whole image.

     3：means right moving mode, original image moves to the right and disappear gradually and new setting image will move to the right until display the whole image.

.. function:: set_animation(frame_index, list)

   Set the animation content on the panel, parameters：

    - *frame_index* index of the animation frame, the parameter range is ``0 ~ 3``; 0 mean the first frame, 1 means the second, and so on.
    - *list* changeable parameter list, each value ranges is ``0 ~ 8``, the first parameter means the first light color, the second parameter means the second light color, and so on; And color parameters are as below: ``black(0x00)``, ``red(0x01)``, ``orange(0x02)``, ``yellow(0x03)``, ``green(0x04)``, ``cray(0x05)``, ``blue(0x06)``, ``purple(0x07)`` and ``while(0x08)``.

.. function:: show_animation(frame_speed, mode)

   Show the animation frame setting by ``set_animation``, parameters：

    - *frame_speed* switch speed of the animation frame content, the parameter range is ``0 ~ 2``

     0：means slow speed that the animation frame rolls every one second

     1：means normal speed that the animation frame rolls every half second

     2：means fast speed that the animation frame rolls every 0.2 second.

   - *mode* frame change mode, the parameter range is ``0 ~ 3``

     0：means emerging mode, setting image will display directly.

     1：means erase mode, original image disappear gradually and new setting image will display gradually and vertically.

     2：means left moving mode, original image moves to the left and disappear gradually and new setting image will move to the left until display the whole image.

     3：means right moving mode, original image moves to the right and disappear gradually and new setting image will move to the right until display the whole image.

.. function:: show_string(red_value, green_value, blue_value, list)

   Display the string as the setting color, parameters：

    - *red_value* Set LED red value, the parameter range is ``0 ~ 255``, 0 means no red color, 255 means the brightest red color.
    - *green_value* Set LED green value, the parameter range is ``0 ~ 255``, 0 means no green color, 255 means the brightest green color.
    - *blue_value* Set LED blue value, the parameter range is ``0 ~ 255``, 0 means no blue color, 255 means the brightest blue color.
    - *list* changeable parameter list, the first character, the second character, the third character...

.. function:: clear()

   Clear the display of the panel.

Sample Code：
------------

.. code-block:: python

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
