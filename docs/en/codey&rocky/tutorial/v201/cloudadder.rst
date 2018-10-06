[Micropython]TPYBoard v201 建立云加法器
==========================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明


引言
---------------
前面的一篇文档向大家介绍了v201的开发板作为客户端终端向TCPS上传数据的基本过程，这次向大家简单介绍一下怎样使用V201开发板搭建一台简易的服务器做远程云加法器。

实验器件
--------------

  - TPYBoard v201开发板 1块

TPYBoard v201开发板简介
---------------------------

TPYBoard v201是以遵照MIT许可的MicroPython为基础，由TurnipSmart公司制作的一款MicroPython开发板，它基于STM32F405单片机，通过USB接口进行数据传输。该开发板内置4个LED灯、板载V201网口功能，可在3.3V-10V之间的电压正常工作。可以说这个开发板在网络稳定方面是一霸也不为过，板上其他硬件资源也非常丰富，像单总线，i2c，spi，串口等接口也是应有尽有，这次我们就要用到串口的功能。

环境搭建
---------------------------
上面介绍了所需器件，下面我们来说一下实验所需的环境。这里只需要能给开发板供电，以及可以支持有线网络连接（可以给开发板接上网线）即可。
开发板接通电源插入网线后，可以看到v201网口上的绿色指示灯亮起来，说明已经连接上网络。

配置v201网口
-----------------

这一步是为了设置v201网口模块的目的地址，本地端口，波特率，数据位，校验位等一系列信息，具体配置方向详见： `TPYBoard相关下载(USR-K2) <https://github.com/TPYBoard/Documentation/blob/master/tpyboard_docs/tpyboard/tutorial/doc/USR-K2资料.rar>`_ 。

接着我们来说一下基本的逻辑流程：

1.确认供电和网络完好；

2.确认网络完好，接下来就是进行传输和处理，在保证网络通畅的前提下，设置串口6，也就是Y1(TX)和Y2(RX)，波特率与设置的v201的波特率保持一致；

3.在这里需要说一句的是，这个开发板在使用以太网功能的时候，Y1，Y2，Y3这三个引脚是被占用的，其中Y1和Y2是串口，执行通信功能；

4.这里需要介绍一下Y3，Y3是V201网口的配置引脚，当Y3为高电平时，v201网口处于正常工作状态，可以进行数据透传，可以利用设置软件通过网络进行配置。当Y3为低电平时，V201网口进入串口配置模式，可利用设置软件通过串口进行配置，此时不能进行数据上传；

5.以上工作全部完成后，剩下的就是时刻监控串口6是否有数据；

6.当第一收到数据的时候，把计数变量加一，并利用寄存变量保存数据；

7.当第二次收到数据之后，把计数变量加一，并利用寄存器变量保存数据；

8.当判断到计数变量为二时，把两次收到的数据相加；

9.最后我们只需要把两次相加的结果从串口6发送出去即可。


实物及数据图
---------------------

下面是我做实验的实物图和数据监控截图，我是在我的电脑上开了个模拟的客户端口，虽然low了点，但是效果一样的。

实物图

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20170415/1492221696685070.jpg

数据监控截图

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20170415/1492221741955689.png



源代码
------------

下面是我做的源代码，共享给大家。

.. code-block:: python

	import pyb
	from pyb import UART
	from pyb import Pin
	from ubinascii import hexlify
	from ubinascii import *

	ulan = UART(6, 9600, timeout = 100)#定义连接网口的串口
	K=1
	jia=0
	jie1=0
	he=0
	js=0#设置寄存变量
	#*******************************主程序**********************************
	print('while')
	while (K>0):
		_dataRead=ulan.readall()#读取客户端数据
		if _dataRead!=None:#判断客户端是否传来数据
			print(_dataRead)
			js=js+1#计数判断执行命令标志
			if(js==1):
				jia=_dataRead.decode('utf-8')#数据转换
				jia=int(jia)#数据转换
				print(jia)
			if(js==2):
				jia1=_dataRead.decode('utf-8')
				jia1=int(jia1)
				print(jia1)
			if(js==2):
				he=jia+jia1
				js=0
				ulan.write(str(jia)+'+'+str(jia1)+'='+str(he)+'\r\n')#计算结果返回给客户端



- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v20x-master/>`_
