:mod:`vibration_motor` --- Vibration Motor
=============================================

.. module:: vibration_motor
    :synopsis: Vibration Motor

``vibration_motor`` The main functionality and functions of the module

Function
----------------------

.. function:: set_strength(val)

   Set the dynamic value of vibration motor, set but not executed, parameters:
- *val*  - Values range from 0 to 100.

.. function:: on(value=None)

   The vibration motor starts to execute. If no parameters are set, the default value is 100. Parameters:
- *value* - Values range from 0 to 100.

Sample Code：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      print("set_strength 100")
      haloboard.vibration_motor.set_strength(100)
      haloboard.vibration_motor.on(100)
      time.sleep(3)
      haloboard.vibration_motor.on(0)
      time.sleep(2)
      print("set_strength 50")
      haloboard.vibration_motor.set_strength(50)
      haloboard.vibration_motor.on()
      time.sleep(3)
