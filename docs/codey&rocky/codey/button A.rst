:mod:`button_a` --- Onboard Button A
=============================================

.. module:: button_a
    :synopsis: Onboard Button A

The main functionality and function of the ``button_a`` module

Function
----------------------

.. function:: is_pressed()

   Get the current state of button A. The result returned is ``True``: the button is pressed, or the ``False``: button is not pressed.

Sample Code：
----------------------

.. code-block:: python

  import codey
  
  def loop():
      while True:
          if codey.button_a.is_pressed():
              print("button A is pressed")
  loop()