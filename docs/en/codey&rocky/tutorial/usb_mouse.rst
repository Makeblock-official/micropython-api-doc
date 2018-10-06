使TPYBoard作为USB鼠标
=====================================

该TPYBoard 是一个USB设备，可配置为用作鼠标而不是默认的USB闪存驱动器。

为此，我们必须首先编辑boot.py文件以更改USB配置。
如果你还没有触到你的boot.py文件，那么它将会是这样的:
::
    # boot.py -- run on boot-up
    # can run arbitrary Python, but best to keep it minimal

    import pyb
    #pyb.main('main.py') # main script to run after this one
    #pyb.usb_mode('VCP+MSC') # act as a serial and a storage device
    #pyb.usb_mode('VCP+HID') # act as a serial device and a mouse

启用鼠标模式，请取消注释文件的最后一行，使其看起来像：
::
    pyb.usb_mode('VCP+HID') # act as a serial device and a mouse

如果您已经更改了boot.py文件，则需要使用的最小代码是：
::
    import pyb
    pyb.usb_mode('VCP+HID')

这告诉TPYBoard将其自身配置为启动时的VCP（虚拟COM端口，即串行端口）和HID（人机界面设备，在我们的例子中是鼠标）USB设备。

弹出/卸载TPYBoard驱动器，并使用RST开关重新设置。您的电脑现在应该检测到TPYBoard为鼠标！

手动发送鼠标事件
----------------------------

为了让鼠标做任何事情，我们需要将鼠标事件发送到PC。
我们将首先使用REPL提示手动进行此操作。使用串行程序连接到您的TPYBoard，并键入以下内容：
::
    >>> hid = pyb.USB_HID()
    >>> hid.send((0, 10, 0, 0))

你的鼠标应该向右移动10像素！在上面的命令中，您将发送4条信息：按钮状态，x，y和滚动。
数字10告诉PC机鼠标在x方向移动10个像素。

让我们让鼠标左右摆动：
::
    >>> import math
    >>> def osc(n, d):
    ...   for i in range(n):
    ...     hid.send((0, int(20 * math.sin(i / 10)), 0, 0))
    ...     pyb.delay(d)
    ...
    >>> osc(100, 50)

函数的第一个参数osc是要发送的鼠标事件的数量，第二个参数是事件之间的延迟（以毫秒为单位）。
尝试玩不同的数字。

**练习：让鼠标绕成一圈。**

用加速度计制作鼠标
-------------------------------------

现在让使用加速度计的鼠标移动基于TPYBoard的角度。
可以直接在REPL提示符下键入以下代码，也可以将其放入main.py文件中。
在这里，我们会加入main.py，因为要做到这一点，我们将学习如何进入安全模式。

目前，TPYBoard充当串行USB设备和HID（鼠标）。所以您无法访问main.py文件系统来编辑文件。

您也无法编辑您boot.py的HID模式，并使用USB驱动器恢复正常模式...

为了解决这个问题，我们需要进入安全模式。这在[安全模式教程]（tut-reset）中有描述，但是我们在此重复说明：

1. 按住USR开关。
2. 同时按住USR，按下并释放RST开关。
3. 然后LED将循环绿色至橙色至绿色+橙色并再次返回。
4. 继续按住USR，直到只有橙色LED点亮，然后放开USR开关。
5. 橙色LED应闪烁4次，然后关闭。
6. 你现在处于安全模式。

在安全模式下，boot.py并且main.py文件不被执行，因此TPYBoard启动时使用默认设置。
这意味着您现在可以访问文件系统（USB驱动器应该出现），您可以编辑main.py。（boot.py按原样离开，因为我们完成编辑后仍然要回到HID模式main.py。）

在main.py下面的代码中：

.. code-block:: python

    import pyb

    switch = pyb.Switch()
    accel = pyb.Accel()
    hid = pyb.USB_HID()

    while not switch():
        hid.send((0, accel.x(), accel.y(), 0))
        pyb.delay(20)

保存文件，弹出/卸载您的TPYBoard驱动器，并使用RST开关重置它。
它现在应该用作鼠标，并且板的角度将移动鼠标。尝试一下，看看是否可以让鼠标静止不动！

按USR开关停止鼠标移动。

你会注意到y轴是倒置的。这很容易解决：只需在上方的y坐标前放一个减号hid.send()。

恢复您的TPYBoard正常
--------------------------------

如果你按原样离开你的TPYBoard，每当你插入它，它就会像鼠标一样表现出来。
你可能想把它改成正常。要做到这一点，您需要先进入安全模式（见上文），然后编辑boot.py文件。
在boot.py文件中，注释掉（放在＃前面）的行与 VCP+HID设置，所以它看起来像：
::
    #pyb.usb_mode('VCP+HID') # act as a serial device and a mouse

保存文件，弹出/卸载驱动器，并重置TPYBoard。现在回到正常的工作模式。
