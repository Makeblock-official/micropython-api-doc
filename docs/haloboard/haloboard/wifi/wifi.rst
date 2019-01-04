:mod:`wifi` --- 板载WiFi模块
=============================================

.. module:: wifi
    :synopsis: 板载WiFi模块

``wifi`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: start(ssid = "wifi_ssid", password = "password", mode = haloboard.wifi.STA)

   启动wifi连接，该API不阻塞，API退出不代表Wi-Fi已连接上，需要调用 wifi.is_connected() 判断，参数：
- *ssid* 字符串类型，Wi-Fi账号。
- *password* 字符串类型，Wi-Fi密码。
- *mode* 启动Wi-Fi的模式，目前只支持WLAN_MODE_STA

.. function:: set_mode(mode)

   设置Wi-Fi的模式，参数：
- *mode* 指WiFi模式，目前只支持WLAN_MODE_STA。

.. function:: connect()

   连接WiFi

.. function:: is_connected()

   检测Wi-Fi连接状态，返回值是布尔值，其中 True 表示Wi-Fi已经建立连接，False 表示Wi-Fi尚未建立连接。

.. function:: disconnect()

   断开WiFi连接

程序示例一：
----------------------

.. code-block:: python

  import haloboard
  haloboard.wifi.start('Maker-guest', 'makeblock')
  haloboard.led.show_all(0,0,0)
  while True:
      if haloboard.wifi.is_connected():
          haloboard.led.show_all(0,0,255)

      else:
          haloboard.led.show_all(0,0,0)

程序示例二：
----------------------

.. code-block:: python

  import haloboard
  import event

  @event.button_pressed
  def on_button():
      haloboard.stop_other_scripts()
      print("start toconnect Maker-guest")
      haloboard.wifi.start('Maker-guest', 'makeblock')
      haloboard.led.show_all(0,0,0)
      while True:
          if haloboard.wifi.is_connected():
              haloboard.led.show_all(0,0,255)
              break
          else:
              haloboard.led.show_all(0,0,0)

  @event.touchpad0_active
  def on_touchpad0_active():
      haloboard.stop_other_scripts()
      print("start toconnect iPhone fftust")
      haloboard.wifi.start('iPhone fftust', '19920112')
      haloboard.led.show_all(0,0,0)
      while True:
          if haloboard.wifi.is_connected():
              haloboard.led.show_all(0,0,255)
              break
          else:
              haloboard.led.show_all(0,0,0)
