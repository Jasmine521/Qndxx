
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
joincourse='https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/course/join'
# 开始学习
learnurl='https://gqti.zzdtec.com/api/event'

ul1 =  'https://qcsh.h5yunban.com/youth-learning/cgi-bin/login/we-chat/callback?callback=https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2Fmine.php&scope=snsapi_userinfo&appid=wxa693f4127cc93fad&nickname=%25E4%25BA%2591%25E5%25B8%25B8%25E8%2588%2592%25E6%25B0%25B4%25E9%2595%25BF%25E4%25B8%259C&headimg=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FUIIYUMuyKFoKXicO6b6KQw34JfmpFkfwo3MHd5SkqA78iaZeZsERibWIDEicWV1HFT6gZMY6gcDa8AfHmaPzlBAToQ%2F132&time=1668496003&source=common&sign=C218A223236B18AC4039701DADD93Cs12&t=1768496003 '
# Press the green button in the gutter to run the script.

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
    headers = {'Cookie' : 'UM_distinctid=18387262709620-07cf36fa855185-64d265e-54ab0-1838726270a7bd; CNZZDATA1278620053=427443237-1664419275-%7C1668147141','host':'qcsh.h5yunban.com'
               ,'Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
               ,'X-Requested-With': 'XMLHttpRequest','Referer': 'https://qcsh.h5yunban.com/youth-learning/signUp-new.php?rom=1' ,'origin':'https://qcsh.h5yunban.com'}
    payload = {'url':'https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2FsignUp-new.php%3From%3D1'}
    payload1 = {'openid':'okMqsjkGt9CenI2WgTnDEPFcpEDc'}


    r = requests.get(ul1,headers=headers1,params=payload1)
    print("============asee")
    print(r.status_code)
    print(r.text)



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


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
