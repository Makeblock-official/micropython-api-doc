[Micropython]TPYBoard v702 LCD5110显示当前经纬度
=================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

什么是TPYBoard v702
---------------------------

TPYBoard v702是山东萝卜电子科技有限公司最新开发的，目前市面上唯一支持通信通信功能的MicroPython开发板：支持Python3.0及以上版本直接运行。支持GPS+北斗双模通信、GPRS通信、短信功能、电话功能；板载温湿度、光敏、三轴加速度传感器、蜂鸣器、LCD5110显示屏。免费提供通信测试服务平台。

**TPYBoard v702实物图**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170426/1493188183717935.png

TPYBoard v702获取经纬度信息
--------------------------------------------------------

**具体要求**

利用TPYBoard v702完成所在地经纬度采集，并在LCD5110显示屏上显示

**所需器件**

- TPYBoard v702开发板 1块
- LCD5110显示屏一块

**板载定位功能及使用介绍**

TPYBoard v702的开发板的整体整体亮点就是能进行定位，可以获取到当前所在地的经纬度，高度，时间等等的一些信息。在这个实验里面我们就要用到获取经纬度这一功能。这个开发板上主要的硬件功能已嵌入到了开发板上，使用起来非常方便，我们只需要进行简单的设置操作就能获取到经纬度，然后再进行数据解析，分割以及数据转换等处理，就可以得到我们想要的经度和纬度了，之后我们在使用显示屏把经纬度显示出来就完成了在开发板上显示经纬度了。

制作主要过程
----------------------------

**效果图**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170425/1493097993618155.png

**制作过程**

（1）首选我们需要做的是把5100显示屏插到702开发板的5110显示屏接口处；

（2）在上面工作完成后，我们这里需要用到主要的类库，5110的类库，我们需要把这个类库的.py文件拷贝到开发板的盘符中；

（3）完成以上工作后，我们开始main（）.py文件代码的编辑；

（4）对需要用到的类库进行声明和定义；

（5）把需要把我们需要使用的变量进行一下定义；

（6）把我们需要用到的接口进行声明和定义，这里我们主要用到了spi1和串口4这两个接口，声明串口4的时候，需要把串口波特率设置为115200；

（7）下面开始主函数的编写，这个实验里面我们用到了显示，我们在程序的开始部分先进行显示部分的初始化；

（8）完成显示部分初始化之后，我们需要做一个最重要的事情，那就是定义“Y6”引脚为输出，然后把：“Y6”引脚拉低两秒以上，之后把此引脚拉高。因为“Y6”引脚是控制整个板载定位系统开启的开关，如果平时我们没有用到定位系统的话，为了节省功耗，板载定位系统是处于关闭状态的，需要使用时只需要拉低“Y6”引脚两秒以上；

（9）当看到开发板上的红色直插LED灯快速闪烁的时候，说明板载定位系统正在启动，当这个红色直插指示灯结束快闪（指示灯处于慢闪或者熄灭状态）说明板载定位系统已经启动；

（10）完成以上工作后，我们的准工作就已经完成了，剩下需要做的就是通过串口4发送相应的指令，获取相应的数据，再把相应的数据进行数据转换，并显示到显示屏上即可。

**具体代码**

.. code-block:: python

    import pyb
    import upcd8544
    from machine import SPI,Pin
    from pyb import UART
     
    leds = [pyb.LED(i) for i in range(1,5)]
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
     
    def DataConver(str_,flag):
        wei_=float(str_)/100
        wei_arr=str(wei_).split('.')
        val_=100000
        if flag==0:#纬度
            val_=10000
        wei_arr[1]=str(float(wei_arr[1])/60*val_).replace('.','')
        weidu=wei_arr[0]+'.'+wei_arr[1]
        return weidu
    while True:
        pyb.LED(2).on()
        u2.write('AT+GPSLOC=1\r\n')
        pyb.delay(3000)
        _dataRead=u2.read()
        print('搜星=',_dataRead)
        pyb.delay(1000)
        u2.write('AT+GPSLOC=0\r\n')
        pyb.delay(200)
        print('BEIDOU')
        _dataRead=u2.read()
        if _dataRead!=None:
            print('原始数据=',_dataRead)
            print('原始数据长度:',len(_dataRead))
            if 60<len(_dataRead)<70:
                _dataRead = _dataRead.decode('utf-8')
                _dataRead1=_dataRead.split(',')
                print('数据=',_dataRead1)
                print(len(_dataRead1),'***')
                if len(_dataRead1)>4:
    #*******************纬度计算********************
                    weidu=_dataRead1[1]
                    WD=DataConver(weidu,0)
    #*******************经度计算********************
                    jingdu=_dataRead1[2]
                    JD=DataConver(jingdu,1)
                    if jingdu.find('0.0000')<0:
                        N2.high()
    #***********************时间************************
        lcd_5110.lcd_write_string('JINGDU:',0,0)
        lcd_5110.lcd_write_string(str(JD),0,1)
        lcd_5110.lcd_write_string('WEIDU:',0,2)
        lcd_5110.lcd_write_string(str(WD),0,3)


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v70x-master>`_
