:mod:`event` --- Event Module
=============================================

.. module:: event
    :synopsis: Event Module

``event`` The main functionality and functions of the module

Two kinds of writing
----------------------
Method 1: registration method, as the following example：

.. code-block:: python

  event.start(test_callback)
  event.received(callback, 'hello')

Method 2: modifier notation, as in the following example：

.. code-block:: python

  @event.start
  def start_callback():
  print(123)
  @event.received('hello')
  def received_callback():
  print(123)

Note: when the function has parameters other than callback, the parameter is added.

Function
----------------------

.. function:: start(callback)

   Start event, parameters:
- *callback* - Callback function.

.. function:: shaked(callback)

   Shaking events, parameters:
- *callback* - Callback function.

.. function:: button_pressed(callback)

   Button press event, parameters:
- *callback* - Callback function.

.. function:: tilted_left(callback)

   Tilted left events, parameters:
- *callback* - Callback function.

.. function:: tilted_right(callback)

   Tilted right events, parameters:
- *callback* - Callback function.

.. function:: arrow_up(callback)

   Arrow up event, parameters:
- *callback* - Callback function.

.. function:: arrow_down(callback)

   Arrow down event, parameters:
- *callback* - Callback function.

.. function:: receieved(callback, message_str)

   Broadcast event, parameters:
- *callback* - Callback function.
- *message_str* - The name of the broadcast to listen for.

.. function:: cloud_message(message)

   Cloud broadcast event, parameters:
- *message* - String data, the name of the information to broadcast.

.. function:: mesh_message(message)

   Mesh broadcast event, parameters:
- *message* - String data, the name of the information to broadcast.

.. function:: greater_than(callback, threshold, type_str)

   Threshold comparison event. If the threshold is exceeded, the event will be triggered. Parameter:
- *callback* - Callback function.
- *threshold* - Numeric, trigger threshold.
- *type_str* - microphone/timer，represents the sound sensor and the timer, which are currently supported only.

.. function:: touchpad0_active(callback)

   Touched button, parameters:
- *callback* - Callback function.

.. function:: touchpad1_active(callback)

   Touched button, parameters:
- *callback* - Callback function.

.. function:: touchpad2_active(callback)

   Touched button, parameters:
- *callback* - Callback function.

.. function:: touchpad3_active(callback)

   Touched button, parameters:
- *callback* - Callback function.

Sample Code：
----------------------

.. code-block:: python

  import haloboard
  import time
  import event

  @event.button_pressed
  def on_button_pressed():
      print("button event successed")
      haloboard.broadcast('hello')
      haloboard.mesh.broadcast('hello')

  @event.start
  def on_start():
      print("start event successed")

  @event.shaked
  def on_shaked():
      print("shaked event activate")

  @event.received("hello")
  def received_cb():
      print("broadcast received event successed")

  @event.tilted_left
  def on_tilted_left():
      print("tilted left event successed")

  @event.tilted_right
  def on_tilted_right():
      print("tilted right event successed")

  @event.arrow_up
  def on_arrow_up():
      print("arrow up event successed")

  @event.arrow_down
  def on_arrow_up():
      print("arrow down event successed")

  @event.greater_than(80, "microphone")
  def on_greater_than():
      print("sound sensor greater event successed")

  @event.greater_than(2, "timer")
  def on_greater_than():
      print("timer greater event successed")

  @event.touchpad0_active
  def on_touchpad0_active():
      print("touchpad0 active")

  @event.touchpad1_active
  def on_touchpad1_active():
      print("touchpad1 active")

  @event.touchpad2_active
  def on_touchpad2_active():
      print("touchpad2 active")

  @event.touchpad3_active
  def on_touchpad3_active():
      print("touchpad3 active")

  @event.cloud_message("hello")
  def on_cloud_message():
      print("cloud message event successed")

  @event.mesh_message("hello")
  def on_mesh_message():
      print("mesh message event successed")
