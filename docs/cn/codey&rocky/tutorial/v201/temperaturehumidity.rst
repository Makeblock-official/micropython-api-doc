[Micropython]TPYBoard v201 温湿度数据上传
=======================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

引言
-------------------------

历来关于温湿度的检测都是没有间断过的，这次我们继续检测温湿度，同样还是使用DHT11来检测。但是这次检测到的温湿度不进行显示，也不进行报警，这次要把检测到的数据通过以太网上传到服务器上去。

所需器材
-------------------------

  - TPYBoard v201开发板 1块
  - DHT11温湿度模块 1个
  - 面包板 1个
  - 杜邦线 若干

**DHT11 简介**

DHT11数字温湿度传感器是一款含有已校准数字信号输出的温湿度复合传感器，它应用专用的数字模块采集技术和温湿度传感技术，确保产品具有极高的可靠性和卓越的长期稳定性。传感器包括一个电阻式感湿元件和一个NTC测温元件，并与一个高性能8位单片机相连接。


接线说明
----------------------

	+-----------+-------------+
	| DHT11V201 | 开发板      |
	+===========+=============+
	| GND       | GND         |
	+-----------+-------------+
	| VCC       | VIN         |
	+-----------+-------------+
	| DATA      | X8          |
	+-----------+-------------+

配置 v201网口
-------------------

详细的配置说明详见上一篇教程
http://docs.tpyboard.com/zh/latest/tpyboard/tutorial/v201/cloudadder.html#v201

实物图

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20170415/1492220610497650.jpg
    :width: 400px

数据监控图

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20170415/1492220644727630.png
    :width: 400px

源代码
----------

下面是源代码，共享给大家。

.. code-block:: python

  import pyb
  from pyb import UART
  from pyb import Pin
  from ubinascii import hexlify
  from ubinascii import *
  from dht11 import DHT11#定义温湿度传感器的库

  ulan = UART(6, 115200,timeout = 100)#定义串口，我的网口设置了115200的波特率
  K=1
  #*******************************主程序**********************************
  print('while')
  while (K>0):
      #init DHT11
      dht=DHT11('X8')
      data_=dht.read_data()#读取温湿度的值
      temp=str(data_[0])#温度
      hum=str(data_[1])#湿度
      print('temp:'+temp)
      print('hum:'+hum)
      ulan.write('temperature is:'+temp+'\r\n')#上传温度
      pyb.delay(2000)#做延时是为了让给模拟服务器一个反应时间
      ulan.write('wet is:'+hum+'%'+'\r\n')#上传湿度
      pyb.delay(12000)


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v20x-master/>`_
