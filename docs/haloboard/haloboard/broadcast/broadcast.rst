:mod:`broadcast` --- 广播消息
=============================================

.. module:: broadcast
    :synopsis: 广播消息

``broadcast`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: broadcast(message_str)

  广播消息，广播消息后，其他线程可以接收到消息，参数：  
- *message_str* 字符串类型，消息值

程序示例：
----------------------

.. code-block:: python

  # -*- coding: utf-8 -*-
  import haloboard
  import time
  import event

  @event.button_pressed
  def on_button_a_pressed():
      print("button is pressed")
      haloboard.broadcast("hello")

  @event.received("hello")
  def received_cb():
      print("received message: hello")
      