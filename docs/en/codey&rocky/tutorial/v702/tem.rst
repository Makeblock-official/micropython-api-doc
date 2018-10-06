[Micropython]TPYBoard v702 LCD5110显示环境信息
===================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

什么是TPYBoard v702
-----------------------------

TPYBoard v702是山东萝卜电子科技有限公司最新开发的，目前市面上唯一支持通信通信功能的MicroPython开发板：支持Python3.0及以上版本直接运行。支持GPS+北斗双模通信、GPRS通信、短信功能、电话功能；板载温湿度、光敏、三轴加速度传感器、蜂鸣器、LCD5110显示屏。免费提供通信测试服务平台。

**TPYBoard v702实物图**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170426/1493188183717935.png


TPYBoard v702获取温度、湿度及光照度
------------------------------------------------------

**具体要求**

利用TPYBoard v702获取温度、湿度及光照度

**所需器件**

- TPYBoard v702开发板 1块
- 温湿度传感器和光敏系统均属于板载器件，无需外接

**板载温湿度传感器介绍**

TPYBoard v702板子温湿度传感器SHT20，新一代Sensirion湿度和温度传感器在尺寸与智能方面建立了新的标准：它嵌入了适于回流焊的双列扁平无引脚DFN封装，底面3x3mm，高度1.1mm。传感器输出经过标定的数字信号，标准I2C格式。
SHT21配有一个全新设计的CMOSens®芯片、一个经过改进的电容式湿度传感元件和一个标准的能隙温度传感元件，其性能已经大大提升甚至超出了前一代传感器（SHT1x和SHT7x）的可靠性水平。例如，新一代湿度传感器，已经经过改进使其在高湿环境下的性能更稳定。每一个传感器都经过校准和测试。在产品表面印有产品批号，同时在芯片内存储了电子识别码-可以通过输入命令读出这些识别码。
此外，SHT20的分辨率可以通过输入命令进行改变（8/12bit乃至12/14bit的RH/T），传感器可以检测到电池低电量状态，并且输出校验和，有助于提高通信的可靠性。

**技术参数**

- 输出:I2C数字接口
- 功耗:1.5uw(8位测量，1次/秒)
- 湿度范围0-100%RH
- 温度范围-40-+125℃（-40-+257℉）
- RH响应时间8s(tau63%)

**光敏系统介绍**

TPYBoard v702开发板上板载了一个光敏传感的系统，利用stm32的ADC检测进行数值采集，这里的ADC数值输入引脚我们使用了Y12。并利用代码逻辑进行相应的数据转换,最终解析出当前光照强度，其中33为光照强度最大值。


制作主要过程
-----------------------

**实物效果图**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170425/1493091201375274.png

**制作过程**

（1）首选我们需要做的是把5100显示屏插到702开发板的5110显示屏接口处；

（2）在上面工作完成后，我们这里需要用到两个主要的类库，5110的类库和SHT20的类库，我们需要把这两个类库的.py文件拷贝到开发板的盘符中；

（3）完成以上工作后，我们开始main（）.py文件代码的编辑；

（4）对需要用到的类库进行声明和定义；

（5）把需要把我们需要使用的变量进行一下定义；

（6）把我们需要用到的接口进行声明和定义，这里我们主要用到了spi和adc这两类接口；

（7）下面开始主函数的编写，首先我们把调用到的SHT20的类库中的函数的返回值读取出来，这样我们就获取到了温度和湿度的数值，其次我们定义ADC的的引脚和模式，上面我们介绍了我们这边的这个光敏系统我们使用的引脚是Y12引脚，我们这里需要把引脚数定义成Y12，其他的我们缺省处理；

（8）完成以上工作后，我们读取ADC引脚的返回值，这样我们获取到温度，湿度和亮度这三个数值；

（9）在完成温度湿度和亮度这三个数值的获取后，我们需要做的就是把这三个数值相应的在5110显示屏上显示出来，在5110显示屏的类库中控制5110显示的函数，可以直接调用；

（10）完成步骤9后，就完成了一个循环，这样往复的循环下去，我就可以实时的检测温湿度以及亮度了，在例程设计的时候，我们还设计了当亮度小于十的时候，蜂鸣器会发出响声。

**具体代码**

.. code-block:: python

    # main.py -- put your code here!
    #main.py
    import pyb
    import upcd8544
    from machine import SPI,Pin
    from pyb import UART
    from sht20 import SHT20
     
     
    ds = SHT20(1)
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
    while True:
        ads = pyb.ADC(Pin('Y12'))
        a=ads.read()
        a=a/100
        a=33-a
        print("a=",a)
        H=ds.TEMP()
        S=ds.TEMP1()
        H=125*H/256-6
        S=175.72*S/256-46.85
        if(a<17):
            N2.high()
        lcd_5110.lcd_write_string('WENDU:',0,0)
        lcd_5110.lcd_write_string(str(S),0,1)
        lcd_5110.lcd_write_string('SHIDU:',0,2)
        lcd_5110.lcd_write_string(str(H),0,3)
        lcd_5110.lcd_write_string('LIANGDU:',0,4)
        lcd_5110.lcd_write_string(str(a),0,5)
        N2.low()


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v70x-master>`_
