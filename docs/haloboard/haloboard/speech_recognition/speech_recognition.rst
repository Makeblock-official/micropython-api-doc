:mod:`speech_recognition` --- 语音识别模块
=============================================

.. module:: speech_recognition
    :synopsis: 语音识别模块

``speech_recognition`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: start(server, language)

   启动语音识别服务，参数：
- *server* 服务器名称
- *language* 识别的语言

.. function:: get_error_code()

   获取结果数据的错误码。返回值对应结果如下：
- *0* : 正确返回
- *3300*： 语音输入参数不正确
- *3301*：语音数据不清晰
- *3302*：鉴权失败
- *3303*：原始音频或者服务端问题
- *3304*：用户请求超限(QPS)
- *3305*：用户请求超限(pv-日请求量)
- *3307*: 服务端问题
- *3308*：音频数据过长
- *3309*：音频数据异常
- *3310*：音频文件过大
- *3311*：采样率错误
- *3312*：音频格式错误
- *3333*：未知错误
- *3334*：响应超时

.. function:: get_error_message()

   获取错误的具体信息，字符串类型。

.. function:: get_result_code()

   获取识别的结果,如果发生错误或者超时，返回空字符串。

.. function:: get_sn_code()

   获取语音数据唯一标识，由服务器系统内部产生。

.. function:: get_all_respond()

   获取语音识别结果，包含整个回复信息，如错误信息等

程序示例一：
----------------------

.. code-block:: python

  # -*- coding: utf-8 -*-
  import haloboard
  import time
  import event

  @event.start
  def use_code():
      haloboard.wifi.start(ssid = "Maker-guest", password = "makeblock", mode = haloboard.wifi.WLAN_MODE_STA) 

      while(True):
          if haloboard.wifi.is_connected() == True:
              print("wifi is connected!")
              break;

      while True:
          if haloboard.button.is_pressed():
              haloboard.led.show_all(0, 0, 50)
              haloboard.speech_recognition.start(haloboard.speech_recognition.SERVER_MICROSOFT, haloboard.speech_recognition.LAN_DEFAULT, 2)
              if haloboard.speech_recognition.get_error_code() != 0:
                  str = haloboard.speech_recognition.get_error_message()
                  print("error_message:" + str)
              else:
                  result = haloboard.speech_recognition.get_result_code()
                  print("result:" + result)
                  if '红色' in result:
                      haloboard.led.show_all(50, 0, 0)
                  elif '黄色' in result:
                      haloboard.led.show_all(50, 50, 0)
                  elif '白色' in result:
                      haloboard.led.show_all(50, 50, 50)
                  elif '蓝色' in result:
                      haloboard.led.show_all(0, 0, 50)
                  elif '绿色' in result:
                      haloboard.led.show_all(0, 50, 0)
                  else:
                      haloboard.led.show_all(0, 0, 0)
          time.sleep(0.5)

程序示例二：
----------------------

.. code-block:: python

  # -*- coding: utf-8 -*-
  import haloboard
  import time
  import event

  haloboard.speech_recognition.set_recognition_url(haloboard.speech_recognition.SERVER_MICROSOFT, "http://msapi.passport3.makeblock.com/ms/bing_speech/interactive")
  haloboard.speech_recognition.set_token(haloboard.speech_recognition.SERVER_MICROSOFT, "ed8xubrmidv")
  # haloboard.speech_recognition.set_account(haloboard.speech_recognition.SERVER_MICROSOFT, "embeded@makeblock.com", "123456")

  @event.start
  def use_code():
      haloboard.wifi.start(ssid = "Maker-guest", password = "makeblock", mode = haloboard.wifi.WLAN_MODE_STA)

      while(True):
          if haloboard.wifi.is_connected() == True:
              print("wifi is connected!")
              break;
      
      while True:
          if haloboard.button.is_pressed():
              haloboard.led.show_all(0, 0, 50)
              haloboard.speech_recognition.start(haloboard.speech_recognition.SERVER_MICROSOFT, haloboard.speech_recognition.LAN_DEFAULT, 2)
              if haloboard.speech_recognition.get_error_code() != 0:
                  str = haloboard.speech_recognition.get_error_message()
                  print("error_message:" + str)
              else:
                  result = haloboard.speech_recognition.get_result_code()
                  print("result:" + result)
                  if '红色' in result:
                      haloboard.led.show_all(50, 0, 0)
                  elif '黄色' in result:
                      haloboard.led.show_all(50, 50, 0)
                  elif '白色' in result:
                      haloboard.led.show_all(50, 50, 50)
                  elif '蓝色' in result:
                      haloboard.led.show_all(0, 0, 50)
                  elif '绿色' in result:
                      haloboard.led.show_all(0, 50, 0)
                  else:
                      haloboard.led.show_all(0, 0, 0)
          time.sleep(0.5)
          