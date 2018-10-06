[Micropython]TPYBoard v202 定时器
================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
-------------

    - 学习使用定时器功能

所需元器件
--------------

    - TPYBoard v102开发板 1块
    - micro USB数据线 1条

实现方法
---------------

**增加一个执行一次的定时器**

.. code-block:: python

    from machine import Timer
    tim = Timer(-1)  #新建一个虚拟定时器
    #此处执行时程序会等待5秒打印1，period=5000 以毫秒为单位，mode=Timer.ONE_SHOT 表示只执行一次，callback绑定回调函数
    tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))

**增加一个循环定时器**

.. code-block:: python

    from machine import Timer
    tim = Timer(-1)  #新建一个虚拟定时器
    #此方法执行时系统会每隔两秒无限打印2
    tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))


利用定时器来获取温湿度
-----------------------------

**硬件实物图**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489561580775098.png

只需要将DHT11温湿度传感器的针脚与TPYBoard v202针脚连接起来即可，本次实验我们将DHT11的VCC连接TPYBoard v202的5V,DHT11的DATA连接TPYBoard v202的G4，DHT11的GND连接TPYBoard v202的GND，连接完成后，将下面代码写进TPYBoard v202即可读取当前温湿度的值，下面是源代码:

.. code-block:: python

	from machine import Timer
	import dht
	import machine
	def f(t):
		d=dht.DHT11(machine.Pin(4))
		d.measure()
		a=d.temperature()
		b=d.humidity()
		print('温度:',a,'°C')
		print('湿度:',b,'%')

	tim = Timer(-1)  #新建一个虚拟定时器
	tim.init(period=2000, mode=Timer.PERIODIC, callback=f)

用串口调试工具每2秒读取一次温湿度，并打印见下图:

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489561615972014.png

若想做一下扩展，可将温湿度显示到OLED显示屏上，这样一个小型的DIY温湿度检测仪就诞生了。


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v20x-master>`_
