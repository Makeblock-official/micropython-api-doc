:mod:`sound_sensor` --- Onboard Sound Sensor
=============================================

.. module:: sound_sensor
    :synopsis: Onboard Sound Sensor

The main functionality and function of the ``sound_sensor`` module

Function
----------------------

.. function:: get_loudness()

   Get the sound intensity detected by the sound sensor, and the return value is the volume. The value range is ``0 ~ 100``.

Sample Code：
------------

.. code-block:: python

  import codey
  
  while True:
      codey.display.show(codey.sound_sensor.get_loudness())