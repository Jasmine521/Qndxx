
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import time
import urllib.parse
import socket

import requests
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

url = "https://qcsh.h5yunban.com/youth-learning/assets/js/all1.js?v=636"
url1 = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/info'
# 拿到课程id
courseurl = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/common-api/course/current'
# 参加课程
joincourse='https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/course/join'
# 开始学习
learnurl='https://gqti.zzdtec.com/api/event'

ul1 =  'https://qcsh.h5yunban.com/youth-learning/cgi-bin/login/we-chat/callback?callback=https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2Fmine.php&scope=snsapi_userinfo&appid=wxa693f4127cc93fad&nickname=%25E4%25BA%2591%25E5%25B8%25B8%25E8%2588%2592%25E6%25B0%25B4%25E9%2595%25BF%25E4%25B8%259C&headimg=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FUIIYUMuyKFoKXicO6b6KQw34JfmpFkfwo3MHd5SkqA78iaZeZsERibWIDEicWV1HFT6gZMY6gcDa8AfHmaPzlBAToQ%2F132&time=1668496003&source=common&sign=C218A223236B18AC4039701DADD93Cs12&t=1768496003 '
# Press the green button in the gutter to run the script.
ul2 = 'https://wx.yunban.cn/wx/oauthInfoCallback?r_uri=https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2Fcgi-bin%2Flogin%2Fwe-chat%2Fcallback%3Fcallback%3Dhttps%253A%252F%252Fqcsh.h5yunban.com%252Fyouth-learning%252Findex.php%26scope%3Dsnsapi_userinfo&source=common&state=STATE&appid=wxa693f4127cc93fad#wechat_redirect'
def postHTMLText():
    try:
        r = requests.post(joincourse,params=payload1,headers = headers1,data=joindata)
        r.raise_for_status()
        return '1'
    except:
        return '0'
if __name__ == '__main__':


    print_hi('PyCharm')
    # 开始学习的头
    headerslearn = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'Content-Type': 'text/plain','accept': '*/*','origin': 'https://h5.cyol.com'
        ,'referer': 'https://h5.cyol.com/special/daxuexi/dp1bsq1us7/m.html'
    }
    # 获取openid 传入courseid的头
    headers1 = {
        'Cookie': 'UM_distinctid=18387262709620-07cf36fa855185-64d265e-54ab0-1838726270a7bd; CNZZDATA1278620053=427443237-1664419275-%7C1668147141',
        'host': 'qcsh.h5yunban.com'
        ,    'host': 'qcsh.h5yunban.com','Content-Type': 'application/json;charset=UTF-8'
        , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'X-Requested-With': 'com.tencent.mm',
        'sec-fetch-site':'cross-site',
        'sec-fetch-mode':'navigate',
        'Connection': 'keep-alive',
        'sec-fetch-dest':'document',
        'Referer': 'https://wx.yunban.cn/wx/oauthInfoCallback?r_uri=https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2Fcgi-bin%2Flogin%2Fwe-chat%2Fcallback%3Fcallback%3Dhttps%253A%252F%252Fqcsh.h5yunban.com%252Fyouth-learning%252Fmine.php%26scope%3Dsnsapi_userinfo&source=common&code=081HRiGa17OOeE0v0eIa1ZhTCA3HRiGl&state=STATE&appid=wxa693f4127cc93fad',
    'upgrade-insecure-requests': '1'}

    headers2 = {
        'cookie': 'PHPSESSID=ka91hco8ivcp3iuq6j0uh11533',
        'host': 'wx.yunban.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'X-Requested-With': 'com.tencent.mm',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'}
    payload2 = {'code': '083Gvn000nOhVO1Agt100A4dUT3Gvn0t'}
    headers = {'Cookie' : 'UM_distinctid=18387262709620-07cf36fa855185-64d265e-54ab0-1838726270a7bd; CNZZDATA1278620053=427443237-1664419275-%7C1668147141','host':'qcsh.h5yunban.com'
               ,'Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
               ,'X-Requested-With': 'XMLHttpRequest','Referer': 'https://qcsh.h5yunban.com/youth-learning/signUp-new.php?rom=1' ,'origin':'https://qcsh.h5yunban.com'}
    payload = {'url':'https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2FsignUp-new.php%3From%3D1'}
    payload1 = {'openid':'okMqsjkGt9CenI2WgTnDEPFcpEDc'}

    payjoin = {'accessToken': '6885F968-7377-427D-8689-B9BADE217450'}


    # 根据openid获取token 哈哈哈哈
    r = requests.get(ul1,headers=headers1,params=payload1)
    print("============asee")
    print(r.status_code)
    print(r.text)

    # 获取课程id
    # r = requests.get(courseurl, headers=headers1, params=payjoin)
    # print("============join")
    # print(r.status_code)
    # print(r.text)

    #
    # r = requests.post(joincourse, headers=headers1, params=payjoin)
    # print("============join")
    # print(r.status_code)
    # print(r.text)
    # HOST = 'open.weixin.qq.com'  # The remote host
    # PORT = 443  # The same port as used by the server
    # print(ul2)
    # # 根据code获取openid
    # r = requests.get(url=ul2, headers=headers2, params=payload2)
    # print("==========openid")
    # print(r.status_code)
    # print(r.headers)
    # print(r.text)





    # rs = re[re.index('redirect_uri=')+len('redirect_uri='):]
    # print(rs)
    # re = urllib.parse.unquote(rs)
    # print(re)

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

    lurl = 'https://open.weixin.qq.com/connect/oauth2/authorize_reply?allow=1&snsapi_userinfo=on&uuid=051sM1Zh2EM4ll2y&uin=Mjc4ODM0NDM0Ng==&key=9453ce6bd1e9fb003352941d86801286833371ddd8621ccadc0649f476f9de33dfca3f4f5b1154f1ac4bb89211d5427bad8c9af2e4ba5f803a12681bb833931aa4c9d0bb719d274322c47ec75f625511109012082678c9ae0893427166094a1faadf434be0ddba8dfc89b1d02ec6a03afb8feaab4be34006fdd03435ad9bb650&pass_ticket=pCDrfNlpPQbKe3F4or7LM2uxDCLw%2Bh2hOzDboQydrMvHDw%2BtmrbG5JXvnC0ZSbim&version=6305002e'
    lheaders = {
        'Host': 'open.weixin.qq.com',


    }
    r = requests.get(url=lurl,headers=lheaders)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
