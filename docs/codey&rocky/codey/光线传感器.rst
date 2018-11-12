:mod:`light_sensor` --- 板载光线传感器
=============================================

.. module:: light_sensor
    :synopsis: 板载光线传感器

``light_sensor`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: get_value()

   获得光线传感器检测的光线强度, 返回值是可见光的强度值。 数值范围 ``0 ~ 100``。

程序示例：
----------------------

.. code-block:: python

  import codey
  
  while True:
      codey.display.show(codey.light_sensor.get_value())