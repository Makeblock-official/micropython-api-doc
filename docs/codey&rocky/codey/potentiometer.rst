:mod:`potentiometer` --- Onboard Potentiometer
=============================================

.. module:: potentiometer
    :synopsis: Onboard Potentiometer

The main functionality and function of the ``potentiometer`` module

Function
----------------------

.. function:: get_value()

   Get the current value of the potentiometer knob. The value range is ``0 ~ 100``.

Sample Code：
----------------------

.. code-block:: python

  import codey
  
  while True:
      codey.display.show(codey.potentiometer.get_value())