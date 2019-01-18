:mod:`soil_moisture` --- Soil Moisture
=============================================

.. module:: soil_moisture
    :synopsis: Soil Moisture

The main functionality and function of the ``soil_moisture`` module

Function
----------------------

.. function:: get_value()

   Get humidity of soil detected, ranging ``0 ~ 100``; the higher value is, the higher humidity is.

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
          print(neurons.soil_moisture.get_value())
          time.sleep(0.2)
