[Micropython]TPYBoard v10x DIY声光控小夜灯
==========================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
------------------

- 学习在PC机系统中扩展简单I/O 接口的方法。
- 进一步学习编制数据输出程序的设计方法。
- 学习光敏模块的工作原理。
- 学习声音的工作原理。
- 学习TPYboard与声音传感器与光敏传感器的接线方法以及利用声音与光控制发光二极管亮灭。

所需元器件
-----------------

- TPYBoard v102板子 1块
- 声音传感器 1个
- 光敏传感器 1个
- 面包板 1块
- 发光二极管 若干
- micro USB数据线 1条
- 杜邦线 若干

光敏传感器模块工作原理
-----------------------------

1.光敏电阻模块对环境光线最敏感，一般用来检测周围环境的光线的亮度，触发单片机或继电器模块等；
2.模块在环境光线亮度达不到设定阈值时，DO端输出高电平，当外界环境光线亮度超过设定阈值时，DO端输出低电平；
3.DO输出端可以与单片机直接相连，通过单片机来检测高低电平，由此来检测环境的光线亮度改变；
4.DO输出端可以直接驱动本店继电器模块，由此可以组成一个光控开关。

光敏传感器实物图：

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20161119/1479545872307793.png


声音传感器模块工作原理
---------------------------

1.声音模块对环境声音强度最敏感，一般用来检测周围环境的声音强度；
2.模块在环境声音强度达不到设定阈值时，OUT输出高电平，当外界环境声音强度超过设定阈值时，模块OUT输出低电平；
3.小板数字量输出OUT可以与单片机直接相连，通过单片机来检测高低电平，由此来检测环境的声音；
4.小板数字量输出OUT可以直接驱动本店继电器模块，由此可以组成一个声控开关；

声音传感器实物图：

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20161119/1479545901165245.png


硬件接线方法
--------------------

上面我们已经知道光敏传感器跟声音传感器的工作原理，以及3个针脚的作用，我们只需讲电源正极与电源负极跟我们TPYBoard v102的3.3V跟GND连接起来，
然后将光敏传感器与声音传感器的信号输出针脚连接到TPYBoard v102的GPIO上(本次实验声音传感器连接的是Y1针脚，光敏传感器连接的是Y2针脚)。
然后将发光数码管的正极插入面包板正极上,负极插入面包板的负极上,用杜邦线将负极连接到TPYBoard v102的GND上，正极连接到TOYBoard v102的X1针脚。


源代码
----------------


.. code-block:: python

    # main.py -- put your code here!
    import pyb
    from pyb import Pin

    voice = Pin('Y1',Pin.IN)
    light = Pin('Y2',Pin.IN)
    led = pyb.Pin("X1",pyb.Pin.OUT_PP)

    while 1:
        if light.value()==1:
            if voice.value()==1:
                led.value(0)
                pyb.LED(2).off()
                pyb.LED(3).off()
                pyb.LED(4).on()
            else:
                pyb.LED(3).off()
                pyb.LED(4).off()
                led.value(1)
                pyb.LED(2).on()
                pyb.delay(5000)
        else:
            pyb.LED(3).on()
            pyb.LED(2).off()
            pyb.LED(4).off()
            led.value(0)


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
