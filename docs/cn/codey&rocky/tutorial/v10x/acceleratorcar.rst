[Micropython]TPYBoard v10x 加速度无线小车
===============================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

引言
-------------

现在无线控制已经成为了电子科学领域的主流，这次就来教大家做一个主流中的主流--无线控制的小车，先给大家看一下最终的成品演示视频：

.. raw:: html
	<video preload='none' src='http://www.micropython.net.cn/ueditor/php/upload/video/20160824/1472020805689816.ogg' id='video_show' />


所有器材
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- TPYBoard v102开发板 2块
- 小车底盘 1个
- LORA无线模块 1块
- 充电宝 1个
- 9014三极管两个（为什么用到它呢，后面再说）

在这个开发板上有一个及速度传感器，我是看到开发板上有个加速度传感器才想起来这样做的，这里的呢我们先介绍一下加速度传感器。

加速度传感器，包括由硅膜片、上盖、下盖，膜片处于上盖、下盖之间，键合在一起；一维或二维纳米材料 、金电极和引线分布在膜片上，并采用压焊工艺引出导线；工业现场测振传感器，主要是压电式加速度传感器。其工作原理主要利于压电敏感元件的压电效应得到与振动或者压力成正比的电荷量或者电压量。目前工业现场典型采用IEPE型加速度传感器，及内置IC电路压电加速度传感器，传感器输出与振动量正正比的电压信号，例如：100mV/g (每个加速度单位输出100mV电压值。1g=9.81m/s-2)。

关于上面的介绍你是不是没看懂？没看懂也没关系，那是我参照官方的介绍写的，其实我也看不懂。其实通俗的说吧，加速度传感器就是通过测量由于重力引起的加速度，你可以计算出设备相对于水平面的倾斜角度。通过分析动态加速度，你可以分析出设备移动的方式。是不是还是不太懂怎么获取这个倾斜的值？那也没关系，我们的Python语言里有获得这个倾斜值的函数，直接使用就可以啦。但是这里值得注意的是，这个函数返回的倾斜度是一个值，每一个传感器因为做工时的差异，返回值不同，这个需要大家自己做实验看一下。

得到倾斜值后，下面的工作的就简单了，那就是判断板子在怎么倾斜，然后把倾斜的信号传出去，这样就OK啦，妥妥哒。

介绍完了这控制端的，那咱们得说说怎么把控制的信号传出吧。这里呢主要是使用了lora模块，这个模块现在还是挺流行的。我亲自去做过一个传输距离的实验，具体的距离我没测，但是我感觉最起码也得有个二三里地吧，这距离对于做个小车妥妥哒够用啦。

说一下lora模块的使用吧，lora模块的使用呢，也很简单，串口通信，无线透传。就是说你使用单片机通过串口给模块什么，模块就给你传输什么（定点的话需要带上地址信道），这个lora模块说明说的很详细。但是是不是觉得还要用串口，感觉好麻烦？我也觉得麻烦，但是Python语言和这个开发板的功能都很强大，有一个写好的使用串口的方法，直接调用就可以（瞬间感觉开发好简单啦）。

上面介绍了控制端的工作和原理，下面说一下被控制端（就是按在小车上的）。

被控制端就是要使用开发板控制小车地盘的电机转动，这里被我被坑了一次，我在某宝上买这架车的时候，问了客服需不需要其他的东西，客服说不用。我感觉现在连电机的驱动都不用啦，感觉好高端，但是买回来发现还是需要一个L298N驱动。瞬间感觉被骗了，但是，悲愤的同时，我的两个9014上场了，简单的做了一个三极管开关电路，妥妥哒（虽然速度略慢）。

信号接收部分，这个和控制端差不多的，都是使用了lora模块，然后把收到的数据做判断。判断后再按照自己的逻辑驱动电机，小车就开起来了（小车怎么拐弯的我就不介绍了，网上教程大把多）。

上面说了这么多，其实也很抽象啦，下面来个聚象的，上图。

先上一个自己画的简单的原理图:

控制器

.. image:: http://tpyboard.com/ueditor/php/upload/image/20160815/1471255048558130.png

被控制端

.. image:: http://tpyboard.com/ueditor/php/upload/image/20160815/1471255085467193.png


这两张图是我画来帮助大家理解的(我这样做的被控制端的电路，速度略慢。大家可以在驱动那里做个放大电路，速度可以上去的，但是不能后退，大家可以直接使用L298N驱动。)，我做的时候是使用杜邦线的，并没有电路图，再上一张成品图给大家看。

成品图：

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20160815/1471255116488443.jpg


这些都是给大家参考的，大家做的时候多学习多看看，亲身体验了才能真的学到东西。

下面的程序给大家，大家可以参考一下。

**控制端源代码**

.. code-block:: python

    import pyb
    xlights = (pyb.LED(2), pyb.LED(3))
    ylights = (pyb.LED(1), pyb.LED(4))
    from pyb import UART
    from pyb import Pin
    #from ubinascii import hexlify
    from ubinascii import *
    accel = pyb.Accel()
    u2 = UART(2,9600,timeout=100)
    i=0
    K=1

    #*******************************主程序**********************************
    print('while')
    while (K>0):
        _dataRead=u2.readall()
        if(1>0):
            x = accel.x()
            print("x=")
            print(x)
            if x > 10:
                xlights[0].on()
                xlights[1].off()
                u2.write('\x00\x05\x18YOU')
                print('\x00\x01\x18YOU')
            elif x < -10:
                xlights[1].on()
                xlights[0].off()
                u2.write('\x00\x05\x18ZUO')
                print('\x00\x01\x18ZUO')

            else:
                xlights[0].off()
                xlights[1].off()

            y = accel.y()
            print("y=")
            print(y)
            if y > 15:
                ylights[0].on()
                ylights[1].off()
            elif y < -15:
                ylights[1].on()
                ylights[0].off()
                u2.write('\x00\x05\x18QIAN')
                print('\x00\x01\x18QIAN')
            else:
                ylights[0].off()
                ylights[1].off()

            pyb.delay(10)


**被控制端源代码**

.. code-block:: python
    
    import pyb
    from pyb import UART
    from pyb import Pin
    from ubinascii import hexlify
    from ubinascii import *
    M1 = Pin('X1', Pin.OUT_PP)
    M3 = Pin('Y1', Pin.OUT_PP)
    u2 = UART(2, 9600,timeout = 100)
    i=0
    K=1
    #*******************************主程序**********************************
    print('while')
    while (K>0):
        M1.high()
        pyb.delay(3)
        M3.high()
        if(u2.any()>0):
            print('1234')
            M1.low()
            M3.low()
            pyb.delay(3)
            _dataRead=u2.readall()
            print('123',_dataRead)
            if(_dataRead.find(b'QIAN')>-1):
                M1.low()
                M3.low()
                print('QIAN')
                pyb.delay(250)
            elif(_dataRead.find(b'ZUO')>-1):
                M1.low()
                M3.high()
                print('ZUO')
                pyb.delay(250)
            elif(_dataRead.find(b'YOU')>-1):
                M1.high()
                M3.low()
                print('ZUO')
                pyb.delay(250)


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
