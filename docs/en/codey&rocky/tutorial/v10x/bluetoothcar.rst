[Micropython]TPYBoard v10x 无线蓝牙智能小车
============================================

原创版权归山东萝卜科技有限公司所有,转载必须以链接形式注明作者和原始出处。

实验目的
-----------------

	- 学习在PC机系统中扩展简单I/O 接口的方法。
	- 进一步学习编制数据输出程序的设计方法。
	- 学习蓝牙模块的接线方法及其工作原理。
	- 学习 L298N电机驱动板模块的接线方法。
	- 学习蓝牙控制小车的工作原理。

所需元器件
------------------

	- TPYBoard v102板子 1块
	- 蓝牙串口透传模块(HC-06) 1个
	- L298N电机驱动板模块 1个
	- 智能小车底盘 1个
	- 数据线 1条
	- 杜邦线 若干

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161215/1481791277901030.jpg

蓝牙串口模块原理
--------------------------

(1)引出接口包括EN,5V,GND,TX,RX,STATE,我们小车只用到RX,TX,GND,5V四个针脚

(2)模块默认波特率位9600，默认配对密码为1234，默认名称位为HC-06

(3)led指示蓝牙连接状态，闪烁表示没有蓝牙连接，常亮表示蓝牙已连接并打开了端口，当我们用安卓手机软件发送指令时,通过串口给TPYBoard发送指令，TPYBoard收到指令通过L298BN模块来驱动小车前进，后退，向左，向右或者停止。

如下图接线，5V 接TPYBoard的VIN， GND 为地线，TX接TPYBoard的RX（这用的是TPYBoard串口2,X3，X4）即X4，RX接TPYBoard的TX即X3

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161215/1481791173622577.png

学习L298N电机驱动板模块的接线方法
----------------------------------------

本模块是2路的H桥驱动，所以可以同时驱动两个电机，接法如图所示使能ENA ENB之后，可以分别从IN1 IN2输入PWM信号驱动电机1的转速和方向，可以分别从IN3 IN4输入PWM信号驱动电机2的转速和方向。我们将电机1接口的OUT1与OUT2与小车的一个电机的正负极连接起来，将电机2接口的OUT3与OUT4与小车的另一个电机的正负极连接起来。然后将两边的接线端子，即供电正极（中间的接线端子为接地）连接TPYboard的VIN，中间的接线端子即接地，连接TPYBoard的GND，In1-In4连接TPYBoard的Y1，Y2，Y3，Y4，通过Y1,Y2与Y3,Y4的高低电平，来控制电机的转动，从而让小车前进，后退，向左，向右。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161215/1481791212316208.jpg

接线OK后，编写main.py，给TPYBoard通电就ok了，下面是源代码。

源代码
--------------------

.. code-block:: python

	import pyb
	from pyb import UART
	from pyb import Pin

	M2 = Pin('X3', Pin.IN)
	M3 = Pin('X4', Pin.IN)
	N1 = Pin('Y1', Pin.OUT_PP)
	N2 = Pin('Y2', Pin.OUT_PP)
	N3 = Pin('Y3', Pin.OUT_PP)
	N4 = Pin('Y4', Pin.OUT_PP)

	u2 = UART(2, 9600 , timeout = 100)

	while True:
		pyb.LED(2).on()
		pyb.LED(3).on()
		pyb.LED(4).on()
		_dataRead=u2.read()
		if _dataRead!=None:
		#停止（读取手机APP传过来的指令，不同的软件指令可能不同，可以自己设定，在这里是默认的，下同）
			if(_dataRead.find(b'\xa5Z\x04\xb1\xb5\xaa')>-1):
				print('stop')
				N1.low()
				N2.low()
				N3.low()
				N4.low()
			#向左
			elif(_dataRead.find( b'\xa5Z\x04\xb4\xb8\xaa')>-1):
				print('left')
				N1.low()
				N2.high()
				N3.high()
				N4.low()
			#向右
			elif(_dataRead.find( b'\xa5Z\x04\xb6\xba\xaa')>-1):
				print('right')
				N1.high()
				N2.low()
				N3.low()
				N4.high()
			#后退
			elif(_dataRead.find(b'\xa5Z\x04\xb5\xb9\xaa')>-1):
				print('back')
				N2.high()
				N1.low()
				N4.high()
				N3.low()
			#向前
			elif(_dataRead.find( b'\xa5Z\x04\xb2\xb6\xaa')>-1):
				print('go')
				N1.high()
				N2.low()
				N3.high()
				N4.low()

- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
