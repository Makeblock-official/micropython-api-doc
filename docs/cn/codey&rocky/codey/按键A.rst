:mod:`button_a` --- 板载按键A
=============================================

.. module:: button_a
   :synopsis: 板载按键A

``button_a`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: is_pressed()

   获取按键A当前状态。 返回的结果是 ``true``：按键被按下， 或者 ``false``: 按键未被按下

程序示例：
------------

.. code-block:: python

  import codey
  
  def loop():
      while True:
          if codey.button_a.is_pressed():
              print("button A is pressed")
  loop()