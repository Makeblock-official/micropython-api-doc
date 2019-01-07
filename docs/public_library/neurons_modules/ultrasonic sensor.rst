:mod:`ultrasonic_sensor` --- 超声波传感器模块
=============================================

.. module:: ultrasonic_sensor
    :synopsis: 超声波传感器模块

``ultrasonic_sensor`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: get_distance()

   获取超声波传感器测量的前方障碍物的距离，单位是 ``厘米``，返回的数据是浮点类型数值。 测量的范围是 ``3 ~ 300`` 厘米，3厘米以内的测量数据会不准确，数值的范围是 ``0 ~ 300`` 厘米。

程序示例：
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