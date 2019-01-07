:mod:`led_strip` --- 灯带驱动模块
=============================================

.. module:: led_strip
    :synopsis: 灯带驱动模块

``led_strip`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: set_single(index, red_value, green_value, blue_value)

   设置灯带上单个灯的颜色, 参数：

    - *index* 设置第几个灯，参数范围是 ``1 ~ 灯带的最大灯珠数目``。
    - *red_value* 全彩LED红色分量的数值，参数范围是 ``0 ~ 255``， 0为无红色分量，255是红色分量最亮。
    - *green_value* 全彩LED绿色分量的数值，参数范围是 ``0 ~ 255``， 0为无绿色分量，255是绿色分量最亮。
    - *blue_value* 全彩LED蓝色分量的数值，参数范围是 ``0 ~ 255``， 0为无蓝色分量，255是蓝色分量最亮。

.. function:: set_all(red_value, green_value, blue_value)

   设置全部灯带的颜色, 参数：

    - *red_value* 全彩LED红色分量的数值，参数范围是 ``0 ~ 255``， 0为无红色分量，255是红色分量最亮。
    - *green_value* 全彩LED绿色分量的数值，参数范围是 ``0 ~ 255``， 0为无绿色分量，255是绿色分量最亮。
    - *blue_value* 全彩LED蓝色分量的数值，参数范围是 ``0 ~ 255``， 0为无蓝色分量，255是蓝色分量最亮。

.. function:: set_effect(mode, speed, list)

   设置灯条的灯效，参数：

    - *mode* 灯效的模式，参数范围是 ``0 ~ 5``，其中

      0： 表示静态模式，按设定的颜色点亮前N个灯，未设置的灯珠处于熄灭状态。

      1： 表示滚动模式，按设定的颜色点亮前N个灯，按设定动态变化速度，N个灯图案，向后滚动，每次滚动一个灯，循环滚动。如下图：

      .. image:: img/2.png

      2： 表示重复模式，按设定的颜色点亮前N个灯，后面的灯重复前面N个灯的效果，直到最后一个灯。如下图：

      .. image:: img/3.png

      3： 表示跑马灯模式，重复的效果加上动态变化，按设定的动态变化速度，N个灯循环挪动。如下图：

      .. image:: img/4.png

      4： 表示呼吸灯模式，呼吸灯的变化速度按人的呼吸频率3秒1次。

      5： 表示渐变模式，整条灯带从原来的颜色渐变到新设定的颜色，变化间隔时间可设定。

    - *speed* 动态变化速度，参数范围是 ``0 ~ 8``，0最慢，8最快。(只针对有动态变化的灯效的设置)。

    - *list* 可变参数列表，每个数值的参数范围是 ``0 ~ 8``，第1个参数表示第一个灯的颜色，第2个参数表示第二个灯的颜色...，颜色的参数如下：  ``黑(0x00)``，``红(0x01)``，``橙(0x02)``，``黄(0x03)``，``绿(0x04)``，``青(0x05)``，``蓝(0x06)``，``紫(0x07)``，``白(0x08)``。

程序示例：
------------

.. code-block:: python

  import codey
  import neurons
  import event
  import time
  
  neurons.led_strip.set_all(0, 0, 255)
  time.sleep(1)
  
  @event.button_a_pressed
  def on_button_a_pressed():
      print("button a event successed")
      neurons.led_strip.set_all(0, 0, 0)
      neurons.led_strip.set_single(1, 255, 0, 0)
      time.sleep(1)
      neurons.led_strip.set_all(0, 0, 0)
      neurons.led_strip.set_single(2, 255, 0, 0)
      time.sleep(1)
      neurons.led_strip.set_all(0, 0, 0)
      neurons.led_strip.set_single(3, 255, 0, 0)
      time.sleep(1)
  
  @event.button_b_pressed
  def on_button_b_pressed():
      print("button b event successed")
      neurons.led_strip.set_effect(0, 8, (1,6,8,1,6,8,1,6,8))
      time.sleep(3)
      neurons.led_strip.set_effect(1, 8, (1,6,8,1,6,8,1,6,8))
      time.sleep(3)
      neurons.led_strip.set_effect(2, 8, (1,6,8,1,6,8,1,6,8))
      time.sleep(3)
      neurons.led_strip.set_effect(3, 8, (1,6,8,1,6,8,1,6,8))
      time.sleep(3)
      neurons.led_strip.set_effect(4, 8, (1,6,8,1,6,8,1,6,8))
      time.sleep(3)
      neurons.led_strip.set_effect(5, 8, (1,6,8,1,6,8,1,6,8))
      time.sleep(3)
  
  @event.button_c_pressed
  def on_button_c_pressed():
      print("button c event successed")
      neurons.led_strip.set_effect(0, 5, (1,1,1,1,1,1,1,1,1))
      time.sleep(3)
      neurons.led_strip.set_effect(1, 5, (1,1,1,1,1,1,1,1,1))
      time.sleep(3)
      neurons.led_strip.set_effect(2, 5, (1,1,1,1,1,1,1,1,1))
      time.sleep(3)
      neurons.led_strip.set_effect(3, 5, (1,1,1,1,1,1,1,1,1))
      time.sleep(3)
      neurons.led_strip.set_effect(4, 5, (1,1,1,1,1,1,1,1,1))
      time.sleep(3)
      neurons.led_strip.set_effect(5, 5, (1,1,1,1,1,1,1,1,1))
      time.sleep(3)
