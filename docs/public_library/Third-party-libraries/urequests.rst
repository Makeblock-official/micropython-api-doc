:mod:`urequests` --- Network Request Module
=============================================

.. module:: urequests
    :synopsis: Network Request Module

The main functionality and function of the ``urequests`` module

Function
----------------------

.. function:: request(method, url, data=None, json=None, headers={})

   Send a network request, it will block the response data returned to the network, parameters：

    - *method* method of establishing a network request. e.g. ``HEAD``，``GET``，``POST``，``PUT``，``PATCH``, ``DELETE``.
    - *url* URL of the network request.
    - *data* (optional), a dictionary, tuple list [(key, value)] (will be form coded), byte or class file object sent in the request body.
    - *json* (optional), json data sent in the request body.
    - *headers* (optional), HTTP header dictionary to be sent with the request.

.. function:: head(url, **kw)

   Send a ``HEAD`` request, the return type is the response of the request, parameters：

    - *url* URL of the network request.
    - **kw request optional parameters.

.. function:: get(url, **kw)

   Send a ``GET`` request, the return type is the response of the request, parameters：

    - *url* URL of the network request.
    - **kw request optional parameters.

.. function:: post(url, **kw)

   Send a ``POST`` request, the return type is the response of the request, parameters：

    - *url* URL of the network request.
    - **kw request optional parameters.

.. function:: put(url, **kw)

   Send a ``PUT`` request, the return type is the response of the request, parameters：

    - *url* URL of the network request.
    - **kw request optional parameters.

.. function:: patch(url, **kw)

   Send a ``PATCH`` request, the return type is the response of the request, parameters：

    - *url* URL of the network request.
    - **kw request optional parameters.

.. function:: delete(url, **kw)

   Send a ``DELETE`` request, the return type is the response of the request, parameters：

    - *url* URL of the network request.
    - **kw request optional parameters.

Sample Code 1：
------------

.. code-block:: python

  import codey
  import urequests as requests
  import time
  
  # Fill in your router's ssid and password here.
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

Sample Code 2：
------------

.. code-block:: python

  import codey
  import urequests as requests
  import time
  
  # Fill in your router's ssid and password here.
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

Sample Code 3：
------------

.. code-block:: python

  import codey
  import urequests as requests
  import ujson
  
  # user_account and password is mblock's account and password
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
  
  # Get weather information
  # cid: checkpoint id
  # arg: Information to be queried
  #            aqi:  Air Quality Index
  #            pm25: PM2.5 concentration
  #            pm10: PM10 concentration
  #            co:   Carbon monoxide concentration
  #            so2:  Sulfur dioxide concentration
  #            no2:  Nitrogen dioxide concentration
  def get_air_quality_info(cid, arg):
      if not codey.wifi.is_connected():
          return ''
      post_data = ujson.dumps({ "cid": cid, "arg": arg})
      request_url = 'http://msapi.passport3.makeblock.com/' + 'air/getone'
      res = requests.post(request_url, headers = get_user_request_header(), data = post_data)
      text = res.text
      return float(text)
  
  # Fill in your router's ssid and password here.
  codey.wifi.start('wifi_ssid', 'password')
  codey.led.show(0,0,0)
  while True:
      if codey.wifi.is_connected():
          codey.led.show(0,0,255)
          data = get_air_quality_info('1539','aqi')  #1539 is Shenzhen checkpoint id
          codey.display.show(data)
      else:
          codey.led.show(0,0,0)