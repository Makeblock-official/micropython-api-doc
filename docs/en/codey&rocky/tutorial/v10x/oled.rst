.. _quickref:

[Micropython]TPYBoard v10X 学习使用OLED显示屏
========================================================


版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
---------------------

    - 学习在PC机系统中扩展简单I/O 接口的方法。
    - 进一步学习编制数据输出程序的设计方法。
    - 学习TPYBoard控制OLED显示字符。

所需元器件
---------------------

    - TPYBoard v102板子 1块
    - micro USB数据线 1条
    - 杜邦线 若干
    - OLED液晶屏 1块

什么是OLED显示屏
---------------------

OLED显示屏简介
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

有机发光二极管（organic light-emitting diode，OLED）是一种由柯达公司开发并拥有专利的显示技术，这项技术使用有机聚合材料作为发光二极管中的半导体（semiconductor）材料。聚合材料可以是天然的，也可能是人工合成的，可能尺寸很大，也可能尺寸很小。其广泛运用于手机、数码摄像机、DVD机、个人数字助理（PDA）、笔记本电脑、汽车音响和电视。OLED显示器很薄很轻，因为它不使用背光。
本例中使用0.96 寸OLED显示屏，该屏具有高亮度，低功耗屏，显示颜色纯正，在阳光下有很好的可视效果。模块供电可以是3.3V 也可以是5V，不需要修改模块电路，同时兼容3种通信方式：4 线SPI、3线SPI、 IIC，通信模式的选择可以根据提供的BOM表进行跳选。该模块一共有三种颜色：蓝色、白色、黄蓝双色。OLED 屏具有多个控制指令，可以控制OLED 的亮度、对比度、开关升压电路等指令。操作方便，功能丰富。同时为了方便应用在产品上，预留4个M2 固定孔，方便用户固定在机壳上。0.96寸OLED显示屏的驱动芯片为：SSD1306(已集成在屏中)。

实际显示效果
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20170211/1486776004559236.png

OLED接口定义
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1> GND= 电源地

    2> VCC= 电源地（2.8V~5.5V）

    3> D0 =  时钟线

    4> D1 =  数据线

    5> RES= 复位线

    6> DC =  数据/命令

    7> CS =  片选

硬件的接线方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    在这OLED需要SPI接口与TPYBoard v102进行连接传输数据，SPI接口是在CPU和外围低速器件之间进行同步串行数据传输，TPYBoard v102自带两个SPI接口，本实验中我们用的TPYBoard v102的SPI1接口。

接线图
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/oled.png

实物接线图
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20170211/1486776112995233.png


接线OK后，并且导入font.py文件和ssd1306.py文件，再可运行main.py了。

源代码
---------------------

.. code-block:: python

    #main.py
    import pyb
    import upcd8544
    from ssd1306 import SSD1306

    display = SSD1306(pinout={'dc': 'Y9',
                          'res': 'Y10'},
                  height=64,
                  external_vcc=False)

    led_red = pyb.LED(1)
    led_red.off()
    display.poweron()
    display.init_display()
    display.draw_text(1,1,'Hello World!',size=1,space=1)
    display.draw_text(1,10,'this is TPYBoard V102！',size=1,space=1)
    # 显示出你想要显示的内容
    display.display()


实现效果
---------------------

.. image:: http://www.micropython.net.cn/ueditor/php/upload/image/20170211/1486776202255121.png


- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
