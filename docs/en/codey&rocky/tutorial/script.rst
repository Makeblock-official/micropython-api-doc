运行第一个脚本
=========================

从这篇教程开始将动手在 TPYboard 板上运行 Python 脚本,毕竟这是我们的目标！

连接开发板
-----------------------

通过 USB 线连接你的 PC 机（windows,mac,linux皆可）。
你不可能搞错因为仅有这么一种连接方式。

.. 图像:: ../img/tpyboard_usb.jpg

当连接成功后开发板将上电和进入开机程序，绿色的 LED 灯应该在半秒或更少的时间内亮起，当其熄灭时意味着开机程序已完成。

安装USB驱动
-----------------------------

你的电脑现在应该认识到TPYboard开发板。这也取决于你的电脑类型。
关于接下来会发生什么：

  - **Windows**: 开发板将作为可移动磁盘出现。Window 将自动弹出窗口界面，或者你需要使用资源管理器自己寻找进入。

   Windows系统同时会将开发板视为串口驱动，且设备将会自动连接。
   如果是这样，取消这样的连接，我们将在下一篇教程中展示串口驱动如何工作。

  - **Mac**: 你的TPYBoard开发板将作为一个可移动磁盘出现在桌面。
    其可能为“NONAME”，请点击打开里边的文件夹。

  - **Linux**: 开发版将作为可移动的多媒体设备出现。
  在 Ubuntu 下其将自动挂载并弹出开发板的文件夹。在其他的 Linux 系统下，开发板自动挂载或者需要手动实现。
  在命令行下敲入 lsblk 参看连接设备，然后敲入 mount /dev/sdb1（用对应的设备名替换sbd1）。
  或许你需要 boot 权限实现这一过程。
  至此开发板以移动磁盘的形式存在了，且有一个开发板驱动的窗口（或者命令行）显示出来。


你所见到的设备是由开发板里边的 /flash实现的，其由以下四个文件关联组成：

* `boot.py <http://micropython.org/resources/fresh-pyboard/boot.py>`_ -- 这个脚本执行时TPYBoard开发板启动。
   它设置了开发板的多个选项参数。

* `main.py <http://micropython.org/resources/fresh-pyboard/main.py>`_ -- 这是包含Python程序的主要脚本。
    在 boot.py 运行后被执行

* `README.txt <http://micropython.org/resources/fresh-pyboard/README.txt>`_ -- 包含开启Python的必要基础信息。

* `pybcdc.inf <http://micropython.org/resources/fresh-pyboard/pybcdc.inf>`_ --   这是一个Windows驱动文件，配置串行USB装置，
之后的教程中有更多的介绍。

编辑mian.py
-------------------

现在我们可以开始编写自己的 python 程序了。
用文本编辑器打开 main.py 文件。Windows 环境下可以使用记事本或者其他编辑器。
Mac 和 linux 下使用你喜欢的文本编辑器即可。
打开文件后你将看到如下的一行：

    # main.py -- put your code here!

该行以 # 字符开始，意味着只是一个注释。
这样的命令行不会被执行，仅为代码提供信息用在这个 main.py 加多两行，如下所示::

    # main.py -- put your code here!
    import pyb
    pyb.LED(4).on()

第一行表明使用 pyb 模块，这个模块包含了控制开发板的所有函数和类。

第二行打开了蓝色的 LED：先是在 pyb 模块中使用了 LED 类，创建了 LED 4 的实例，然后将其点亮。

重置开发板
---------------------

为运行这个小小的脚本，我们需要保存并关闭 main.py文件，
然后在 USB 设备中退出（或者卸载），就像退出移动磁盘一样。

当设备安全退出或解除挂载后就来到了实现功能的地方：
按下板上的复位键将重置开发板并运行写好的程序。
RST复位按键位于右边，USB 接口下。

当按下复位键后绿色的 LED 将快速闪烁，然后蓝色的 LED 保持长亮。

至此编写和运行第一个 MicroPython 程序就完成了，加油！You  Can  Do  It !
