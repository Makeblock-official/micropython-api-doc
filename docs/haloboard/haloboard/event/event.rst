:mod:`event` --- 事件模块
=============================================

.. module:: event
    :synopsis: 事件模块

``event`` 模块的主要功能与函数

两种写法
----------------------
方法一：注册方式，如以下示例：

.. code-block:: python

  event.start(test_callback)
  event.received(callback, 'hello')

方法二：修饰器写法，如以下示例：

.. code-block:: python

  @event.start
  def start_callback():
  print(123)
  @event.received('hello')
  def received_callback():
  print(123)

注意：当函数有callback之外的其他参数时，需加上参数。

功能相关函数
----------------------

.. function:: start(callback)

   启动事件，参数：
- *callback* 回调函数。

.. function:: shaked(callback)

   摇晃事件，参数：
- *callback* 回调函数。

.. function:: button_pressed(callback)

   按键按下事件，参数：
- *callback* 回调函数。

.. function:: tilted_left(callback)

   左倾事件，参数：
- *callback* 回调函数。

.. function:: tilted_right(callback)

   右倾事件，参数：
- *callback* 回调函数。

.. function:: arrow_up(callback)

   前倾事件，参数：
- *callback* 回调函数。

.. function:: arrow_down(callback)

   后倾事件，参数：
- *callback* 回调函数。

.. function:: receieved(callback, message_str)

   广播事件，参数：
- *callback* 回调函数。
- *message_str* 监听的广播名称。

.. function:: cloud_message(message)

   云广播事件，参数：
- *message* 字符串数据，广播的信息名称。

.. function:: mesh_message(message)

   mesh广播事件，参数：
- *message* 字符串数据，广播的信息名称。

.. function:: greater_than(callback, threshold, type_str)

   阈值比较事件， 超过阈值则触发，参数：
- *callback* 回调函数。
- *threshold* 数值型，触发阈值。
- *type_str* microphone/timer，分别代表声音传感器和计时器，目前仅支持这两个。

.. function:: touchpad0_active(callback)

   被触摸按键，参数：
- *callback* 回调函数。

.. function:: touchpad1_active(callback)

   被触摸按键，参数：
- *callback* 回调函数。

.. function:: touchpad2_active(callback)

   被触摸按键，参数：
- *callback* 回调函数。

.. function:: touchpad3_active(callback)

   被触摸按键，参数：
- *callback* 回调函数。

程序示例：
----------------------

.. code-block:: python

  import haloboard
  import time
  import event

  @event.button_pressed
  def on_button_pressed():
      print("button event successed")
      haloboard.broadcast('hello')
      haloboard.mesh.broadcast('hello')

  @event.start
  def on_start():
      print("start event successed")

  @event.shaked
  def on_shaked():
      print("shaked event activate")

  @event.received("hello")
  def received_cb():
      print("broadcast received event successed")

  @event.tilted_left
  def on_tilted_left():
      print("tilted left event successed")

  @event.tilted_right
  def on_tilted_right():
      print("tilted right event successed")

  @event.arrow_up
  def on_arrow_up():
      print("arrow up event successed")

  @event.arrow_down
  def on_arrow_up():
      print("arrow down event successed")

  @event.greater_than(80, "microphone")
  def on_greater_than():
      print("sound sensor greater event successed")

  @event.greater_than(2, "timer")
  def on_greater_than():
      print("timer greater event successed")

  @event.touchpad0_active
  def on_touchpad0_active():
      print("touchpad0 active")

  @event.touchpad1_active
  def on_touchpad1_active():
      print("touchpad1 active")

  @event.touchpad2_active
  def on_touchpad2_active():
      print("touchpad2 active")

  @event.touchpad3_active
  def on_touchpad3_active():
      print("touchpad3 active")

  @event.cloud_message("hello")
  def on_cloud_message():
      print("cloud message event successed")

  @event.mesh_message("hello")
  def on_mesh_message():
      print("mesh message event successed")
