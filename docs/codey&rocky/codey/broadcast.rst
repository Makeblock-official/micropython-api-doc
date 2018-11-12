:mod:`codey_broadcast` --- Broadcast Module
=============================================

.. module:: codey
    :synopsis: Broadcast Module

The main functionality and function of the ``codey_broadcast`` module (you do not need to bring the module name when using due to it is a system function)

Function
----------------------

.. function:: broadcast(str)

   A broadcast can be sent to the serial port, Bluetooth, and its own event monitoring unit, Parameter：

    - *str* The content of the broadcast.

Sample Code：
----------------------

.. code-block:: python

  import codey
  import event
  
  @event.button_a_pressed
  def button_a_cb():
      print("button a event succeeded")
      codey.broadcast("hello")
  
  @event.received("hello")
  def received_cb():
      print("received message: hello")