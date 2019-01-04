:mod:`clock` --- 板载底板时钟模块
=============================================

.. module:: clock
    :synopsis: 板载底板时钟模块，计算接上底板后的时间计算

``clock`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: get_date_and_time(clock_id)

   获取时间的值。 
  - *clock_id* 时间类型参数，可以为小时：clock.HOUR_INDEX，分钟：clock.MINUTE_INDEX，秒：clock.SECOND_INDEX。

程序示例：
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
