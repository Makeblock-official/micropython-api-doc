:mod:`touchpad1` --- 触摸按键1
=============================================

.. module:: touchpad1
    :synopsis: 触摸按键

``touchpad1`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: is_touched()

   获取触摸按键1当前状态。返回的结果是 True：触摸按键1被触摸， 或者 False: 触摸按键1未被触摸。

.. function:: get_value()

   获取触摸按键被触摸状态。数值范围为0-10000。

.. function:: set_touch_threshold()

   设定触摸按键的阈值，参数：

- *val* 触摸变化的百分比，检测到变化的幅值大于该百分比时认为被触摸，数值范围为0-1。

程序示例：
----------------------

.. code-block:: python

  import haloboard
  import time

  haloboard.touchpad0.set_touch_threshold(0.01 * 2)
  haloboard.touchpad1.set_touch_threshold(0.01 * 2)
  haloboard.touchpad0.set_touch_threshold(0.005 * 2)
  haloboard.touchpad0.set_touch_threshold(0.015 * 2)
  while True:
      if haloboard.touchpad0.is_touched():
          print("TouchPad 0 is touched！")
      if haloboard.touchpad1.is_touched():
          print("TouchPad 1 is touched！")
      if haloboard.touchpad2.is_touched():
          print("TouchPad 2 is touched！")
      if haloboard.touchpad3.is_touched():
          print("TouchPad 3 is touched！")

      print("val:" + str(haloboard.touchpad0.get_value()) + " ," + str(haloboard.touchpad1.get_value()) + " ," + str(haloboard.touchpad2.get_value()) + " ," + str(haloboard.touchpad3.get_value()))
      time.sleep(0.01)
