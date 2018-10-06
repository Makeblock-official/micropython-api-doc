.. _quickref:

[MicroPython]TPYBoard 添加自定义类库
======================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

开始之前，首先要感谢一下TPYBoard技术交流群(157816561)-云之初晓网友的分享。


将自己编写的一些Python脚本的类库添加到固件中，在使用时只需import调用，就像使用内置的pyb一样简单便捷;
同时还有另外一个重要的功能，就是可以很好的保护源代码。比起生成mpy加密文件这种方式来说，显然添加到固件中会更加安全可靠。


搭建micropython编译环境
-------------------------
1.安装arm-none-eabi-gcc交叉编译工具和gcc编译器。

.. code-block::

  sudo apt-get install gcc-arm-none-eabi
  
  sudo apt-get install gcc

2.下载micropython源码包到本地，我下载到了home目录下。

.. code-block::

  sudo git clone --recursive https://github.com/micropython/micropython.git

MicroPython的源码结构
---------------------------

.. image:: img/add1.png

+--------------+---------------------------------------------+
| docs/        | micropython的说明文档(restructuredText)     |
+--------------+---------------------------------------------+
| drivers/     | 一些外接设备的实现例程(eg:ds18b20,nrf24l01) |
+--------------+---------------------------------------------+
| examples/    | micropython的使用例程                       |
+--------------+---------------------------------------------+
| extmod/      | C语言实现的模块                             |
+--------------+---------------------------------------------+
| lib/         | 各类芯片的lib文件                           |
+--------------+---------------------------------------------+
| mpy-cross/   | 自带的交叉编译器，可以将.py生成.mpy加密文件 |
+--------------+---------------------------------------------+
| ports/       | 移植到各类MCU上的源码(eg:stm32,esp8266)     |
+--------------+---------------------------------------------+
| tests/       | 测试框架和Python脚本                        |
+--------------+---------------------------------------------+
| tools/       | 工具                                        |
+--------------+---------------------------------------------+

进入ports目录下你会发现，micropython根据不同的MCU运行平台进行了分类，比如esp8266就是运行在esp8266-WIFI模块上的micropython，stm32是运行在stm32上的，还有cc3200等。

.. image:: img/add2.png

然后进入stm32/boards目录下,里面又根据stm32不同的系列进行了划分。

开始编译
-------------------------
3.回到stm32/目录下，将需要添加到固件中的Python脚本类库放到modules/目录下。编译之前，请确保程序运行无误。为了测试新建了一个test.py文件，简单写了两个函数。如下:

.. code-block:: python

    import pyb
    
    def on():
        pyb.LED(4).on()
    def off():
        pyb.LED(4).off()


4.执行编译命令，等待编译完成。

.. code-block::

  sudo make BOARD=PYBV10

BOARD参数为stm32/boards/目录下相应的开发板名称。
本次教程用的是TPYBoardv102（蓝色）开发板，兼容PYBV10，所以选择PYBV10开发板编译。
若是TPYBoardv102（绿色）基础板，同样选择PYBV10。
若是TPYBoardv102（黑色）开发板，需选择PYBV11。

.. image:: img/add3.png

生成的固件在stm32/build-PYBV10/目录下的firmware.dfu和firmware.hex文件。

.. image:: img/add4.png

5.将dfu和hex文件拷贝到本地，进行烧写。

dfu文件的烧写教程，请参考：http://tpyboard.com/support/reference11/302.html

hex文件的烧写需要借助ST-LINK工具，请参考：http://tpyboard.com/support/reference11/239.html

6.烧写完毕后进行测试，在main.py文件输入以下内容:

.. code-block:: python

    import pyb
    import test
    test.on()
    pyb.delay(1500)
    test.off()
