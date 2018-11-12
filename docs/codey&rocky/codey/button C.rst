:mod:`button_c` --- Onboard Button C
=============================================

.. module:: button_c
    :synopsis: Onboard Button C

The main functionality and function of the ``button_c`` module

Function
----------------------

.. function:: is_pressed()

   Get the current state of button C. The result returned is ``True``: the button is pressed, or the ``False``: button is not pressed.

Sample Code：
----------------------

.. code-block:: python

  import codey
  
  def loop():
      while True:
          if codey.button_c.is_pressed():
              print("button C is pressed")
  loop()