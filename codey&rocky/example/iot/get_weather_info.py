# -*- coding: utf-8 -*-
import codey
import urequests as requests
import ujson

#   获取天气信息
#   city_code: 城市编码, 可以在mblock上获取
#   data_type: 获取数据类型
#              0: 最高温度(℃)
#              1: 最低温度(℃)
#              2: 最高温度(℉)
#              3: 最低温度(℉)
#              4: 天气
#              5: 湿度
def get_weather_info(city_code, data_type):
    if not codey.wifi.is_connected():
        return ''
    request_url = 'http://mweather.makeblock.com/' + 'getweather?woeid=' + str(city_code) + '&type=' + str(data_type)
    resp = requests.get(request_url)
    text = resp.text
    if int(data_type) <= 3:
        return int(text)
    return text

codey.wifi.start('Maker-guest', 'makeblock')
codey.led.show(0,0,0)
while True:
    if codey.wifi.is_connected():
        codey.led.show(0,0,255)
        data = get_weather_info(2161853,4)  #2161853 表示深圳
        print(data)
        codey.display.show(data)
    else:
        codey.led.show(0,0,0)