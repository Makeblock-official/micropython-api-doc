:mod:`haloboard.mesh` --- mesh广播消息
=============================================

.. module:: haloboard.mesh
    :synopsis: mesh广播消息

``haloboard.mesh`` 模块的主要功能与函数

功能描述
----------------------
该模块主要介绍基于mesh网络模块的函数API

功能相关函数
----------------------

.. function:: start(type = "node")

  启动mesh通讯，参数：
- *type* 指mesh网络中的类型，可以为root或者node，默认为node。

# mesh boardcast

.. function:: get_number_of_nodes()

  获取目前mesh网络中node的数量（仅限于root？）。

.. function:: on_mesh_message_come(msg)

  处理mesh消息。
- *msg* 当前需要处理的mesh消息。

.. function:: get_info(msg)

  获取mesh消息的info信息。
- *msg* 当前需要处理的mesh消息。

.. function:: get_info_status(msg)

  获取mesh消息当前状态（status）
- *msg* 当前需要处理的mesh消息。

# for online mode

.. function:: get_all_info_status()

  获取所有mesh消息的当前状态


.. function:: get_info_once(msg)

  单次获取mesh消息的info信息。
- *msg* 当前需要处理的mesh消息。

程序示例一：
----------------------

.. code-block:: python

  # -*- coding: utf-8 -*-
  # as a node
  import haloboard
  import time
  import event

  count = 0

  @event.start
  def on_start():
      haloboard.mesh.start(type = "node")

  @event.button_pressed
  def on_button_a_pressed():
      global count
      print("button is pressed")
      haloboard.mesh.broadcast("hello", str(count))
      count += 1

  @event.mesh_message("hello")
  def received_cb():
      print("received message: hello")
      print("value:", haloboard.mesh.get_info("hello"))

程序示例二：
----------------------

.. code-block:: python

  # -*- coding: utf-8 -*-
  # as a root
  import haloboard
  import time
  import event

  @event.start
  def on_start():
      haloboard.mesh.start(type = "root")

  @event.button_pressed
  def on_button_a_pressed():
      print("button is pressed")
      haloboard.mesh.broadcast("hello", '123')

  @event.mesh_message("hello")
  def received_cb():
      print("received message: hello")
      print("value:", haloboard.mesh.get_info("hello"))
