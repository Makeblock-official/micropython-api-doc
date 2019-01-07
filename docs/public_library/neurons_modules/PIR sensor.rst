:mod:`pir_sensor` --- 人体红外传感器模块
=============================================

.. module:: pir_sensor
    :synopsis: 人体红外传感器模块

``pir_sensor`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: is_activated()

   获取传感器的检测结果。 返回的结果是 ``True``：检测到附近有人， 或者 ``False``: 未检测到活动的人。

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
          print(neurons.pir_sensor.is_activated())
          time.sleep(0.2)
