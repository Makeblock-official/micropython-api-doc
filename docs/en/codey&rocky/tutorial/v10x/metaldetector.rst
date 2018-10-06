[Micropython]TPYBoard v10x DIY金属检测仪
======================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明。

实验目的
----------------

    - 学习在PC机系统中扩展简单I/O 接口的方法。
    - 进一步学习编制数据输入输出程序的设计方法。
    - 学习LJ12A3-4-Z/BX金属接近开关的工作原理。
    - 硬件接线方法。
    - 学会用TPYBoard接收金属接近开关的输出信号，并对信号进行判断处理，点亮LED发光二极管。

所需元器件
-----------------

    - TPYBoard v102 板子 1块
    - LJ12A3-4-Z/BX 金属接近开关 1个
    - 面包板 1块
    - 发光二极管 1个
    - micro USB数据线 1条
    - 杜邦线 若干

LJ12A3-4-Z/BX 接近开关工作原理
-------------------------------------

.. image:: http://tpyboard.com/ueditor/php/upload/image/20161220/1482216851281836.png

    接近开关既有行程开关、微动开关的特性，同时具有传感性能，且动作可靠，性能稳定，频率响应快，应用寿命长，抗干扰能力强等，并且有防水防震，耐腐蚀等特点。
    接近开关的输出信号是输出数字信号，即当没有金属靠近时，输出1；当有金属时，输出0。将信号输出端接入TPYBoard v102，然后TPYBoard v102进行相应的判断，金属检测仪广泛应用于机床、冶金、化工、航天航空、轻纺与印刷等行业。
    在日常生活中，可用于宾馆、饭店、车库的自动门，自动热风机上都有应用；在安全防盗方面，如资料档案、财会、金融、博物馆、金库等重地，通常都装有各种接近开关组成的防盗装置。


硬件接线方法
--------------------

    LJ12A3-4-Z/BX接近开关

.. image::http://tpyboard.com/ueditor/php/upload/image/20161220/1482216879826644.png

    我们只需要正极（灰线）连接TPYBoard v102的VIN引脚，负极（蓝线）接TPYBoard v102的GND引脚，黑线（输出信号）连接TPYBoard v102的IO针脚(本次使用Y1针脚)。
    连接完毕后，当有金属靠近时，接近开关本身自带的红色灯就会亮起来，当远离金属时候，灯熄灭。
    TPYboard v102开发板通过Y1针脚收集金属开关传递过来的数字信号，用来控制自动门开，报警等，本教程只是做了一个简单易懂的应用，点亮我们的红色LED发光二极管。

    无金属接近时：

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161220/1482216919240450.png

    用金属接近时：

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20161220/1482216954934573.png

源代码
-------------

.. code-block:: python

    # main.py -- put your code here!
    import pyb
    from machine import Pin

    y1 = Pin('Y1', Pin.IN)
    x1 = Pin('X1', Pin.OUT_PP)

    while 1:
        #无金属时
        if y1.value() == 1 :
            print(y1.value())
            x1.value(0)
        #有金属时
        else:
            print(y1.value())
            x1.value(1)

- `下载源码 <https://github.com/TPYBoard/developmentBoard/tree/master/TPYBoard-v10x-master>`_
