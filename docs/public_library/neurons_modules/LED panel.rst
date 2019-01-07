:mod:`led_panel` --- LED面板模块
=============================================

.. module:: led_panel
    :synopsis: LED面板模块

``led_panel`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: set_all(red_value, green_value, blue_value)

   设置并显示整个LED面板的颜色, 参数：

    - *red_value* 全彩LED红色分量的数值，参数范围是 ``0 ~ 255``， 0为无红色分量，255是红色分量最亮。
    - *green_value* 全彩LED绿色分量的数值，参数范围是 ``0 ~ 255``， 0为无绿色分量，255是绿色分量最亮。
    - *blue_value* 全彩LED蓝色分量的数值，参数范围是 ``0 ~ 255``， 0为无蓝色分量，255是蓝色分量最亮。

.. function:: set_pixel(x, y, red_value, green_value, blue_value)

   设置LED面板单个像素点的颜色，参数：

    - *x* 像素点在表情面板上x轴的坐标，参数范围是 ``0 ~ 7``。
    - *y* 像素点在表情面板上y轴的坐标，参数范围是 ``0 ~ 7``。
    - *red_value* 全彩LED红色分量的数值，参数范围是 ``0 ~ 255``， 0为无红色分量，255是红色分量最亮。
    - *green_value* 全彩LED绿色分量的数值，参数范围是 ``0 ~ 255``， 0为无绿色分量，255是绿色分量最亮。
    - *blue_value* 全彩LED蓝色分量的数值，参数范围是 ``0 ~ 255``， 0为无蓝色分量，255是蓝色分量最亮。

.. function:: show_image(list, mode = 0)

   以图片参数的方式设置显示的内容，参数：

    - *list* 可变参数列表，每个数值的参数范围是 ``0 ~ 8``，第1个参数表示第一个灯的颜色，第2个参数表示第二个灯的颜色...，颜色的参数如下： ``黑(0x00)``，``红(0x01)``，``橙(0x02)``，``黄(0x03)``，``绿(0x04)``，``青(0x05)``，``蓝(0x06)``，``紫(0x07)``，``白(0x08)``。
    - *mode* 显示内容的呈现方式，参数范围是 ``0 ~ 3``，其中

     0：表示显现模式，直接将设定的图案显示出来。

     1：表示擦除模式，原图像按竖列逐渐消失，同时设定的图像按竖列逐渐显现出来。

     2：表示左移模式，原图像向左移动消失，设定的图像向左移动显现出来

     3：表示右移模式，原图像向右移动消失，设定的图像向右移动显现出来

.. function:: set_animation(frame_index, list)

   设置LED面板的动画帧内容，参数：

    - *frame_index* 动画帧的帧序列，参数范围是 ``0 ~ 3``，0表示第一帧。
    - *list* 可变参数列表，每个数值的参数范围是 ``0 ~ 8``，第1个参数表示第一个灯的颜色，第2个参数表示第二个灯的颜色...，颜色的参数如下： ``黑(0x00)``，``红(0x01)``，``橙(0x02)``，``黄(0x03)``，``绿(    04)``，``青(0x05)``，``蓝(0x06)``，``紫(0x07)``，``白(0x08)``。

.. function:: show_animation(frame_speed, mode)

   显示 ``set_animation`` 设定的动画帧内容，参数：

    - *frame_speed* 动画帧的切换速度，参数范围是 ``0 ~ 2``，其中

     0：表示慢速，1秒的滚动间隔。

     1：表示正常，0.5秒的滚动间隔。

     2：表示快速，0.2秒的滚动间隔。

    - *mode* 帧变化的模式，参数范围是 ``0 ~ 3``，其中

     0：表示显现模式，直接将设定的图案显示出来。

     1：表示擦除模式，原图像按竖列逐渐消失，同时设定的图像按竖列逐渐显现出来。

     2：表示左移模式，原图像向左移动消失，设定的图像向左移动显现出来

     3：表示右移模式，原图像向右移动消失，设定的图像向右移动显现出来

.. function:: show_string(red_value, green_value, blue_value, list)

   按指定颜色显示字符串，参数：

    - *red_value* 全彩LED红色分量的数值，参数范围是 ``0 ~ 255``， 0为无红色分量，255是红色分量最亮。
    - *green_value* 全彩LED绿色分量的数值，参数范围是 ``0 ~ 255``， 0为无绿色分量，255是绿色分量最亮。
    - *blue_value* 全彩LED蓝色分量的数值，参数范围是 ``0 ~ 255``， 0为无蓝色分量，255是蓝色分量最亮。
    - *list* 可变参数列表，第1个字符，第2个字符...

.. function:: clear()

   清除面板的显示，即所有LED灯珠都熄灭。

程序示例：
------------

.. code-block:: python

  import codey
  import neurons
  import event
  import time
  
  neurons.led_panel.clear()
  neurons.led_panel.set_all(0, 0, 255)
  time.sleep(1)
  neurons.led_panel.clear()
  
  @event.button_a_pressed
  def on_button_a_pressed():
      print("button a event successed")
      neurons.led_panel.set_pixel(0, 0, 255, 0, 0)
      time.sleep(1)
      neurons.led_panel.set_pixel(4, 4, 255, 0, 0)
      time.sleep(1)
      neurons.led_panel.set_pixel(7, 7, 255, 0, 0)
      time.sleep(1)
      neurons.led_panel.set_pixel(0, 6, 255, 0, 0)
      time.sleep(1)
  
  @event.button_b_pressed
  def on_button_b_pressed():
      print("button b event successed")
      neurons.led_panel.show_image([1,6,8,0,0,0,1,6,8],0)
      time.sleep(1)
      neurons.led_panel.show_image([1,1,1,1,1,1,1,1,1],1)
      time.sleep(1)
      neurons.led_panel.show_image([6,6,6,6,6,6,6,6,6],2)
      time.sleep(1)
      neurons.led_panel.show_image([8,8,8,8,8,8,8,8,8],3)
      time.sleep(1)
  
  @event.button_c_pressed
  def on_button_c_pressed():
      print("button c event successed")
      neurons.led_panel.set_animation(0, (1,6,8,1,6,8,0,0,0))
      neurons.led_panel.set_animation(1, (6,6,6,6,6,6,6,6,6))
      neurons.led_panel.set_animation(2, [6,6,6,6,6,6,6,6,6])
      neurons.led_panel.set_animation(3, (8,8,8,8,8,8,8,8,8))
      neurons.led_panel.show_animation(1, 2)
      time.sleep(6)
      neurons.led_panel.show_string(255, 0, 0, "hello")
      time.sleep(4)
      neurons.led_panel.show_string(255, 0, 0, (100))
      time.sleep(4)
      neurons.led_panel.show_string(255, 0, 0, (1,2,3))
      time.sleep(4)
