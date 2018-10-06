[Micropython]TPYBoard v202 连接Putty教程
===================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

实验目的
-------------

	- 学习在PC机系统中通过putty连接开发板教程

所需器件
--------------

	- TPYBoard v202开发板 1块
	- micro USB数据线 1条

所需软件
----------------

	- TPYBoard v202开发板驱动 `点击下载 <http://www.micropython.net.cn/download/tool/163.html>`_
	- PuTTY_0.67.0.0.exe  `点击下载 <http://www.micropython.net.cn/download/tool/3.html>`_

Putty连接方法
----------------

**安装驱动**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556668728667.png


.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556688121032.png

首先将驱动下载并打开文件进行安装，执行CH341SER.EXE 会出现下图：

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556703306179.png

点击安装，安装成功会出现如下效果：

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556719107216.png

通过数据线将TPYBoard v102开发板连接电脑。打开桌面，右键点击我的电脑选择设备管理器。单击端口选项，会出现如下效果：

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556741930279.png

**注意事项**

如果在端口中没有出现红色方框中的选项，请确认以下几点：

	- 检查驱动程序（CH341SER）是否安装成功。
	- 安装驱动精灵且将TPYBoard v102开发板连接电脑的同时自动搜索与其匹配的驱动进行安装。
	- 检查TPYBoard-esp8266开发板与电脑的连接是否有误。

通过PUTTY连接TPYBoard v102开发板

双击下载后的PuTTY_0.67.0.0.exe软件，点击运行。红色方框中Host Name 填写端口中新加入的端口名字（这里可以写括号中的COM4）Port中填写115200。Connection type 中选择Serial选项。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556775793306.png

点击下图左方框，在右侧Flow control 选项中选择None。

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556798517874.png

点击Open按钮,会弹出如下界面：

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556809372737.png

点击TPYBoard v102开发板中的RST键，会出现如下界面：

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556824915207.png

当界面出现红色方框中的内容时说明TPYBoard v102开发板已经安装成功。现在可以编写python代码，如图：

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489556846690984.png

还可以使用快捷键Ctrl+C 停止运行程序，Ctrl +D 重新运行程序。
