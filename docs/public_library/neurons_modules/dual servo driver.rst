:mod:`servo_driver` --- 双舵机驱动模块
=============================================

.. module:: servo_driver
    :synopsis: 双舵机驱动模块

``servo_driver`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: set_angle(position, ch = 0)

   设置双路舵机各路电机的动力，参数：

    - *position* 控制目标舵机的转动角度，参数范围是 ``0 ~ 180``。
    - *ch* 控制的舵机通道，参数范围是 ``0 ~ 2``，其中 ``0`` 表示两路舵机通道，``1`` 表示插槽1通道，``2`` 表示插槽2通道。

程序示例：
------------

.. code-block:: python

  import codey
  import neurons
  import event
  import time
  
  neurons.servo_driver.set_angle(0, 0)
  time.sleep(1)
  
  @event.button_a_pressed
  def on_button_a_pressed():
      print("button a event succeeded")
      neurons.servo_driver.set_angle(100, 1)
  
  @event.button_b_pressed
  def on_button_b_pressed():
      print("button b event succeeded")
      neurons.servo_driver.set_angle(100, 2)
  
  @event.button_c_pressed
  def on_button_c_pressed():
      print("button c event succeeded")
      neurons.servo_driver.set_angle(100, 0)
