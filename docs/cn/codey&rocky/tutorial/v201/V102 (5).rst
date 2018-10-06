[Micropython]TPYBoardV201 K2网口配置使用文档
=================================================

原创版权归山东萝卜科技有限公司所有,转载必须以链接形式注明作者和原始出处。

超级网口 V201网口 用于实现串口到以太网口的数据的双向透明转发，用户无需关心具体细节，模块内部完成协议转换，通过简单设置即可设定工作细节。参数可以通过模块内部的网页进行设置，也可以通过设置软件进行设置，一次设置永久保存。

下面简单介绍一下软件配置的方法。

用户需要预设的参数有：

1.工作模式：TCP Client、TCP Server、UDP Client、UDP Server

2.默认 TCP/UDP连接参数

3.连接类型（Server或Client）

4.目标端口

5.目标IP地址

6.本地端口

7.串口参数

8.波特率

9.数据位

10.检验位

11.停止位

12.RS485等功能的选择

13.IP地址和模块密码等

14.IP地址获取方式

15.模块名称、用户名和密码的设置

用户配置完所有参数后重启，模块就可以按照设置的参数工作了。

使用软件配置分为网络操作和串口操作两种，下面分别介绍。

我们使用的配置软件为USR-M0-Series_V2.0.1.521。`点击下载 <https://github.com/TPYBoard/Documentation/blob/master/tpyboard_docs/tpyboard/tutorial/doc/USR-K2资料.rar>`_

图标如图。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170415/1492219608161569.png

一、通过网络配置
-------------------------

1.第一步是给整个开发板供电，使用双头usb数据，连接电脑和开发板；

2.第二步从路由器上引出一根网线插在开发板的网口上；

3.打开配置软件，界面如图

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170415/1492219619821144.png

4.点击搜索设备，出现如图，这里可以在设备名称的地方看到V201网口这个设备，

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170415/1492219666274759.png

5.点击选择V201网口这个设备，如图

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170415/1492219680890988.png

6.这里我们需要在端口设置里面进行各个参数的设置，然后点击保存参数，结果如图

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170415/1492219702772241.png

二、串口设置
-------------------------------

1.使用串口设置前需要有一个TTL转串口模块，并按如下表格对应接线

.. image:: images/c2.png

2.在完成以上接线后，使用杜邦线把Y3与GND短接；

3.给开发板供电；

4.在TTL转串口模块正确连接电脑与开发板之后，打开配置软件；

5.选择通过串口操作，如图

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170415/1492219789194685.png

6.按照上图中进行项目选择，结果如图

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170415/1492219808554216.jpg

7.这样就可以进行目的IP和本地端口等参数的设置了，具体设置参照网络设置；

8.设置完成后，点击保存即可。