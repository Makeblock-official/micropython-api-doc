:mod:`ultrasonic_sensor` --- Ultrasonic Sensor
=============================================

.. module:: ultrasonic_sensor
    :synopsis: Ultrasonic Sensor

The main functionality and function of the ``ultrasonic_sensor`` module

Function
----------------------

.. function:: get_distance()

   Get the distance (``cm``) between the obstacle ahead and ultrasonic sensor; the result is floating point, ranging ``3 ~ 300`` cm; but measure distance ranges ``3 ~ 300`` cm as detection is not exact enough within 3 cm.

Sample Code：
------------

.. code-block:: python

  import codey
  import time
  import event
  import neurons
  
  @event.start
  def start_cb():
      while True:
          print(neurons.ultrasonic_sensor.get_distance())
          time.sleep(0.2)