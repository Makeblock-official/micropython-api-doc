:mod:`vibration_motor` --- 震动电机
=============================================

.. module:: vibration_motor
    :synopsis: 触摸按键

``vibration_motor`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: set_strength(val)

   设置震动电机动力值，设置但不执行，参数：
- *val* 数值范围0-100。

.. function:: on(value=None)

   震动电机开始执行，若未设置参数，默认值是100，参数：
- *value* 数值范围为0-100。

程序示例：
----------------------

.. code-block:: python

  import haloboard
  import time

  while True:
      print("set_strength 100")
      haloboard.vibration_motor.set_strength(100)
      haloboard.vibration_motor.on(100)
      time.sleep(3)
      haloboard.vibration_motor.on(0)
      time.sleep(2)
      print("set_strength 50")
      haloboard.vibration_motor.set_strength(50)
      haloboard.vibration_motor.on()
      time.sleep(3)
