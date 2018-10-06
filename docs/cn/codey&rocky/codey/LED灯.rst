:mod:`led` --- 板载全彩LED灯功能函数
=============================================

.. module:: led
   :synopsis: 板载全彩LED灯功能函数

``LED`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: show(r,g,b)

   设置并显示RGB LED灯的颜色, 参数：

  - *r* 全彩LED红色分量的数值，参数范围是 ``0 ~ 255``， 0为无红色分量，255是红色分量最亮。
  - *g* 全彩LED绿色分量的数值，参数范围是 ``0 ~ 255``， 0为无绿色分量，255是绿色分量最亮。
  - *b* 全彩LED蓝色分量的数值，参数范围是 ``0 ~ 255``， 0为无蓝色分量，255是蓝色分量最亮。


.. function:: set_red(val)

    设置 RGB LED灯的红色色值，参数：

    - *val* 全彩LED红色分量的数值，参数范围是 ``0 ~ 255``， 0为无红色分量，255是红色分量最亮。

.. function:: set_green(val)

    设置 RGB LED灯的绿色色值，参数：

    - *val* 全彩LED绿色分量的数值，参数范围是 ``0 ~ 255``， 0为无绿色分量，255是绿色分量最亮。
 
.. function:: set_blue(val)

    设置 RGB LED灯的蓝色色值，参数：

    - *val* 全彩LED红色分量的数值，参数范围是 ``0 ~ 255``， 0为无蓝色分量，255是蓝色分量最亮。
 
.. function:: off()

    熄灭LED灯

程序示例：
------------

.. code-block:: python

import codey
import time

codey.led.show(2555,255,255)
time.sleep(2)
codey.led.off()
time.sleep(2)
while True:
    codey.led.set_red(255)
    time.sleep(1)
    codey.led.set_green(255)
    time.sleep(1)
    codey.led.set_blue(255)
    time.sleep(1)
    codey.led.off()
    time.sleep(1)
