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

#   添加云列表的数据
#   name: 数据名称
#   data: 数据
def get_cloud_list(name, index):
    if not codey.wifi.is_connected():
        return ''
    req_type = 'index'
    req_index = 0
    if index == 'random':
        req_type = 'random'
    elif index == 'last':
        req_type = 'last'
    else:
        index = int(index)
        if index > 0:
            req_index = index - 1
        else:
            return ''
    request_url = 'http://iothub.makeblock.com/' + 'meos/getCloudListItemByIndex?listName=' + name + '&type=' + req_type + '&index=' + str(req_index)
    res = requests.get(request_url, headers = get_user_request_header()).json()
    if(res['code'] == 0):
        return res['data']['itemData']['data']
    else:
        return ''

codey.wifi.start('Maker-guest', 'makeblock')
codey.led.show(0,0,0)
while True:
    if codey.wifi.is_connected():
        codey.led.show(0,0,255)
        data = get_cloud_list('Yan', 1)
        codey.display.show(data)
    else:
        codey.led.show(0,0,0)