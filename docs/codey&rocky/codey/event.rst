:mod:`event` --- Event Processing Unit
=============================================

.. module:: event
    :synopsis: Event Processing Unit

The main functionality and function of the ``event`` module

Event processing unit instructions
----------------------
The way user events are used currently supports two ways of writing. One is registration：

.. code-block:: python

  import codey
  import time
  import event
  
  def start_cb():
      while True:
          codey.led.show(255, 0, 0)
          time.sleep(1)
          codey.led.show(0, 0, 0)
          time.sleep(1)
  event.start(start_cb)

The other is to use a decorator, such as：

.. code-block:: python

  import codey
  import time
  import event
  
  @event.start
  
  def start_callback():
      while True:
          codey.led.show(255, 0, 0)
          time.sleep(1)
          codey.led.show(0, 0, 0)
          time.sleep(1)

Function
----------------------

.. function:: start(callback)

   Startup event.

.. function:: shaked(callback)

   Codey was shaken event.

.. function:: received(callback, msgstr)

   Broadcast reception detection event. In addition to the callback parameter, the parameter：

    - *msgstr* string type, the string to be matched. The event will be triggered when the received string matches the matching string.

.. function:: button_a_pressed(callback)

   Button A pressed event.

.. function:: button_b_pressed(callback)

   Button B pressed event.

.. function:: button_c_pressed(callback)

   Button C pressed event.

.. function:: tilted_left(callback)

   Codey left tilt event.

.. function:: tilted_right(callback)

   Codey right tilt event.

.. function:: ears_up(callback)

   Codey ear up event.

.. function:: ears_down(callback)

   Codey ear down event.

.. function:: ir_received(callback, ir_str)

   Infrared string reception detection event. In addition to the callback parameter, the parameter：

    - *ir_str* string type, the string to be matched. The event will be triggered when the received string matches the matching string.

.. function:: greater_than(callback, threshold, type_str)

   The threshold comparison event, which will be triggered when the threshold is exceeded. In addition to the callback parameter, the parameter：

    - *threshold* value data, set the threshold for triggering.
    - *type_str* string data, currently only supports ``sound_sensor``: volume sensor, ``timer``: timer.

.. function:: less_than(callback, threshold, type_str)

   Threshold comparison event, triggered below the threshold, in addition to the callback parameter, the parameter：

    - *threshold* value data, set the threshold for triggering
    - *type_str* string data, currently only supports ``light_sensor``: light sensor.

Sample Code：
----------------------

.. code-block:: python

  import codey
  import event
  
  @event.button_a_pressed
  def button_a_cb():
      print("button a event triggered")
  
  @event.button_b_pressed
  def button_b_cb():
      print("button b event triggered")
  
  @event.button_c_pressed
  def button_c_cb():
      print("button c event triggered")
  
  @event.greater_than(20, "sound_sensor")
  def sound_sensor_cb():
      print("sound sensor greater event triggered")
  
  @event.greater_than(5, "timer")
  def timer_cb():
      print("timer greater event triggered")
  
  @event.less_than(30, "light_sensor")
  def light_sensor_cb():
      print("light sensor event triggered")