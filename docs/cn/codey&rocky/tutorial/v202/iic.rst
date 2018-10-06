[Micropython]TPYBoard v202 I2C操作DS3231时钟模块
================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
-------------

    - 学习TPYBoard v202中I2C接口的使用方法
    - 学习使用DS3231制作简易的电子时钟

准备工作
-------------

    - TPYBoard v202 1块
    - DS3231时钟模块 1个
    - 所需软件 MicroPython File Uploader `点击下载 <http://www.tpyboard.com/download/tool/170.html>`_


I2C的基本介绍
-------------------

  - I2C(Inter-Integrated Circuit(集成电路总线))

    I2C总线类型是由飞利浦半导体公司在八十年代初设计出来的一种简单、双向、二线制、同步串行总线，主要是用来连接整体电路(ICS)。
    
    I2C是一种多向控制总线，也就是说多个芯片可以连接到同一总线结构下，同时每个芯片都可以作为实时数据传输的控制源。

    
MicroPython中I2C类库介绍
--------------------------------

    .. code-block:: python
    
        from machine import Pin, I2C

        # construct an I2C bus
        i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

        i2c.readfrom(0x3a, 4)   # read 4 bytes from slave device with address 0x3a
        i2c.writeto(0x3a, '12') # write '12' to slave device with address 0x3a

        buf = bytearray(10)     # create a buffer with 10 bytes
        i2c.writeto(0x3a, buf)  # write the given buffer to the slave
    
    
    请参考：http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html?highlight=i2c

    
    TPYBoard v202的I2C接口中SCL=Pin(14),SDA=Pin(2)，I2C初始化修改为如下：
    
    .. code-block:: python
    
        i2c = I2C(scl=Pin(14), sda=Pin(2), freq=100000)    
        
    
DS3231时钟芯片的基本介绍
---------------------------

    DS3231是低成本、高精度I2C实时时钟(RTC)，具有集成的温补晶振(TCXO)和晶体。该器件包含电池输入端，断开主电源时仍可保持精确的计时。
    
    集成晶振提高了器件的长期精确度，并减少了生产线的元件数量。DS3231提供商用级和工业级温度范围，采用16引脚300mil的SO封装。
    
    DS3231内部集成了一个非常精确的数字温度传感器，可通过I2C接口对其进行访问(同读取时间一样)，精度为±3°C。


硬件的连接
-------------------
    
    - 示意图
        
        +---------------+-----------------+
        | TPYBoard v202 | DS3231时钟模块  |
        +===============+=================+
        | 3.3V          | VCC             |
        +---------------+-----------------+
        | GND           | GND             |
        +---------------+-----------------+
        | SDA           | SDA             |
        +---------------+-----------------+
        | SCL           | SCL             |
        +---------------+-----------------+
        
源代码
-------------------

main.py程序代码

.. code-block:: python

    import machine
    import time
    from ds3231 import DS3231

    ds=DS3231()
    ds.DATE([17,9,1])
    ds.TIME([10,10,10])

    while True:
        print('Date:',ds.DATE())
        print('Time:',ds.TIME())
        print('TEMP:',ds.TEMP())
        time.sleep(5)


ds3231.py `点击预览 <https://github.com/TPYBoard/developmentBoard/blob/master/TPYBoard-v20x-master/TPYBoard%20v202%20%E5%85%B8%E5%9E%8B%E5%AE%9E%E4%BE%8B/05.I2C%E6%93%8D%E4%BD%9CDS3231%E6%A8%A1%E5%9D%97/ds3231.py>`_


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v20x-master>`_
