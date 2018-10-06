# -*- coding: utf-8 -*-
import codey
import urequests as requests
import ujson

# deviceid 要根据自己的硬件MAC去填写, 用户的账户信息就是mblock的账户
def get_user_request_header():
    post_data = ujson.dumps({ 'account': 'guojia198769@163.com', 'password': 'a@@#198769'})
    request_url = 'http://passport2.makeblock.com/v1/user/login'
    res = requests.post(request_url, headers = {'content-type': 'application/json'}, data = post_data).json()
    header_data = ''
    if res['code'] == 0:
        header_data = { "content-type": 'application/json; charset=utf-8', "devicetype": '1'}
        header_data["uid"] = str(res['data']['user']['uid'])
        header_data["deviceid"] = '30AEA427EC60'
    return header_data

#   获取天气信息
#   cid: 检查站id
#   arg: 需要查询的信息
#              aqi:  空气质量指数
#              pm25: PM2.5浓度
#              pm10: PM2.5浓度
#              co:   一氧化碳浓度
#              so2:  二氧化硫浓度
#              no2:  二氧化氮浓度
def get_air_quality_info(cid, arg):
    if not codey.wifi.is_connected():
        return ''
    post_data = ujson.dumps({ "cid": cid, "arg": arg})
    request_url = 'http://msapi.passport3.makeblock.com/' + 'air/getone'
    res = requests.post(request_url, headers = get_user_request_header(), data = post_data)
    text = res.text
    return float(text)

codey.wifi.start('Maker-guest', 'makeblock')
codey.led.show(0,0,0)
while True:
    if codey.wifi.is_connected():
        codey.led.show(0,0,255)
        data = get_air_quality_info('1539','aqi')  #1539 表示深圳测试点
        codey.display.show(data)
    else:
        codey.led.show(0,0,0)