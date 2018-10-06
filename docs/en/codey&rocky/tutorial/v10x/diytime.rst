[Micropython]TPYBoard v10x DIY电子时钟
=======================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
----------------------

 - 学习在PC机系统中扩展简单I/O 接口的方法。
 - 什么是SPI接口。
 - 学习TPYBoard I2C接口的用法。
 - 学习LCD5110接线方法。
 - 设定时钟并将当前时间显示在LCD5110上。

所需元器件
---------------------

 - DS3231模块 1个
 - TPYBoard v102开发板 1块
 - LCD5110显示屏 1个
 - 数据线 1条
 - 杜邦线 若干

TPYBoard v102的SPI接口
-------------------------------

LCD5110需要SPI接口与TPYBoard v102进行连接传输数据，SPI接口是在CPU和外围低速器件之间进行同步串行数据传输，TPYBoard v102有两个SPI接口，我们用的为SPI1接口。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161126/1480150621179364.png

TPYBoard v102的I2C接口
----------------------------------
DS3231是I2C接口通信的，它通过I2C接口与TPYBoard v102进行数据通讯，DS3231通过这个接口与TPYBoard v102进行双向通讯，进行数据传输，TPYBoard v102有两个I2C接口，我们在这用的是I2C接口1。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161126/1480150651145892.png

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161126/1480150657750799.png

DS3231的接线方法
---------------------------------
DS会我们在这只用到DS3231的SCL,SDA,VCC,GND四个针脚即可设定读出当前时间，我们用的位I2C接口1，即DS3231的针脚SCL接TPYBoard v102的针脚X9，针脚SDA接TPYBoard v102的针脚X10。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161126/1480150682569300.png

控制5110显示屏显示6x8字符
----------------------------------------

TPYBoard的针脚与5110的针脚对应关系如下：

+----------+------------+------------------------------------------------+
| TPYBoard | LCD5110    | memo                                           |
+==========+============+================================================+
|Y10       | RST        | Reset pin (0=reset, 1=normal)                  |
+----------+------------+------------------------------------------------+
|Y11       | CE         | Chip Enable (0=listen for input,1=ignore input)|
+----------+------------+------------------------------------------------+
|Y9        | DC         | Data/Command (0=commands, 1=data)              |
+----------+------------+------------------------------------------------+
|X8        | DIN        | data flow (Master out, Slave in)               |
+----------+------------+------------------------------------------------+
|X6        | CLK        | SPI clock                                      |
+----------+------------+------------------------------------------------+
|3.3V      | VCC        | VCC                                            |
+----------+------------+------------------------------------------------+
|Y12       | LIGHT      | Light (0=on, 1=off)                            |
+----------+------------+------------------------------------------------+
|GND       | GND        | GND                                            |
+----------+------------+------------------------------------------------+


源代码
-------------------

接线OK后，并且导入font.py文件、upcd8544.py文件以及DS3231.py，编写main.py设定时间，运行main.py即可将当前时间显示在5110显示屏上。

.. code-block:: python

    # main.py -- put your code here!
    import pyb
    import upcd8544
    from machine import SPI,Pin
    from DS3231 import DS323
    ds=DS3231(1)
    ds.DATE([16,11,26])
    ds.TIME([16,14,6])
    while True:
        ds.TEMP()
        ds.DATE()
        SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
        #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
        #CLK =>SPI(1).SCK  'X6' SPI clock
        RST    = pyb.Pin('Y10')
        CE     = pyb.Pin('Y11')
        DC     = pyb.Pin('Y9')
        LIGHT  = pyb.Pin('Y12')
        lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
        lcd_5110.lcd_write_string('Date',0,0)
        lcd_5110.lcd_write_string(str(ds.DATE()),0,1)
        lcd_5110.lcd_write_string('Time',0,2)
        lcd_5110.lcd_write_string(str(ds.TIME()),0,3)
        lcd_5110.lcd_write_string('Tem',0,4 )
        lcd_5110.lcd_write_string(str(ds.TEMP()),0,5)
        pyb.delay(1000)


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
