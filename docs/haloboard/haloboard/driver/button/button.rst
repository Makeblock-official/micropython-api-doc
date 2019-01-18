:mod:`button` --- Onboard Button
=============================================

.. module:: button
    :synopsis: Onboard Button

``button`` The main functionality and functions of the module

Function
----------------------

.. function:: is_pressed()

   Gets the current state of key A. The returned result is ` ` True ` ` : button is pressed, or ` ` False ` ` : button is not pressed.

Sample Code ：
----------------------

.. code-block:: python

  import haloboard

  def loop():
      while True:
          if haloboard.button.is_pressed():
              haloboard.led.show_all(255, 255, 255)
          else:
              haloboard.led.show_all(0, 0, 0)
  loop()