[Micropython]TPYBoard v202 文件查看与修改
========================================================

版权声明：翻译整理属于TPYBoard，转载时请以超链接形式标明文章原始出处和作者信息及本声明

前言
--------------

TPYBoard(Micropython)开发板上有搭建的文件系统，但是TPYBoard v202与TPYBoard v102有所不同，v202没有USB驱动器，所以只能通过串口或者Wifi方式访问。

简单命令的介绍
------------------------

显示文件列表
通过串口访问文件的方法，通过os列出当前目录下的文件和目录：

>>> import os
>>> os.listdir()
['boot.py', 'demos', 'drive', 'main.py']

查看当前目录

>>> os.getcwd()

改变当前目录

>>> os.chdir()

创建目录

>>> os.mkdir("demos")
os.mkdir("demos")

命令就是创建一个demos的目录，档执行os.listdir()时会显示['boot.py', 'main.py', 'demos']说明已经在开发板中建立了一个demos的目录。


删除指定文件

>>> os.remove()

删除指定目录

>>> os.rmdir()


查看和修改文件
-----------------------------------------

**首先打开工具，进入调试串口页面**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559117996837.png

进入到主页面后，选择好TPYBoard v202的串口，这里的串口位COM3，点击open(),注意波特率一定要调成115200

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559217503207.png

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559228312214.png

点击open出现下面界面

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559471388068.png

这个时候我们按下TPYboard v202的RST按键，就会出现下面界面

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559482825552.png

**查看文件内容**

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559501609896.png

只需要这两行代码即可，我们点击Send to ESP按钮，即可将这两行代码发送给我们的TPYBoard  v202开发板，下面是效果图

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559520178974.png

我们就可以看到这里面有三个文件，分别是boot.py，main.py，hello.py文件。下面我们查看hello.py文件的内容

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559534857841.png

这是直接打开文件的内容，下面我们通过串口工具查看，写完下面代码点解Send to ESP按钮将代码传给TPYBoard v202

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559542326782.png

**修改文件内容**

我们将hello.py中的内容修改为hello TurnipSmart，this is tpyboard V202

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559559745332.png

点击open按钮，选中hello.py,选中打开后出现下面的界面

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559569520690.png

我们修改hello.py中内容，点击Save to ESP按钮，就修改成功了

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559580371705.png

写入成功后，我们读取hello.py，看看里面是什么内容

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559588359216.png

里面内容变为hello TurnipSmart，this is tpyboard V202，下面我们看一下原文件的内容

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559597555963.png

同样内容变为hello TurnipSmart，this is tpyboard V202文件修改成功。


TPYBoard v202网络配置
---------------------------

下面我们将TPYBoard v202连接本地网络

.. image:: http://www.tpyboard.com/ueditor/php/upload/image/20170315/1489559613516829.png

页面会返回True，我们即配置成功。