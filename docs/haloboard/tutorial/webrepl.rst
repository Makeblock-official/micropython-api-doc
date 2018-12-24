.. __haloboard_tutorial_webrepl_index:

光环板上面的webrepl的开启与连接
=============================================

webrepl是micropython提供无线链接的管理平台。

步骤一：烧写固件
       确保好自己的固件已经烧好了即可。

步骤二：连接网络
       打开串口助手（如putty，secureCRT等等）,光环板与电脑之间使用USB连接好,按ctrl+e进入代码粘贴模式，将以下代码的ssid和password填写完整以后，粘贴在串口助手，然后ctrl+d运行代码。（注意：ssid为WiFi的名字、password为WiFi的密码）

.. code-block:: python

	import network
	import time 
	ssid=''
	password=''
	wlan=network.WLAN(network.STA_IF)
	wlan.active(True)
	wlan.connect(ssid,password)
	i=0

	while(wlan.ifconfig()[0]=='0.0.0.0' and i < 100):
	    i=i+1
	    time.sleep(1)
	    if(wlan.ifconfig()[0]=='0.0.0.0'):
	        print('connect Wifi False!')
	        #return False
	    else:
	        print('connect Wifi True!')
	        print(wlan.ifconfig())
	        #return True

.. image:: img/1.jpg
如上图所示，网络配置完成，输出模块IP地址。

步骤三：配置webrepl
	1.向串口中输入
.. code-block:: python

	import webrepl_setup

.. image:: img/2.jpg
如上图所示，向串口中输入 import webrepl_setup。

	2.输入 E 确定开启webrepl，连续输入两次密码即可完成配置
.. image:: img/3.jpg
如上图所示，输入两次密码。

	3.手动依次输入 import webrepl 和 webrepl.start() ，开启webrepl
.. image:: img/4.jpg
如上图所示，开启webrepl。

步骤四：连接webrepl
	1.打开webrepl的地址：http://micropython.org/webrepl/
.. image:: img/5.jpg
如上图所示，webrepl界面。

    2.输入第三步中的ip地址，点击Connect，输入配置时候的密码（注：密码在输入的时候不显示!）
.. image:: img/6.jpg
如上图所示，连接完成界面。

    3.可以输入help()尝试一下
.. image:: img/7.jpg

步骤五：配置开机连接WiFi和开启webrepl
	1.新建boot.py，内容如下
.. code-block:: python

	import time    

	ssid=''
	password=''

	def connectWifi():
	    wlan=network.WLAN(network.STA_IF)                     #create a wlan object
	    wlan.active(True)                                     #Activate the network interface
	    wlan.connect(ssid,password)   
	    i=0
	    while(wlan.ifconfig()[0]=='0.0.0.0' and i < 10):
	        i=i+1
	        time.sleep(1)
	        if(wlan.ifconfig()[0]=='0.0.0.0'):
	            print('connect Wifi False!')
	            return False
	        else:
	            print('connect Wifi True!')
	            print(wlan.ifconfig())
	            return True          
	if(connectWifi() == True):
	    import webrepl
	    webrepl.start()
注意：要将上代码的ssid和password填写完整。

	2.回到webrepl的网站界面，在右侧栏Send a file 下方点击 浏览 选择刚才写好的boot.py，点击Send to device，等待上传完成
.. image:: img/8.jpg
如上图所示，发送一个文件。

	3.输入ctrl+d或者断电重启光环板，重启完成后再次连接。
  		此时在打开webrepl的网站就能管理光环板，而不用串口线。
