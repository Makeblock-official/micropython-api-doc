:mod:`button_c` --- 板载按键C
=============================================

.. module:: button_c
   :synopsis: 板载按键C

``button_c`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: is_pressed()

   获取按键C当前状态。 返回的结果是 ``true``：按键被按下， 或者 ``false``: 按键未被按下

程序示例：
------------

.. code-block:: python

  import codey
  
  def loop():
      while True:
          if codey.button_c.is_pressed():
              print("button C is pressed")
  loop()