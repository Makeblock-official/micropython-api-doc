:mod:`wifi` --- 板载wifi
=============================================

.. module:: wifi
   :synopsis: 板载wifi

``wifi`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: start(ssid = "Maker-guest", password = "makeblock", mode = codey.wifi.STA)

   启动wifi连接，该API不阻塞，API退出不代表wifi已连接上，需要调用wifi.is_connected()判断。参数：

  - *ssid* 字符串类型，wifi账号。
  - *password* 字符串类型，wifi 密码。
  - *mode* 启动wifi的模式。

.. function:: is_connected()

    检测wifi是否已连接上，返回值是布尔值，其中 ``True`` 表示wifi已经建立连接，``False`` 表示wifi尚未建立连接。

常量
----------------------

.. data:: wifi.STA

   WiFi的站点模式，即无线网卡模式，该模式下，wifi可以连接到路由器。

.. data:: wifi.AP

   WiFi的无线接入点模式，一般的无线路由/网桥工作在该模式，该模式下，wifi可以允许其它无线设备接入。

.. data:: wifi.APSTA

   WiFi的AP和STA模式共存。

程序示例：
----------------------

.. code-block:: python

  import codey
  codey.wifi.start('makeblock', 'password', codey.wifi.STA)
  codey.led.show(0,0,0)
  while True:
      if codey.wifi.is_connected():
          codey.led.show(0,0,255)
  
      else:
          codey.led.show(0,0,0)