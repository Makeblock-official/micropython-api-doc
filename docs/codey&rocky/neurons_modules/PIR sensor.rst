:mod:`pir_sensor` --- PIR Sensor
=============================================

.. module:: pir_sensor
    :synopsis: PIR Sensor

The main functionality and function of the ``pir_sensor`` module

Function
----------------------

.. function:: is_activated()

   Get the detecting result from the sensor. Result will be ``True``: it detects human nearby or ``False``: it doesn't detect human nearby.

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
          print(neurons.pir_sensor.is_activated())
          time.sleep(0.2)
