:mod:`button_b` --- 板载按键B
=============================================

.. module:: button_b
   :synopsis: 板载按键B

``button_b`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: is_pressed()

   获取按键B当前状态。 返回的结果是 ``true``：按键被按下， 或者 ``false``: 按键未被按下

程序示例：
------------

.. code-block:: python

  import codey
  
  def loop():
      while True:
          if codey.button_b.is_pressed():
              print("button B is pressed")
  loop()