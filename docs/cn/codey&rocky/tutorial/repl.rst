获取MicroPython REPL提示
=================================

REPL（交互式解释器）全称是 Read Evaluate Print Loop，TPYBoard 允许用户和 MicorPython 的交互式连接。
使用repl是迄今为止来测试你的代码和运行命令的最简单的方法。
使用 REPL 可以往 "main.py" 中增添脚本内容。

使用 REPL 需要用 USB 串口连接 TPYBoard。如何做到这一点取决于开发环境。

Windows
---------

你需要安装TPYBoard驱动使用串行USB设备。
该驱动在TPYBoard的USB闪存驱动中，名为 "tpybcdc.inf"。

安装该驱动用户需要在电脑的设备管理器列表中中找到 TPYBoard 设备（尚未工作的设备，旁边应该有黄色的警告图标）
在该设备上鼠标右键，选择工具（properties）然后安装驱动。
你需要手动选择选项找到驱动（不要通过 Windows 自动升级的方式），导航到TPYBoard的USB驱动器并安装。
安装完毕后回到设备管理器找到安装后的TPYBoard，查看其使用了那个端口（例如 COM4）。
更多内容可以查看
`Windows `TPYBoard指南 <http://micropython.org/resources/Micro-Python-Windows-setup.pdf>`_
如果安装驱动程序有问题，请咨询本指南。

您现在需要运行您的终端程序。
你可以使用超级终端，如果你没有安装，或者下载免费程序putty:
`putty.exe <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_.
串口程序通过上一步找到的 COM 端口运行。
对于PuTTY , 点击其左边界面的“Session”，点击右边的“Serial”按钮
然后在串口行中选择COM端口（例如COM4），最后，点击“Open”按钮。

Mac OS X
----------

打开一个终端并运行：
::

    screen /dev/tty.usbmodem

当想要终止退出界面时，使用快捷键 CTPL-A CTRL-\

Linux
-------

打开终端并运行：
::

    screen /dev/ttyACM0

你也可以尝试 piocom 或者 minicom 的连接方式而非终端界面。
你需要使用 /dev/ttyACM1或者更高的ttyACM数字。
而且，用户需要给自己正确的权限连接该设备（例如组 uucp 或者 dialout，或者权限 sudo）

使用交互式选择器
---------------------

现在让我们试着在TPYBoard直接运行一些micropython代码。

打开串口程序（例如Putty，终端界面，piocom等等）可以看到一个光标闪烁着的空屏幕。
按下任意按键进入MicroPython 解释器，显示为 “>>>“。可以通过下面的程序确认是否进入：

>>> print("hello pyboard!")
hello pyboard!

在上面的例程中用户不需要敲入">>>"字符，而是应该在解释器中写入内容。
在最后，一旦输入 "print("hello pyboard!")"文本并按下回车键，输出结果将在屏幕上如上呈现。

如果你已经知道一些Python，你可以尝试一些基本的命令在这里。

如果打印不成功，尝试下边的硬件复位或者软件复位的方法。可以继续打入其他指令如：

>>> pyb.LED(1).on()
>>> pyb.LED(2).on()
>>> 1 + 2
3
>>> 1 / 2
0.5
>>> 20 * 'py'
'pypypypypypypypypypypypypypypypypypypypy'
    

复位
-------------------

如果出错可以通过两种方式复位开发板。
其一是在 MicroPython 解释器中打入 CTRL-D 进行软件复位。出现的消息如下所示：
::

    >>>
    TPYB: sync filesystems
    TPYB: soft reboot
    Micro Python v1.0 on 2014-05-03; TPYBoard v10x with STM32F405RG
    Type "help()" for more information.
    >>>
    

如果这是行不通的，你可以执行一个硬复位（关闭和再次打开）按RST按键硬件复位（开发板上USB接线下的黑色按键）。
这将断开与 TPYBoard的任何端口连接
如果你想准备进行硬件复位，建议你先关闭串口程序(PuTTY)和退出/卸载TPYBoard设备。
