:mod:`timer` --- Timer
=============================================

.. module:: timer
    :synopsis: Timer

``timer`` The main functionality and functions of the module

Function
----------------------

.. function:: get_timer()

   Gets the system timer time in seconds.

.. function:: reset_timer()

  Reset system timer time.

Sample Code：
----------------------

.. code-block:: python

  import haloboard
  import time

  haloboard.reset_timer()

  while True:
      if haloboard.button.is_pressed():
          haloboard.reset_timer()
          print("reset_timer")
      print("time:", end = "")
      print(haloboard.get_timer())
