:mod:`mqtt` --- Message Queue Telemetry Transmission
=============================================

.. module:: mqtt
    :synopsis: Message Queue Telemetry Transmission

``mqtt`` 模块的主要功能与函数

Class
----------------------

.. class:: MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={})

   Instantiating the interface object of MQTT client, parameters：

    - *client_id* the unique client id string used when connecting to the broker. If client_id is zero length or None, then one will be randomly generated. In this case, the parameter ``clean_session`` of the ``connect`` function must be ``True``.
    - *server* The host name or IP address of the remote server.
    - *port* (optional), the network port of the server host to connect to. The default port number is 1883. Please note that the default port number of the MQTT over SSL/TLS is 8833.
    - *user* (optional), the username registered on the server.
    - *password* (optional),  the password registered on the server.
    - *keepalive* (optional), the client’s keepalive time out value. Default is 60 s.
    - *ssl* (optional), whether enable the SSL/TLS support.
    - *ssl_params* (optional), SSL/TLS parameter.

    .. method:: connect(clean_session=True)

   Connect the client to the server, this is a blocking function, parameters：

    - *clean_session* a boolean that determines the client type. If ``True``, the broker will remove all information about this client when it disconnects. If ``False``, the client is a durable client and subscription information and queued messages will be retained when the client disconnects.


    .. method:: reconnect()

   Reconnect to the server using the details provided previously. You must call ``connect`` before calling this function.

    .. method:: disconnect()

   Disconnect from the server.

    .. method:: ping()

   Test the connectivity between the server and client.

    .. method:: set_last_will(topic, msg, retain=False, qos=0)

   Set the will to be sent to the server. If the client disconnects without calling ``disconnect()``, the server will post a message on its behalf, parameters：

    - *topic* The topic of the will post.
    - *msg* A will message to send.
    - *retain* If set to ``True``, the will message will be set to the last known ``good/reserved message`` for the topic.
    - *qos* Is used for the quality of service level of the will.

    .. method:: publish(topic, msg, retain=False, qos=0)

   A message is sent from the client to the agent and then sent from the agent to any client that subscribes to the matching topic, parameters：

    - *topic* The topic of the message should be posted.
    - *msg* The actual message to send.
    - *retain* If set to True, the will message will be set to the last known ``good/reserved message`` for the topic.
    - *qos* The level of quality of service to use.

    .. method:: subscribe(topic, qos=0)

   Subscribe to a topic of the service, this module provides some helper functions to subscribe and process messages directly. For example ``set_callback``, parameters：

    - *topic* The subject of the message to subscribe.
    - *qos* The level of quality of service to use.

    .. method:: set_callback(f)

   Sets the callback function for the topic subscription, which is called when the server responds to our subscription request, parameters：

    - *f* callback function.

    .. method:: wait_msg()

   Wait for the server until the server has no pending messages. This function is a blocking function.

    .. method:: check_msg()

   Check if the server has pending messages. If not, return directly, if any, do same processing as function ``wait_msg``.

Sample Code：
------------

.. code-block:: python

  from mqtt import MQTTClient
  import codey
  import time
  
  MQTTHOST = "mq.makeblock.com"
  MQTTPORT = 1883
  
  # Fill in as you like
  client_id = "20180911203800"
  
  # Example Path
  Topic = "/sensors/temperature/#"
  
  mqttClient = MQTTClient(client_id, MQTTHOST, port=MQTTPORT, user='test', password='test', keepalive=0, ssl=False)
  
  # Connect to the MQTT server
  def on_mqtt_connect():
      mqttClient.connect()
  
  # publish a message
  def on_publish(topic, payload, retain=False, qos = 0):
      mqttClient.publish(topic, payload, retain, qos)
  
  # message processing function
  def on_message_come(topic, msg):
      print(topic + " " + ":" + str(msg))
      codey.display.show(msg)
  
  # subscribe message
  def on_subscribe():
      mqttClient.set_callback(on_message_come)
      mqttClient.subscribe(Topic, qos = 1)
  
  # Fill in your router's ssid and password here.
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