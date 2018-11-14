:mod:`event` --- 事件处理单元
=============================================

.. module:: event
    :synopsis: 事件处理单元

``event`` 模块的主要功能与函数

事件处理单元使用说明
----------------------
用户事件的使用方式目前支持两种写法，一种为注册方式：

.. code-block:: python

  import codey
  import time
  import event
  
  def start_cb():
      while True:
          codey.led.show(255, 0, 0)
          time.sleep(1)
          codey.led.show(0, 0, 0)
          time.sleep(1)
  event.start(start_cb)

另一种是使用修饰器的写法，如：

.. code-block:: python

  import codey
  import time
  import event
  
  @event.start
  
  def start_callback():
      while True:
          codey.led.show(255, 0, 0)
          time.sleep(1)
          codey.led.show(0, 0, 0)
          time.sleep(1)

功能相关函数
----------------------

.. function:: start(callback)

   开机启动事件。

.. function:: shaked(callback)

   小程被摇晃事件。

.. function:: received(callback, msgstr)

   广播接收事件, 除了回调参数之外，参数：

    - *msgstr* 字符串类型，要匹配的字符串，当收到的字符串和匹配字符串一致时，会触发该事件。

.. function:: button_a_pressed(callback)

   按键A被按下事件。

.. function:: button_b_pressed(callback)

   按键B被按下事件。

.. function:: button_c_pressed(callback)

   按键C被按下事件。

.. function:: tilted_left(callback)

   小程左倾斜事件。

.. function:: tilted_right(callback)

   小程右倾斜事件。

.. function:: ears_up(callback)

   小程耳朵向上事件。

.. function:: ears_down(callback)

   小程耳朵向下事件。

.. function:: ir_received(callback, ir_str)

   红外字符串接收检测事件，除了回调参数之外，参数：

    - *ir_str* 字符串类型，要匹配的字符串，当收到的字符串和匹配字符串一致时，会触发该事件。

.. function:: greater_than(callback, threshold, type_str)

   阈值比较事件，超过阈值则触发，除了回调参数之外，参数：

    - *threshold* 数值数据，设置触发的阈值。
    - *type_str* 字符串数据，目前只支持 ``sound_sensor``：音量传感器，``timer``：计时器。

.. function:: less_than(callback, threshold, type_str)

   阈值比较事件，低于阈值则触发，除了回调参数之外，参数：

    - *threshold* 数值数据，设置触发的阈值。
    - *type_str* 字符串数据，目前只支持 ``light_sensor``：光线传感器。

程序示例：
----------------------

.. code-block:: python

  import codey
  import event
  
  @event.button_a_pressed
  def button_a_cb():
      print("button a event triggered")
  
  @event.button_b_pressed
  def button_b_cb():
      print("button b event triggered")
  
  @event.button_c_pressed
  def button_c_cb():
      print("button c event triggered")
  
  @event.greater_than(20, "sound_sensor")
  def sound_sensor_cb():
      print("sound sensor greater event triggered")
  
  @event.greater_than(5, "timer")
  def timer_cb():
      print("timer greater event triggered")
  
  @event.less_than(30, "light_sensor")
  def light_sensor_cb():
      print("light sensor event triggered")