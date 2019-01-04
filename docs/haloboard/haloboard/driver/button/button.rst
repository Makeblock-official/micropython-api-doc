:mod:`button` --- 板载按键
=============================================

.. module:: button
    :synopsis: 板载按键

``button`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: is_pressed()

   获取按键A当前状态。 返回的结果是 ``True``：按键被按下， 或者 ``False``: 按键未被按下。

程序示例：
----------------------

.. code-block:: python

  import haloboard

  def loop():
      while True:
          if haloboard.button.is_pressed():
              haloboard.led.show_all(255, 255, 255)
          else:
              haloboard.led.show_all(0, 0, 0)
  loop()