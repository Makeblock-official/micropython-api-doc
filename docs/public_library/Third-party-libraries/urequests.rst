:mod:`urequests` --- 网络请求模块
=============================================

.. module:: urequests
    :synopsis: 网络请求模块

``urequests`` 模块的主要功能与函数

功能相关函数
----------------------

.. function:: request(method, url, data=None, json=None, headers={})

   发送网络请求, 它会阻塞返回网络的响应数据，参数：

    - *method* 建立网络请求的方法，例如 ``HEAD``，``GET``，``POST``，``PUT``，``PATCH``, ``DELETE``。
    - *url* 网络请求的URL(网址)。
    - *data*（可选）在请求正文中发送的字典或元组列表[（键，值）]（将是表单编码的），字节或类文件对象。
    - *json*（可选）在请求正文中发送的json数据。
    - *headers*（可选）要与请求一起发送的HTTP标头字典。

.. function:: head(url, **kw)

   发送一个 HEAD 请求，返回类型是 request 的响应，参数：

    - *url* 网络请求的URL(网址)。
    - **kw request可选的参数

.. function:: get(url, **kw)

   发送一个 GET 请求，返回类型是 request 的响应，参数：

    - *url* 网络请求的URL(网址)。
    - **kw request可选的参数

.. function:: post(url, **kw)

   发送一个 POST 请求，返回类型是 request 的响应，参数：

    - *url* 网络请求的URL(网址)。
    - **kw request可选的参数

.. function:: put(url, **kw)

   发送一个 PUT 请求，返回类型是 request 的响应，参数：

    - *url* 网络请求的URL(网址)。
    - **kw request可选的参数

.. function:: patch(url, **kw)

   发送一个 PATCH 请求，返回类型是 request 的响应，参数：

    - *url* 网络请求的URL(网址)。
    - **kw request可选的参数

.. function:: delete(url, **kw)

   发送一个 DELETE 请求，返回类型是 request 的响应，参数：

    - *url* 网络请求的URL(网址)。
    - **kw request可选的参数

程序示例1：
------------

.. code-block:: python

  import codey
  import urequests as requests
  import time
  
  # 此处需填入自己路由器的 ssid 和 密码
  codey.wifi.start('wifi_ssid', 'password')
  codey.led.show(0,0,0)
  while True:
      if codey.wifi.is_connected():
          codey.led.show(0,0,255)
          res = requests.get(url='http://www.baidu.com/')
          print(res.text)
          time.sleep(3)
      else:
          codey.led.show(0,0,0)

程序示例2：
------------

.. code-block:: python

  import codey
  import urequests as requests
  import time
  
  # 此处需填入自己路由器的 ssid 和 密码
  codey.wifi.start('wifi_ssid', 'password')
  codey.led.show(0,0,0)
  hour = minite = second = "00"
  while True:
      if codey.wifi.is_connected():
          try:
              res = requests.get(url = 'http://www.time.ac.cn/timeflash.asp?user=flash').text
              hour_begin = res.find('<hour>') + len('<hour>')
              hour_end = res.find('</hour>')
              minite_begin = res.find('<minite>') + len('<minite>')
              minite_end = res.find('</minite>')
              second_begin = res.find('<second>') + len('<second>')
              second_end = res.find('</second>')
              if hour_begin > len('<hour>') and hour_end > hour_begin and \
                 minite_begin > len('<minite>') and minite_end > minite_begin and \
                 second_begin > len('<second>') and second_end > second_begin:
              
                  if hour_end - hour_begin == 1:
                      hour = '0' + res[hour_begin:hour_end]
                  elif hour_end - hour_begin == 2:
                      hour = res[hour_begin:hour_end]
              
                  if minite_end - minite_begin == 1:
                      minite = '0' + res[minite_begin:minite_end]
                  elif minite_end - minite_begin == 2:
                      minite = res[minite_begin:minite_end]
              
                  if second_end - second_begin == 1:
                      second = '0' + res[second_begin:second_end]
                  elif second_end - second_begin == 2:
                      second = res[second_begin:second_end]
              
                  print(hour + ":" + minite + ":" + second)
                  cur_time = hour + ':' + minite;
                  codey.display.show(cur_time)
          except:
              print("get error data")
      else:
          codey.led.show(0,0,0)

程序示例3：
------------

.. code-block:: python

  import codey
  import urequests as requests
  import ujson
  
  # user_account 和 password 的账户信息就是mblock的账户
  def get_user_request_header():
      post_data = ujson.dumps({ 'account': 'user_account', 'password': 'password'})
      request_url = 'http://passport2.makeblock.com/v1/user/login'
      res = requests.post(request_url, headers = {'content-type': 'application/json'}, data = post_data).json()
      header_data = ''
      if res['code'] == 0:
          header_data = { "content-type": 'application/json; charset=utf-8', "devicetype": '1'}
          header_data["uid"] = str(res['data']['user']['uid'])
          header_data["deviceid"] = '30AEA427EC60'
      return header_data
  
  # 获取天气信息
  # cid: 检查站id
  # arg: 需要查询的信息
  #            aqi:  空气质量指数
  #            pm25: PM2.5浓度
  #            pm10: PM10浓度
  #            co:   一氧化碳浓度
  #            so2:  二氧化硫浓度
  #            no2:  二氧化氮浓度
  deget_air_quality_info(cid, arg):
    if not codey.wifi.is_connected():
          return ''
      post_data = ujson.dumps({ "cid": cid, "arg": arg})
      request_url = 'http://msapi.passport3.makeblock.com/' + 'air/getone'
      res = requests.post(request_url, headers = get_user_request_header(), data = post_data)
      text = res.text
      return float(text)
  
  # 此处需填入自己路由器的 ssid 和 密码
  codey.wifi.start('wifi_ssid', 'password')
  codey.led.show(0,0,0)
  while True:
      if codey.wifi.is_connected():
          codey.led.show(0,0,255)
          data = get_air_quality_info('1539','aqi')  #1539 表示深圳测试点
          codey.display.show(data)
      else:
          codey.led.show(0,0,0)