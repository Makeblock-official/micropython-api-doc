[Micropython]TPYBoard v202 Network连接网络
================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
-------------

- 学习在PC机系统中网络（network）的使用方法
- 学习TPYBoard V202连接网络的使用

准备工作
-------------

- TPYBoard v202 1块
- micro USB数据线 1条
- 电脑 1台（本次实验以win7为例）
- 所需软件 ESPlorer `点击下载 <http://www.tpyboard.com/download/tool/169.html>`_

**Network库的使用方法**

网络模块用于配置WiFi连接。一共两种模式，模式一:是TPYBoard v202当STA节点，即连接路由器的节点。模式二，是TPYBoard v202做为AP，充当路由。

**TPYBoard v202 STA节点模式**

.. code-block:: python

	import network
	wlan = network.WLAN(network.STA_IF)      # 创建一个站（当ESP8266连接到路由器时）接口
	wlan.active(True)                          # 激活接口
	wlan.scan()                                 # 扫描接入点
	wlan.isconnected()                         # 检查站点是否连接到路由器
	wlan.connect('essid', 'password')        # 连接到路由器
	wlan.config('mac')      # 获取接口的MAC地址
	wlan.ifconfig()         # 获取接口的IP / netmask / gw / DNS地址

	#检查是否连接是否建立:
	wlan.isconnected()
	#检查接口是否活动：
	wlan.active()
	#检查接口的网络设置：
	wlan.ifconfig()

TPYBoard v202自动连接本地网络:

.. code-block:: python

	from machine import Pin
	import network
	import time
	def led_state():
		p2 = Pin(2, Pin.OUT)
		p2.value(0)
		time.sleep_ms(500)
		p2.value(1)
		time.sleep_ms(500)
		p2.value(0)
		time.sleep_ms(500)
        p2.value(1)
		time.sleep_ms(500)
	def do_connect():
		sta_if = network.WLAN(network.STA_IF)
		p2 = Pin(2, Pin.OUT)
		sta_if.active(False)
		if not sta_if.isconnected():
			p2.low()
			print('connecting to network...')
			sta_if.active(True)
			sta_if.connect('TurnipSmart', 'turnip2016')
			while not sta_if.isconnected():
				pass
		if sta_if.isconnected():
			print('connect success')
			led_state()
			print('network config:', sta_if.ifconfig())
	do_connect()

只需要将上面代码写入boot.py,在开发板上电后，就看到蓝灯常亮（正在连接网络），然后蓝灯交替闪烁两次，控制台打印connect success，证明已经连接到本地网络。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489562186715918.png

**TPYBoard v202 AP模式**

.. code-block:: python

	import network
	ap = network.WLAN(network.AP_IF) ＃创建接入点接口
	ap.active(True)         # 激活接口
	ap.config(essid='ESP-AP') # 设计接入点的ESSID


向指定地址发送数据的方法：

.. code-block:: python

	def http_get(url):
		_, _, host, path = url.split('/', 3)
		addr = socket.getaddrinfo(host, 80)[0][-1]
		s = socket.socket()
		s.connect(addr)
		s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
		while True:
			data = s.recv(100)
			if data:
				print(str(data, 'utf8'), end='')
			else:
				break
		s.close()

实验一
----------

**实验要求**

当TPYBoard v202未连接到网络时，led亮起警示，当连接成功后，熄灭。

main.py程序代码

.. code-block:: python

	import network
	from machine import Pin
	sta_if = network.WLAN(network.STA_IF)
	p2 = Pin(2, Pin.OUT)
	#我们在这里把接入点接口禁用，方便观看实验效果，非实验可以去掉
	sta_if.active(False)
	if not sta_if.isconnected():
		p2.low()
		print('connecting to network...')
		sta_if.active(True)
		sta_if.connect('TurnipSmart', 'turnip2016')
		while not sta_if.isconnected():
			pass
	if sta_if.isconnected():
		print('connect success')
		p2.high()
		print('network config:', sta_if.ifconfig())

**实验效果**

当我们复位，把程序写进去的时候会看到TPYBoard V202板载的蓝灯亮起来，当连接成功后蓝灯熄灭，控制台打印connect success。

实验二
-----------

**实验要求**
当TPYBoard v202连接网络成功后，通过get方式向网址http://www.tpyboard.com/esp8266/test.php?val=A

发送字符A,网站接到后，页面显示begin，并返回bigin，TPYBoard V202收到bigin，LED快闪2次。

main.py程序代码

.. code-block:: python

	import network
	from machine import Pin
	import socket
	import urllib
	import time

	def led_state():
		p2 = Pin(2, Pin.OUT)
		p2.value(0)
		time.sleep_ms(500)
		p2.value(1)
		time.sleep_ms(500)
		p2.value(0)
		time.sleep_ms(500)
		p2.value(1)

	def do_connect():
		sta_if = network.WLAN(network.STA_IF)
		p2 = Pin(2, Pin.OUT)
		sta_if.active(False)
		if not sta_if.isconnected():
			p2.low()
			print('connecting to network...')
			sta_if.active(True)
			sta_if.connect('TurnipSmart', 'turnip2016')
			while not sta_if.isconnected():
				pass
		if sta_if.isconnected():
			print('connect success')
			p2.high()
			print('network config:', sta_if.ifconfig())

	def http_get(url):
		_, _, host, path = url.split('/', 3)
		addr = socket.getaddrinfo(host, 80)[0][-1]
		s = socket.socket()
		s.connect(addr)
		s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
		while True:
			data = s.recv(50)
			if data:
				recive=str(data, 'utf8')
				#print('recive:',recive)
				print(str(data, 'utf8'), end='')
				if(recive.find('begin')>-1):
				   led_state()
			else:
				break
		s.close()
	do_connect()
	http_get('http://www.tpyboard.com/esp8266/test.php?val=A')

**实验效果**

当点击Send to ESP时，控制台显示从页面上传过来的内容为begin，并且led灯交替闪烁两次。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489562363252568.png

当访问的网址 http://www.tpyboard.com/esp8266/test.php?val=X
后面参数不是A的时候，页面会提示 This is not ‘A’。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489562400709859.png


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v20x-master>`_
