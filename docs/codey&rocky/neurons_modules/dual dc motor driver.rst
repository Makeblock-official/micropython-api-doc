:mod:`dc_motor_driver` --- Dual DC Motor Driver
=============================================

.. module:: dc_motor_driver
    :synopsis: dDual DC Motor Driver

The main functionality and function of the ``dc_motor_driver`` module

Function
----------------------

.. function:: set_power(speed, ch = 0)

   Set power for the motor driver in each channel, parameters:

    - *speed* Refers to power value of the motor controlled, the parameter range is ``-100 ~ 100``.
    - *ch* Refers to channel number of the motor controlled, the parameter range is ``0 ~ 2``, and ``0``: stands for both slots，``1``: for slot 1 channel，``2``: for slot 2 channel.

Sample Code：
------------

.. code-block:: python

  import codey
  import neurons
  import event
  
  @event.button_a_pressed
  def on_button_a_pressed():
      print("button a event succeeded")
      neurons.dc_motor_driver.set_power(100, 1)
  
  @event.button_b_pressed
  def on_button_b_pressed():
      print("button b event succeeded")
      neurons.dc_motor_driver.set_power(100, 2)
  
  @event.button_c_pressed
  def on_button_c_pressed():
      print("button c event succeeded")
      neurons.dc_motor_driver.set_power(100, 0)
      neurons.dc_motor_driver.set_power(100, 1, 2)