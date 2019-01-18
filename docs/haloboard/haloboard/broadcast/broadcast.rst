:mod:`broadcast` --- Broadcast Message
=============================================

.. module:: broadcast
    :synopsis: Broadcast Message

``broadcast`` The main functionality and functions of the module

Function
----------------------

.. function:: broadcast(message_str)

  Broadcast message, after broadcast message, other threads can receive the message, parameters:
- *message_str* - The message type is string, message value.

Sample Code ：
----------------------

.. code-block:: python

  # -*- coding: utf-8 -*-
  import haloboard
  import time
  import event

  @event.button_pressed
  def on_button_a_pressed():
      print("button is pressed")
      haloboard.broadcast("hello")

  @event.received("hello")
  def received_cb():
      print("received message: hello")
      