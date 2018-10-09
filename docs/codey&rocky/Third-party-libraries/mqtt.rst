:mod:`mqtt` --- 消息队列遥测传输
=============================================

.. module:: mqtt
   :synopsis: 消息队列遥测传输

``mqtt`` 模块的主要功能与函数

功能相关函数
----------------------

.. class:: MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={})

   实例化MQTT客户端的接口对象，参数:

   - *client_id* 连接到代理时使用的唯一客户端ID字符串，如果client_id为零长度或无，则将随机生成一个。在这种情况下，``connect``的clean_session参数必须为True。
   - *server* 远程服务器的主机名或IP地址。
   - *port*（可选）要连接的服务器主机的网络端口。 默认为1883，请注意，MQTT over SSL / TLS的默认端口是8883。
   - *user*（可选）在服务器上注册的用户名。
   - *password*（可选）在服务器上注册的密码。
   - *keepalive*（可选）客户端的keepalive超时值。 默认为60秒。
   - *ssl*（可选）是否使能 SSL/TLS 支持。
   - *ssl_params*（可选）SSL/TLS 参数。

    .. method:: connect(clean_session=True)

    将客户端连接到服务器。 这是一个阻塞函数，参数：

    - *clean_session* 一个确定客户端类型的布尔值。 如果为True，服务器将在断开连接时删除有关此客户端的所有信息。
      如果为False，则客户端是持久客户端，并且当客户端断开连接时，将保留订阅信息和排队消息。


    .. method:: reconnect()

    使用先前提供的详细信息重新连接到服务器。 在调用此函数之前，您必须调用 ``connect``。

    .. method:: disconnect()

    与服务器断开连接。

    .. method:: ping()

    测试客户端与服务器的连通性。

    .. method:: set_last_will(topic, msg, retain=False, qos=0)

    设置要发送给服务器的遗嘱。 如果客户端断开而没有调用disconnect()，服务器将代表它发布消息。

    - *topic* 该遗嘱消息发布的主题。
    - *msg* 要发送的遗嘱消息。。
    - *retain* 如果设置为True，遗嘱消息将被设置为该主题的“最后已知良好”/保留消息。
    - *qos* 用于遗嘱的服务质量等级。

    .. method:: publish(topic, msg, retain=False, qos=0)

    从客户端向代理发送消息，然后从代理发送到订阅匹配主题的任何客户端。 参数：

    - *topic* 应该发布消息的主题。
    - *msg* 要发送的实际消息。。
    - *retain* 如果设置为True，遗嘱消息将被设置为该主题的“最后已知良好”/保留消息。
    - *qos* 要使用的服务质量水平。

    .. method:: subscribe(topic, qos=0)

    订阅服务的某个主题，该模块提供了一些辅助函数，可以直接订阅和处理消息。例如 ``set_callback``。

    - *topic* 要订阅消息的主题。
    - *qos* 要使用的服务质量水平。

    .. method:: set_callback(f)

    设置主题订阅的回调函数，当服务器响应我们的订阅请求时调用。参数：

    - *f* 回调函数。

    .. method:: wait_msg()

    等待服务器直到服务器无待处理消息。该函数是阻塞函数。

    .. method:: check_msg()

    检查服务器是否有待处理消息。如果没有，直接返回，如果有的话，同 ``wait_msg``的处理。

程序示例：
------------

.. code-block:: python

  from mqtt import MQTTClient
  import codey
  import time
  
  MQTTHOST = "mq.makeblock.com"
  MQTTPORT = 1883
  
  # 任意填写
  client_id = "20180911203800"
  
  # 示例
  Topic = "/sensors/temperature/#"
  
  mqttClient = MQTTClient(client_id, MQTTHOST, port=MQTTPORT, user='test', password='test', keepalive=0, ssl=False)
  
  # 连接MQTT服务器
  def on_mqtt_connect():
      mqttClient.connect()
  
  # 发布消息
  def on_publish(topic, payload, retain=False, qos = 0):
      mqttClient.publish(topic, payload, retain, qos)
  
  # 消息处理函数
  def on_message_come(topic, msg):
      print(topic + " " + ":" + str(msg))
      codey.display.show(msg)
  
  # subscribe 消息
  def on_subscribe():
      mqttClient.set_callback(on_message_come)
      mqttClient.subscribe(Topic, qos = 1)
  
  # 此处填入自己家的wiif账户和密码
  codey.wifi.start('wifi_ssid', 'password')
  codey.led.show(0,0,0)
  codey.display.show(0)
  while True:
      if codey.wifi.is_connected():
          on_mqtt_connect()
          on_subscribe()
          codey.led.show(0,0,255)
          while True:
              # Blocking wait for message
              on_publish("/sensors/temperature/home", str(38), qos = 1)
              mqttClient.wait_msg()
              time.sleep(1)
      else:
          codey.led.show(0,0,0)