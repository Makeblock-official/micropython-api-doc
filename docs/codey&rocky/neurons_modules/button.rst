:mod:`button` --- Button
=============================================

.. module:: button
    :synopsis: Button

The main functionality and function of the ``button`` module

Function
----------------------

.. function:: is_pressed()

   Get current status of button; the result will be ``True``: button pressed  or ``False``: button is not pressed.

Sample Code：
------------

.. code-block:: python

  import neurons
  
  while True:
      if neurons.button.is_pressed():
          print("pressed!")
