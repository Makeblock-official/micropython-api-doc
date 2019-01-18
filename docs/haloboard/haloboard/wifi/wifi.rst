:mod:`wifi` --- Onboard WIFI
=============================================

.. module:: wifi
    :synopsis: Onboard WIFI

``wifi`` The main functionality and functions of the module

Function
----------------------

.. function:: start(ssid = "wifi_ssid", password = "password", mode = haloboard.wifi.STA)

   Start wifi connection, the API is not blocked, API exit does not mean that the Wi-Fi is connected, 
   "wifi.is_connected()"" needs to be called to determine, parameter:
- *ssid* - String type, Wi-Fi account.
- *password* - String type, Wi-Fi password.
- *mode* - Enable Wi-Fi mode, currently only supports WLAN_MODE_STA mode.

.. function:: set_mode(mode)

   Set Wi-Fi mode, parameters:
- *mode* - Refers to Wi-Fi mode, currently only supports WLAN_MODE_STA mode.

.. function:: connect()

   Connect WiFi.

.. function:: is_connected()

   Detect the wi-fi connection status, and the return value is a boolean value, 
   where "True" indicates that the Wi-Fi connection has been established and "False" indicates that the Wi-Fi connection has not been established.

.. function:: disconnect()

   Disconnect WiFi.

Sample Code 1：
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

Sample Code 2：
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
