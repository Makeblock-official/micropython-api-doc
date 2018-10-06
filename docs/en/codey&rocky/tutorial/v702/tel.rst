[Micropython]TPYBoard v702 来电显示功能
=============================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

什么是TPYBoard v702
---------------------------

TPYBoard v702是山东萝卜电子科技有限公司最新开发的，目前市面上唯一支持通信通信功能的MicroPython开发板：支持Python3.0及以上版本直接运行。支持GPS+北斗双模通信、GPRS通信、短信功能、电话功能；板载温湿度、光敏、三轴加速度传感器、蜂鸣器、LCD5110显示屏。免费提供通信测试服务平台。

**TPYBoard v702实物图**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170426/1493188183717935.png

TPYBoard v702实现来电显示
-------------------------------------------------------------------------------

**具体要求**

利用TPYBoard v702完成接收提示来电，并在显示屏上显示来电号码及来电人员称谓

**所需器件**

- TPYBoard v702开发板 1块
- LCD5110显示屏 1块
- SIM卡 1张(支持移动、联通)


板载通信功能及使用介绍
------------------------------

TPYBoard v702的开发板的整体整体亮点置一就是能板载通信功能，只要在开发板的卡槽上插上一张可以使用的手机卡（不支持电信），即可使用该功能。开发板板载的通信功能包括了电话，短信，GPRS等功能，在这个实验里面我们只使用电话这个功能。
开发板板载的通信功能已经设计的很完善，在接到来电的时候，会主动的把来电的信息通过串口4发送进来，这样一来作为用户的我们就是需要把数据进行相应的处理加显示就可以了。

制作主要过程
---------------------

**效果图**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170425/1493092006716181.png
   :width: 300px

`观看演示视频 <http://v.youku.com/v_show/id_XMjQ4MjgyMjI2OA==.html?spm=a2h3j.8428770.3416059.1>`_

**制作过程**

（1）首选我们需要做的是把5100显示屏插到702开发板的5110显示屏接口处；

（2）在上面工作完成后，我们这里需要用到主要的类库，5110的类库，我们需要把这个类库的.py文件拷贝到开发板的盘符中；

（3）完成以上工作后，我们开始main（）.py文件代码的编辑；

（4）对需要用到的类库进行声明和定义；

（5）把我们需要使用的变量进行一下定义；

（6）把我们需要用到的接口进行声明和定义，这里我们主要用到了spi1和串口4这两个接口，声明串口4的时候，需要把串口波特率设置为115200；

（7）下面开始主函数的编写，这个实验里面我们用到了显示，我们在程序的开始部分先进行显示部分的初始化；

（8）完成显示部分初始化之后，我们需要做一个最重要的事情，那就是定义“Y6”引脚为输出，然后把：“Y6”引脚拉低两秒以上，之后把此引脚拉高。因为“Y6”引脚是控制整个板载通信系统开启的开关，如果平时我们没有用到通信系统的话，为了节省功耗，板载通信系统是处于关闭状态的，需要使用时只需要拉低“Y6”引脚两秒以上；

（9）当看到开发板上的红色直插LED灯快速闪烁的时候，说明板载通信系统正在启动，当这个红色直插指示灯结束快闪（如果插在开发板卡槽上的手机可用，指示灯处于慢闪状态）说明板载通信系统已经启动；

（10）完成以上工作后，准备工作就已经完成了，剩下需要做的就是监控串口4是否有数据发送过来，当检测到串口4有数据发送过来，对数据进行相应的判断及处理，并显示到显示屏上即可。

**具体代码**

.. code-block:: python

    import pyb
    import upcd8544
    from machine import SPI,Pin
    from pyb import UART
     
    SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
    #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
    #CLK =>SPI(1).SCK  'X6' SPI clock
    RST    = pyb.Pin('X20')
    CE     = pyb.Pin('X19')
    DC     = pyb.Pin('X18')
    LIGHT  = pyb.Pin('X17')
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    N2 = Pin('Y3', Pin.OUT_PP)
    N1 = Pin('Y6', Pin.OUT_PP)
    N1.low()
    pyb.delay(2000)
    N1.high()
    pyb.delay(10000)
    u2 = UART(4, 115200,timeout=100)
     
    while True:
        N2.low()
        if u2.any()>0:
            _dataRead=u2.read()
            if _dataRead!=None:
                print('原始数据=',_dataRead)
                print('原始数据长度:',len(_dataRead))
                print('123',_dataRead[2:6])
                RING=_dataRead[2:6]
                print('111',_dataRead[18:29])
                HM=_dataRead[18:29]
                if(RING==b'RING'):
                    N2.high()
                    lcd_5110.lcd_write_string('Phone Number:',0,0)
                    lcd_5110.lcd_write_string(HM.decode("utf8"),2,1)
            pyb.delay(1000)


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v70x-master>`_
