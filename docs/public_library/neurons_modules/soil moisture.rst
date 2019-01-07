:mod:`soil_moisture` --- 土壤湿度传感器模块
=============================================

.. module:: soil_moisture
    :synopsis: 土壤湿度传感器模块

``soil_moisture`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: get_value()

   获取传感器检测到的土壤湿度值，数值的范围是 ``0 ~ 100`` 数值越大，表示土壤湿度越高。

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
          print(neurons.soil_moisture.get_value())
          time.sleep(0.2)
