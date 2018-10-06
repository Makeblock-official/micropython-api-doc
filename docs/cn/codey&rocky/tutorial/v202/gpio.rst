[Micropython]TPYBoard v202 GPIO的使用
====================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
--------------

- 学习在PC机系统中GPIO（General Purpose I/O Ports，即通用输入/输出端口）的使用方法
- 学会用TPYBoard接收GPIO的高低电平，控制板子上LED灯的发光与否

准备工作
----------------

- TPYBoard板子 1块
- micro USB数据线 1条
- 电脑 1台（本次实验以win7为例）
- 所需软件 ESPlorer

GPIO的介绍
----------------------

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170427/1493271806734258.png

GPIO（General Purpose I/O Ports）意思为通用输入/输出端口，通俗地说，就是一些引脚，可以通过它们输出高低电平或者通过它们读入引脚的状态-是高电平或是低电平。

上图标记1为一个小的LED灯，和板子上的G2接口相连，低电平时亮，高电平灭。通过GPIO输出高低电平，从而控制LED灯的发光与否。

实验方法
-----------------

第一步：下载安装所需的软件--ESPlorer

下载地址：http://www.tpyboard.com/download/tool/169.html

第二步：连接TPYBoard-esp8266开发板

通过USB数据线将电脑和TPYBoard-esp8266开发板连接起来，会自动安装USB转串的驱动。安装完毕后，查看设备管理器，是否正确创建串口。

.. image:: http://old.tpyboard.com/ueditor/php/upload/image/20170315/1489560644598749.png

第三步：双击ESPlorer的ESPlorer.jar，根据下图标记的红色框进行设置。

.. image:: http://old.tpyboard.com/ueditor/php/upload/image/20170315/1489560660603166.png

.. image:: http://old.tpyboard.com/ueditor/php/upload/image/20170315/1489560674907087.png

第四步：设置完成后，单击open按钮。

.. image:: http://old.tpyboard.com/ueditor/php/upload/image/20170315/1489560688651356.png

第五步：按下上记板子上标记的3，进行重置。

.. image:: http://old.tpyboard.com/ueditor/php/upload/image/20170315/1489560706861108.png

第六步：书写测试代码，点击Send to ESP进行测试。

.. image:: http://old.tpyboard.com/ueditor/php/upload/image/20170315/1489560724105195.png

运行结果：每隔3秒，LED灯进行<亮-灭>切换

.. image:: http://old.tpyboard.com/ueditor/php/upload/image/20170315/1489560910187276.png

.. image:: http://old.tpyboard.com/ueditor/php/upload/image/20170315/1489560920923300.png


源代码
----------------

.. code-block:: python

	from machine import Pin
	import time

	p2 = Pin(2, Pin.OUT)    # create output pin on GPIO2
	p2.value(1)             # set pin to high

	while True:
	  p2.low()                # set pin to low
	  p2.value()
	  time.sleep(3)           # sleep for 3 second
	  p2.high()               # set pin to high
	  p2.value()
	  time.sleep(3)           # sleep for 3 second


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v20x-master>`_
