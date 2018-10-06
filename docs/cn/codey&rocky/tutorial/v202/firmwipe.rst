[Micropython]TPYBoard v202 固件的检查与擦除
========================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
-------------------

	- 学会TPYBoard v202开发板的固件完整性检查
	- 学会flash的擦除方法

准备工作
-----------------

	- TPYBoard v202板子 1块
	- micro USB数据线 1条
	- 电脑 1台（本次实验以win7为例）
	- PuTTY(工具)

固件完整性检查
-----------------------

第一步：下载安装所需的软件--PuTTY

第二步：连接TPYBoard v202开发板

通过USB数据线将电脑和TPYBoard v202开发板连接起来，会自动安装USB转串的驱动。安装完毕后，查看设备管理器，是否正确创建串口。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489557520973289.png

第三步：打开PuTTY，根据下图标记的红色框进行设置。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489557553767371.png

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489557752936716.png

第四步：设置完成后，单击open按钮。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489557763855186.png

第五步：按下板子上的rst，进行重置。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489557774682280.png

第六步：按下图命令操作

运行命令：

::

    import esp
    esp.check_fw()

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489557784930344.png

如果最后显示True，代表固件是完整的，否则可能存在问题。如果显示False，最好重新刷一次固件。
详情可参考下一篇文档进行固件的烧写。

固件的擦除
----------------------

第一步：安装Python环境

从Python的官方网站http://www.python.org下载最新的2.7版本

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489557824955933.png

第二步：安装esptool和pyserial

在命令行里运行：pip install esptool和pip install pyserial

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489557851831033.png

第三步：擦除flash

运行的指令::

	esptool.py --port COM3 erase_flash 

(注意：执行擦除的指令前，需要像烧录固件一样，让esp8266进入烧写模式)即按住板上的flash键不放，按下rst键，等待两秒，松开rst键，再松开flash键。
否则会出现如下的错误提示：A fatal error occurred: Failed to connect to ESP8226

固件成功擦除后，可参考下一篇文档进行固件的烧写。
