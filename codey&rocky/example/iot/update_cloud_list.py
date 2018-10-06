# -*- coding: utf-8 -*-
import codey
import urequests as requests
import ujson
import time

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

#   添加云列表的数据
#   name: 数据名称
#   data: 数据
def update_cloud_list(name, data):
    if not codey.wifi.is_connected():
        return ''
    post_data = ujson.dumps({ "listName": name, "data": data})
    request_url = 'http://iothub.makeblock.com/' + 'meos/postcloudlist'
    res = requests.post(request_url, headers = get_user_request_header(), data = post_data).json()
    if(res['code'] == 0):
        return res['data']
    else:
        return ''

codey.wifi.start('Maker-guest', 'makeblock')
codey.led.show(0,0,0)
while True:
    if codey.wifi.is_connected():
        codey.led.show(0,0,255)
        data = update_cloud_list('Yan','test')  #1539 表示深圳测试点
        codey.display.show(data)
        time.sleep(5)
    else:
        codey.led.show(0,0,0)