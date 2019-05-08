:mod:`timer` --- 计时器模块
=============================================

.. module:: timer
    :synopsis: 计时器模块

``timer`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: timer()

   获取系统计时器时间，单位为秒。

.. function:: reset_timer()

  复位系统计时器时间。

程序示例：
----------------------

.. code-block:: python

  import novapi

  novapi.reset_timer()

  while True:
      if novapi.timer() > 5:
          novapi.reset_timer()
      print("time:", novapi.timer())
