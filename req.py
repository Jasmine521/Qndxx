# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import time
import urllib.parse

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


url = "https://qcsh.h5yunban.com/youth-learning/assets/js/all1.js?v=636"
url1 = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/info'
# 拿到课程id
courseurl = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/common-api/course/current'
# 参加课程
joincourse = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/course/join'
# 开始学习
learnurl = 'https://gqti.zzdtec.com/api/event'

ul1 = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/login/we-chat?callback=https://qcsh.h5yunban.com/youth-learning/index.php'


# Press the green button in the gutter to run the script.

def postHTMLText():
    try:
        r = requests.post(joincourse, params=payload1, headers=headers1, data=joindata)
        r.raise_for_status()
        return '1'
    except:
        return '0'


if __name__ == '__main__':
    print_hi('PyCharm')
    # 开始学习的头
    headerslearn = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'Content-Type': 'text/plain', 'accept': '*/*', 'origin': 'https://h5.cyol.com'
        , 'referer': 'https://h5.cyol.com/special/daxuexi/dp1bsq1us7/m.html'
    }
    # 获取openid 传入courseid的头
    headers1 = {
        'host': 'in.yunban.cn', 'Content-Type': 'application/json;charset=UTF-8'
        ,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'X-Requested-With': 'com.tencent.mm',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'Referer': 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/login/we-chat?callback=https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2Findex.php',
        'upgrade-insecure-requests': '1'}
    headers = {
        'Cookie': 'UM_distinctid=18387262709620-07cf36fa855185-64d265e-54ab0-1838726270a7bd; CNZZDATA1278620053=427443237-1664419275-%7C1668147141',
        'host': 'qcsh.h5yunban.com'
        , 'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://qcsh.h5yunban.com/youth-learning/signUp-new.php?rom=1',
        'origin': 'https://qcsh.h5yunban.com'}
    payload = {'url': 'https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2FsignUp-new.php%3From%3D1'}
    payload1 = {'accessToken': '6885F968-7377-427D-8689-B9BADE217450'}

    # r = requests.get(url,headers=headers)
    # print("============json")
    # f = open('response.json','w')
    # f.write(r.text)
    # f.close()

    headers3 = {
        'host': 'in.yunban.cn'
        ,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'X-Requested-With': 'com.tencent.mm',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'Referer': 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/login/we-chat?callback=https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2Findex.php',
        'upgrade-insecure-requests': '1'}

    headers4 = {
        'host': 'qcsh.h5yunban.com'
        ,
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'X-Requested-With': 'com.tencent.mm',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'Referer': 'https://qcsh.h5yunban.com/youth-learning/index.php',
        'upgrade-insecure-requests': '1'}
    r = requests.get(ul1, headers=headers4)
    print("===============info")
    print(r.status_code)
    r.raise_for_status()
    print(r.apparent_encoding)
    print(r.headers)
    print(r.text)
    rs = r.text.split('\'')
    re = rs[-2]
    print(re)

    r = requests.get(re, headers=headers3)
    print("===============info")
    print(r.status_code)
    r.raise_for_status()
    print(r.apparent_encoding)
    print(r.headers)
    print(r.text)
    rs = r.text.split('\'')
    print(rs[-2])
    # re = urllib.parse.unquote(rs[-2])
    # print(re)
    re = rs[-2]

    rs = re[re.index('redirect_uri=') + len('redirect_uri='):]
    print(rs)
    re = urllib.parse.unquote(rs)
    print(re)

    # time.sleep(1)
    #
    # 此处为请求微信oauth2认证，通过微信登录获取code  再用code获取openid， 最后调用qcsh接口用openid和appid合成qcsh自己的accessToken
    # r = requests.get(rs[-2], headers=headers1)
    # print("===============info")
    # print(r.status_code)
    # r.raise_for_status()
    # print(r.apparent_encoding)
    # print(r.headers)
    # print(r.text)
    # ####################

    # rs = r.text.split('\'')

    headers2 = {
        'cookie': 'PHPSESSID=ka91hco8ivcp3iuq6j0uh11433',
        'host': 'wx.yunban.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e)'
        , 'X-Requested-With': 'com.tencent.mm',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'}
    payload2 = {'code': '003ZEg10075ZTO1jfp300qiEoj0ZEg1I'}

    r = requests.get(url=re  , headers=headers2, params=payload1)
    print("==========openid")
    print(r.status_code)
    print(r.headers)
    print(r.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
