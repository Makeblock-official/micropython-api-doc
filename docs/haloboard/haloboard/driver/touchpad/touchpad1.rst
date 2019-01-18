:mod:`touchpad0` --- Touch Button1
=============================================

.. module:: touchpad0
    :synopsis: Touch Button1

``touchpad0`` The main functionality and functions of the module

Function
----------------------

.. function:: is_touched()

   Gets the current state of touch button 1.This returns True: the touch button 1 is touched, or False: the touch button 1 is not touched.

.. function:: get_value()

   Gets the touched state of the touch button. Values range from 0 to 10000.

.. function:: set_touch_threshold()

   Set the threshold value of the touch button, parameters:

- *val* - The percentage of touch change, when the detected change amplitude is greater than this percentage, 
          it is considered to be touched, and the value range is 0-1.

Sample Code：
----------------------

.. code-block:: python

  import haloboard
  import time

  haloboard.touchpad0.set_touch_threshold(0.01 * 2)
  haloboard.touchpad1.set_touch_threshold(0.01 * 2)
  haloboard.touchpad0.set_touch_threshold(0.005 * 2)
  haloboard.touchpad0.set_touch_threshold(0.015 * 2)
  while True:
      if haloboard.touchpad0.is_touched():
          print("TouchPad 0 is touched！")
      if haloboard.touchpad1.is_touched():
          print("TouchPad 1 is touched！")
      if haloboard.touchpad2.is_touched():
          print("TouchPad 2 is touched！")
      if haloboard.touchpad3.is_touched():
          print("TouchPad 3 is touched！")

      print("val:" + str(haloboard.touchpad0.get_value()) + " ," + str(haloboard.touchpad1.get_value()) + " ," + str(haloboard.touchpad2.get_value()) + " ," + str(haloboard.touchpad3.get_value()))
      time.sleep(0.01)
