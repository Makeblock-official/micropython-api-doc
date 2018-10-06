[Micropython]TPYBoard v10x DIY温度计
=====================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
------------------

 	- 学习在PC机系统中扩展简单I/O 接口的方法。
 	- 进一步学习编制数据输出程序的设计方法。
 	- 学习DS18B20的接线方法，并利用DS18B20检测当前温度
 	- 学习8*8LED点阵接线方法，并将当前温度显示

所需元器件
------------------

 	- TPYBoard v102开发板 1块
 	- micro USB数据线 1条
 	- 杜邦线 若干
 	- 8*8LED点阵屏 1个
 	- DS18B20温度传感器 1个

学习DS18B20的接线方法
----------------------------------------

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20160815/1471247227119424.png


先看一下DS18B20针脚含义,如上图：

TPYBoard的针脚与DS18B20的针脚对应关系如下：

+------------+---------+
| TPYBoard   | DS18B20 |
+============+=========+
| 3V3/Pin    | VDD     |
+------------+---------+
| Pin        | DO      |
+------------+---------+
| GND        | GND     |
+------------+---------+

还是看不明白? 直接上针脚编号

+------------+---------+
| TPYBoard   | LCD5110 |
+============+=========+
| 3.3v       | VDD     |
+------------+---------+
| GND        | GND     |
+------------+---------+
| Y10        | DO      |
+------------+---------+

接线OK后，找到MicroPython的源码目录中，进入drivers\onewire\目录，然后将目录下的文件ds18x20.py和onewire.py复制到TPYBFLASH磁盘的根目录。
复制文件后要安全退出磁盘，然后重新接入，即可运行main.py文件了。通过Putty可查看打印的温度信息。

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

控制8*8LED点阵显示温度
----------------------

.. image:: http://tpyboard.com/ueditor/php/upload/image/20160815/1471247464571951.png


点阵后面有两排针脚，一排以1开头，即1-8针脚，一排以9开头，即9-16针脚，上图中圆圈内的数字即为针脚的对应数字。当ROW 的针脚为高电平，COL的针脚为低电平时候，我们的LED即全部点亮。
为了方便操作行和列，我们可以将ROW的8个引脚接到我们TPYBoard v102的X1-X8，COL的8个引脚接到我们TPYBoard v102的Y1-Y8。这样我们通过控制X引脚和Y引脚的高低电平就可以控制每一个LED的亮与不亮，这样就可以设计想显示的任何字符和图形，快来试试吧。

将温度显示在8*8LED点阵上
--------------------------------

接线成功以后，我们将测试出温度通过分割函数将十位，个位显示在点阵屏上，代码如下：

.. code-block:: python

	import pyb
	from pyb import Pin
	from ds18x20 import DS18X20
	x_PIN = [Pin(i, Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7','X8']]
	y_PIN = [Pin(i, Pin.OUT_PP) for i in ['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8']]
	temp=['0000,0110,0110,0110,0110,0110,0110,0000','1101,1101,1101,1101,1101,1101,1101,1101,
	'0000,1110,1110,0000,0111,0111,0111,0000','0000,1110,1110,0000,1110,1110,1110,0000',
	'0101,0101,0101,0000,1101,1101,1101,1101','0000,0111,0111,0000,1110,1110,1110,0000',
	'0000,0111,0111,0000,0110,0110,0110,0000','0000,1110,1110,1110,1110,1110,1110,1110',
	'0000,0110,0110,0000,0110,0110,0110,0000','0000,0110,0110,0000,1110,1110,1110,0000']
	tempValue=0
	def show(l_num,r_num):
		flag=0
		for x_ in range(0,8):
			for x_ in range(0,8):
				if x_!=flag:
					x_PIN[x_].value(0)
			left_ = temp[l_num]
			left_item=left_.split(',')
			right_ = temp[r_num]
			right_item=right_.split(',')
			li_l=left_item[flag]
			li_r=right_item[flag]
			y_PIN[0].value(int(li_l[:1]))
			y_PIN[1].value(int(li_l[1:2]))
			y_PIN[2].value(int(li_l[2:3]))
			y_PIN[3].value(int(li_l[3:4]))
			y_PIN[4].value(int(li_r[:1]))
			y_PIN[5].value(int(li_r[1:2]))
			y_PIN[6].value(int(li_r[2:3]))
			y_PIN[7].value(int(li_r[3:4]))
			x_PIN[flag].value(1)
			flag=flag+1
			pyb.delay(2)
	def display(time_,l_num,r_num):
		for x in range(0,time_):
			for y in range(0,110):
				show(l_num,r_num)
	if __name__=='__main__':
		#time_t=Timer(4,freq=5,callback=randSensor)
		DQ=DS18X20(Pin('Y10'))#DQ
		while 1:
			tempValue =int(DQ.read_temp())
			print(tempValue)
			l_n=tempValue//10
			r_n=tempValue%10
			print(l_n)
			print(r_n)
			display(60,l_n,r_n)
			for i in x_PIN:
				i.value(0)

- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
