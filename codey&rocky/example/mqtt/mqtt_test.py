# -*- coding: utf-8 -*-
from mqtt import MQTTClient
import codey
import time

MQTTHOST = "mq.makeblock.com"
MQTTPORT = 1883
client_id = "20180911203800"
Topic = "/sensors/temperature/#"

mqttClient = MQTTClient(client_id, MQTTHOST, port=MQTTPORT, user='zhangkun', password='zhangkun', keepalive=0,ssl=False)

# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect()


# publish 消息
def on_publish(topic, payload, retain=False, qos = 0):
    mqttClient.publish(topic, payload, retain, qos)

# 消息处理函数
def on_message_come(topic, msg):
    print(topic + " " + ":" + str(msg))


# subscribe 消息
def on_subscribe():
    mqttClient.set_callback(on_message_come)
    mqttClient.subscribe(Topic, qos = 1)

def sub_cb(topic, msg):
    print((topic, msg))

codey.wifi.start('Maker-guest', 'makeblock')
codey.led.show(0,0,0)
while True:
    if codey.wifi.is_connected():
        on_mqtt_connect()
        on_subscribe()
        codey.led.show(0,0,255)
        while True:
            if True:
                # Blocking wait for message
                on_publish("/sensors/temperature/home", str(38), qos = 1)
                mqttClient.wait_msg()
            else:
                # Non-blocking wait for message
                mqttClient.check_msg()
                # Then need to sleep to avoid 100% CPU usage (in a real
                # app other useful actions would be performed instead)
            time.sleep(1)
    else:
        codey.led.show(0,0,0)
