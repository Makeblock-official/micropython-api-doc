:mod:`battery` --- 内置锂电池
=============================================

.. module:: battery
    :synopsis: 内置锂电池

``battery`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: get_voltage()

   获取当前的电池电压，返回值是一个浮点数据。单位是 ``V``

.. function:: get_percentage()

   获取剩余电池电量的百分比，返回值是一个整数，数据范围是 ``0 ~ 100``，其中 100 表示剩余电量还有 100%。

程序示例：
----------------------

.. code-block:: python

  import codey
  
  while True:
      print("vol" + str(codey.battery.get_voltage()))
      print("percentage" + str(codey.battery.get_percentage()))