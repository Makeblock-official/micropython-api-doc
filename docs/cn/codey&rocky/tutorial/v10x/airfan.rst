[Micropython]TPYBoard v10x DIY智能温控小风扇
=============================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明


实验目的
---------------

   - 学习在PC机系统中扩展简单I/O 接口的方法。
   - 进一步学习编制数据输出程序的设计方法。
   - 学习DS18B20的接线方法，并利用DS18B20检测当前温度。
   - 学习三极管9014的用法。
   - 通过18B20智能控制直流电机驱动小风扇。

所需元器件
------------------

   - TPYBoard v102板子 1块
   - 直流电机 1个
   - 面包板 1块
   - 数据线 1条
   - 三极管9014（NPN）1个
   - 杜邦线 若干

学习DS18B20的接线方法
-------------------------------------

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20161125/1480062707271272.png


先看一下DS18B20针脚含义,如上图：

TPYBoard v102的针脚与DS18B20的针脚对应关系如下：

	+-----------+------------+
	| TPYBoard  | DS18B20    |
	+===========+============+
	| 3.3v      | VDD        |
	+-----------+------------+
	| GND       | GND        |
	+-----------+------------+
	| Y10       | DO         |
	+-----------+------------+

接线OK后，在MicroPython的源码目录中，进入drivers\onewire\目录，然后将目录下的文件ds18x20.py和onewire.py复制到PYBFLASH磁盘的根目录。复制文件后要安全退出磁盘，然后重新接入，不然找不到文件，即可运行main.py文件了，打印温度，即可用Putty看到当前的温度。

main.py源代码：

.. code-block:: python

	#main.py
	import pyb
	from pyb import Pin
	from ds18x20 import DS18X20

	Pin("Y11",Pin.OUT_PP).low()#GND
	Pin("Y9",Pin.OUT_PP).high()#VCC
	pyb.delay(100)
	DQ=DS18X20(Pin('Y10'))#DQ
	while True:
	   tem = DQ.read_temp()
	   print(tem)
	   pyb.delay(1000)

三极管的原理
--------------------------

.. image:: http://tpyboard.com/ueditor/php/upload/image/20161125/1480063045583790.png


在这里我们用到三极管的开关与放大功能，给基极不同电平控制直流电机电流的通断，以达到控制电机转动的目的，根据三极管特性我们将集电极连接TPYBoard的3.3v，发射极连接电机一极，电机另一极接TPYboard的GND，通过温度传感器18B20检测温度，当温度到达指定温度时,通过TPYBoard控制三极管基极的电平，驱动直流电机转动。


效果图
----------------

.. image:: http://tpyboard.com/ueditor/php/upload/image/20161125/1480063122271025.png


源代码
----------------

我们按照上面的步骤做完以后，然后通电，编写main.py文件，即可通过温度控制风扇的转动，具体代码如下：

.. code-block:: python

	#main.py
	import pyb
	from pyb import Pin
	from ds18x20 import DS18X20

	Pin("Y9",Pin.OUT_PP).high()#VCC
	Pin("Y11",Pin.OUT_PP).low()#GND
	x1 = Pin('X1', Pin.OUT_PP)
	pyb.delay(100)
	DQ=DS18X20(Pin('Y10'))#DQ
	while 1:
		tem = DQ.read_temp()
		if tem > 18:
			x1.value(1)
		else:
			x1.value(0)

- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
