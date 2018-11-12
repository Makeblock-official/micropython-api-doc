:mod:`button_b` --- Onboard Button B
=============================================

.. module:: button_b
    :synopsis: Onboard Button B

The main functionality and function of the ``button_b`` module

Function
----------------------

.. function:: is_pressed()

   Get the current state of button B. The result returned is ``True``: the button is pressed, or the ``False``: button is not pressed.

Sample Code：
----------------------

.. code-block:: python

  import codey
  
  def loop():
      while True:
          if codey.button_b.is_pressed():
              print("button B is pressed")
  loop()