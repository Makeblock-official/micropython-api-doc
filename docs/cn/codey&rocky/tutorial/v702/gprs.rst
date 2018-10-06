[Micropython]TPYBoard v702 GPRS功能测试
===========================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

什么是TPYBoard v702
---------------------------

TPYBoard v702是山东萝卜电子科技有限公司最新开发的，目前市面上唯一支持通信通信功能的MicroPython开发板：支持Python3.0及以上版本直接运行。支持GPS+北斗双模通信、GPRS通信、短信功能、电话功能；板载温湿度、光敏、三轴加速度传感器、蜂鸣器、LCD5110显示屏。免费提供通信测试服务平台。

**TPYBoard v702实物图**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170426/1493188183717935.png

TPYBoardV702使用GPRS功能把数据上传至服务器
---------------------------------------------------------

**具体要求**

利用TPYBoard v702使用GPRS功能把数据上传至服务器

**所需器件**

- TPYBoard v702开发板 1块
- SIM卡 1张(支持移动、联通)

**板载通信功能及使用介绍**

TPYBoard v702的开发板的整体整体亮点置一就是能板载通信功能，只要在开发板的卡槽上插上一张可以使用的手机卡（不支持电信），即可使用该功能。开发板板载的通信功能包括了电话，短信，GPRS等功能，在这个实验里面我们只使用GPRS这个功能。我们使用GPRS功能，主要是为了借助这个功能向服务器透传数据，所以我们第一步是要打开透传功能。然后我们要和服务器建立连接，这时我们需要知道服务器的地址和端口。这个实验我们借用官方提供的测试平台，发送一个自己编辑的数据包，来学习一下GPRS功能的使用方法。

制作主要过程
---------------------

先上个图，下面再开始说代码的问题。

Putty数据监控图

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170426/1493188237747626.png

示例定位图

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170426/1493188346729478.png


**制作步骤**

（1）第一步是先把手机卡插到开发板开槽上，需要保证手机卡可以使用；

（2）在上面工作完成后，我们开始main（）.py文件代码的编辑；

（3）对需要用到的类库进行声明和定义；

（4）把我们需要使用的变量进行一下定义；

（5）把我们需要用到的接口进行声明和定义，这里我们主要用到了串口4这个接口，声明串口4的时候，需要把串口波特率设置为115200

（6）下面开始主函数的编写，这个实验里面我们用到了数据包，我们先新建一个符合格式的数据包；

（7）完成以上之后，我们需要做一个最重要的事情，那就是定义“Y6”引脚为输出，然后把：“Y6”引脚拉低两秒以上，之后把此引脚拉高。因为“Y6”引脚是控制整个板载通信系统开启的开关，如果平时我们没有用到通信系统的话，为了节省功耗，板载通信系统是处于关闭状态的，需要使用时只需要拉低“Y6”引脚两秒以上；

（8）当看到开发板上的红色直插LED灯快速闪烁的时候，说明板载通信系统正在启动，当这个红色直插指示灯结束快闪（如果插在开发板卡槽上的手机可用，指示灯处于慢闪状态）说明板载通信系统已经启动；

（9）完成以上工作后，准备工作就已经完成了，下面我们需要先把通信系统的通信方式设置为透传，之后再和相应的服务器地址和端口进行连接；

（10）和服务器建立连接后，就可以开始想服务器发送数据了，直接把数据从串口4送出去就可以了，通信系统会原封不动的把你发的数据发送到服务器。

**具体代码**

.. code-block:: python

    import pyb
    import upcd8544
    from machine import SPI,Pin
    from pyb import UART
     
    #lcd5110初始化
    SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
    #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
    #CLK =>SPI(1).SCK  'X6' SPI clock
    RST    = pyb.Pin('X20')
    CE     = pyb.Pin('X19')
    DC     = pyb.Pin('X18')
    LIGHT  = pyb.Pin('X17')
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    lcd_5110.clear()
    lcd_5110.lcd_write_string('Getting Ready',0,1)
    #GU620模块初始化
    N1 = Pin('Y6', Pin.OUT_PP)#定义通信系统启动引脚
    N1.low()
    pyb.delay(2000)
    N1.high()
    pyb.delay(10000)#拉高拉低引脚，启动通信系统
    u2 = UART(4,115200,timeout = 100)#定义串口4，设置 波特率为115200
    #报文详细格式说明参照萝卜电子服务平台示例报文格式。
    #www.turnipsmart.com:8080
    message = 'TPGPS,1234567890abcde,36.67191670,119.17200000,201701120825,25,50,END'
    if __name__ == '__main__':
        #连接TCP服务器
        u2.write('AT+CIPSTART="TCP","139.196.110.155",30000\r\n')
        while True:
            if u2.any() > 0:
                _dataRead = u2.read()
                print('_dataRead:',_dataRead)
                if _dataRead.find(b'CONNECT OK') > -1:
                    #说明已经和服务器成功建立连接
                    lcd_5110.lcd_write_string('CONNECT OK',0,2)
                    print('CONNECT OK')
                    pyb.LED(2).on()
                    #发送指令进入透传模式
                    u2.write('ATO0\r\n')
                if _dataRead.find(b'ATO0\r\n\r\nOK\r\n') > -1:
                    #成功进入透传模式,退出透传模式发送+++,注意前后1秒内不能输入任何字符
                    #发送数据给服务器
                    u2.write(message)
                if _dataRead.find(b'TPGPSOK') > -1:
                    #该数据为服务器返回
                    #在向服务器发送了数据后，服务器会对数据进行判断，并返相应的报文
                    pyb.LED(3).on()
                    lcd_5110.lcd_write_string('SEND OK',0,3)
                    break


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v70x-master>`_
