:mod:`servo_driver` --- Dual Servo Driver
=============================================

.. module:: servo_driver
    :synopsis: Dual Servo Driver

The main functionality and function of the ``servo_driver`` module

Function
----------------------

.. function:: set_angle(position, ch = 0)

   set power for the servo driver in each channel, parameters：

    - *position* Refers to turning angle value of the servo controlled, the parameter range is ``0 ~ 180``.
    - *ch* Refers to channel number servo controlled, the parameter range is ``0 ~ 2``, and ``0``: stands for both slots，``1``: for slot 1 channel，``2``: for slot 2 channel.

Sample Code：
------------

.. code-block:: python

  import codey
  import neurons
  import event
  import time
  
  neurons.servo_driver.set_angle(0, 0)
  time.sleep(1)
  
  @event.button_a_pressed
  def on_button_a_pressed():
      print("button a event succeeded")
      neurons.servo_driver.set_angle(100, 1)
  
  @event.button_b_pressed
  def on_button_b_pressed():
      print("button b event succeeded")
      neurons.servo_driver.set_angle(100, 2)
  
  @event.button_c_pressed
  def on_button_c_pressed():
      print("button c event succeeded")
      neurons.servo_driver.set_angle(100, 0)
