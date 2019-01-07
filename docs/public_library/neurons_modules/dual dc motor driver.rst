:mod:`dc_motor_driver` --- 双直流电机驱动模块
=============================================

.. module:: dc_motor_driver
    :synopsis: 双直流电机驱动模块

``dc_motor_driver`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: set_power(speed, ch = 0)

   设置双路直流电机各路电机的动力，参数：

    - *speed* 控制目标电机的动力值，参数范围是 ``-100 ~ 100``。
    - *ch* 控制的电机通道，参数范围是 ``0 ~ 2``，其中 ``0`` 表示两路电机通道，``1`` 表示插槽1通道，``2`` 表示插槽2通道。

程序示例：
------------

.. code-block:: python

  import codey
  import neurons
  import event
  
  @event.button_a_pressed
  def on_button_a_pressed():
      print("button a event succeeded")
      neurons.dc_motor_driver.set_power(100, 1)
  
  @event.button_b_pressed
  def on_button_b_pressed():
      print("button b event succeeded")
      neurons.dc_motor_driver.set_power(100, 2)
  
  @event.button_c_pressed
  def on_button_c_pressed():
      print("button c event succeeded")
      neurons.dc_motor_driver.set_power(100, 0)
      neurons.dc_motor_driver.set_power(100, 1, 2)