:mod:`battery` --- Built-in Lithium Battery
=============================================

.. module:: battery
    :synopsis: Built-in Lithium Battery

The main functionality and function of the ``battery`` module

Function
----------------------

.. function:: get_voltage()

   Get the current battery voltage, the return value is a floating point data. The unit is ``V``.

.. function:: get_percentage()

   Get the percentage of remaining battery power. The return value is an integer. The data range is ``0 ~ 100``, where 100 means there is still 100% of the remaining battery.

Sample Code：
----------------------

.. code-block:: python

  import codey
  
  while True:
      print("vol" + str(codey.battery.get_voltage()))
      print("percentage" + str(codey.battery.get_percentage()))