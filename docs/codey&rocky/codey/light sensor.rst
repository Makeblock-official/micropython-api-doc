:mod:`light_sensor` --- Onboard Light Sensor
=============================================

.. module:: light_sensor
    :synopsis: Onboard Light Sensor

The main functionality and function of the ``light_sensor`` module

Function
----------------------

.. function:: get_value()

   Get the light intensity detected by the light sensor, and the return value is the intensity value of visible light. The value range is ``0 ~ 100``.

Sample Code：
----------------------

.. code-block:: python

  import codey
  
  while True:
      codey.display.show(codey.light_sensor.get_value())