:mod:`button` --- 按钮模块
=============================================

.. module:: button
    :synopsis: 按钮模块

``button`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: is_pressed()

   获取按键的当前状态。 返回的结果是 ``True``：按键被按下， 或者 ``False``: 按键未被按下。

程序示例：
------------

.. code-block:: python

  import codey
  import neurons
  
  while True:
      if neurons.button.is_pressed():
          print("pressed!")
