:mod:`gyro_sensor` --- Gyro Sensor
=============================================

.. module:: gyro_sensor
    :synopsis: Gyro Sensor

The main functionality and function of the ``gyro_sensor`` module

gyro sensor user Guide
----------------------

Refer to below picture for Gyro module coordinate system:

.. image:: img/5.png


Function
----------------------

.. function:: get_roll()

   Get the roll of the Euler angle, the returned data range is ``-90 ~ 90``.

.. function:: get_pitch()

   Get the pitch of the Euler angle, the returned data range is ``-180 ~ 180``.

.. function:: get_yaw()

   Get the yaw of the Euler angle, The returned data range is ``-32768 ~ 32767``，Since the gyro sensor is a six-axis sensor, there is no electronic compass. So in fact the yaw angle is just the integral of the Z-axis angular velocity. It has accumulated errors. If you want to get a true yaw angle, this API is not suitable for use.

.. function:: is_shaked()

   Check if the gyro sensor is shaken, the return value is a Boolean value, where ``True`` means that gyro sensor is shaken, and ``False`` means that gyro sensor is not shaken.

.. function:: get_acceleration(axis)

   Get the acceleration values of the three axes in ``g``, Parameters：

   - *axis* String type, with ``x``, ``y``, ``z`` representing the axis defined by gyro sensor.

.. function:: get_gyroscope(axis)

   Get the angular velocity values of the three axes in ``°/sec``, Parameters：

   - *axis* String type, with ``x``, ``y``, ``z`` representing the axis defined by gyro sensor.

Sample Code 1：
------------

.. code-block:: python

  import rocky
  import event
  import neurons
  
  @event.button_a_pressed
  def on_button_a_callback():
      codey.stop_other_scripts()
      codey.display.show("pit")
      while True:
          print(neurons.gyro_sensor.get_pitch())
          time.sleep(0.05)
  
  @event.button_b_pressed
  def on_button_b_callback():
      codey.stop_other_scripts()
      codey.display.show("rol")
      while True:
          print(neurons.gyro_sensor.get_roll())
          time.sleep(0.05)
  
  @event.button_c_pressed
  def on_button_c_callback():
      codey.stop_other_scripts()
      codey.display.show("yaw")
      while True:
          print(neurons.gyro_sensor.get_yaw())
          time.sleep(0.05)

Sample Code 2：
------------

.. code-block:: python

  import rocky
  import event
  import neurons
  
  @event.start
  def start_cb():
      codey.display.show("sha")
      while True:
          print(neurons.gyro_sensor.is_shaked())
          time.sleep(0.2)

Sample Code 3：
------------

.. code-block:: python

  import rocky
  import event
  import neurons
  
  @event.start
  def start_cb():
      while True:
          print("gyro z:", end = "")
          print(neurons.gyro_sensor.get_gyroscope("z"))
          print("accel z:", end = "")
          print(neurons.gyro_sensor.get_acceleration("z"))
          time.sleep(0.2)