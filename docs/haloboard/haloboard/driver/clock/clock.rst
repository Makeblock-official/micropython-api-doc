:mod:`clock` --- Onboard Baseboard Clock
=============================================

.. module:: clock
    :synopsis: Onboard Baseboard Clock

``clock`` The main functionality and functions of the module

Function
----------------------

.. function:: get_date_and_time(clock_id)

   Gets the value of the time.
  - *clock_id* - Time type parameter, can be hours: clock.HOUR_INDEX，minute：clock.MINUTE_INDEX，second：clock.SECOND_INDEX。

Sample Code ：
----------------------

.. code-block:: python

  from haloboard import * 
  import time

  minute = 0
  hour = 0
  count = 0
  while True:
      hour = clock.get_date_and_time(clock.HOUR_INDEX)
      minute = clock.get_date_and_time(clock.MINUTE_INDEX)
      second = clock.get_date_and_time(clock.SECOND_INDEX)

      print("hour:%d, minute:%d, second:%d" %(hour, minute, second))
      time.sleep(1) 
