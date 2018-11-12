:mod:`wifi` --- Onboard Wifi
=============================================

.. module:: wifi
    :synopsis: Onboard Wifi

The main functionality and function of the ``wifi`` module

Function
----------------------

.. function:: start(ssid = "wifi_ssid", password = "password", mode = codey.wifi.STA)

   Start wifi connection, the API will not block process, API exit does not mean that wifi is connected, you need to call ``wifi.is_connected()`` to judge, Parameter：

  - *ssid* string type, wifi account.
  - *password* string type, wifi password.
  - *mode* starts the wifi mode.

.. function:: is_connected()

   Check if wifi is connected, the return value is Boolean, where ``True`` means that wifi has established a connection, ``False`` means that wifi has not yet established a connection.

Constant
----------------------

.. data:: wifi.STA

   The wifi station mode, that is, the wireless adapter mode. In this mode, wifi can be connected to the router.

.. data:: wifi.AP

   Wireless access point mode, the general wireless routing / bridge works in this mode. In this mode, it allows other wireless devices to access.

.. data:: wifi.APSTA

   The wifi AP and STA modes coexist.

Sample Code：
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