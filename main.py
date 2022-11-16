# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import time

import requests
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

url = "https://qcsh.h5yunban.com/youth-learning/wx-share.php"
url1 = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/info'
# 拿到课程id
courseurl = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/common-api/course/current'
# 参加课程
joincourse='https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/course/join'
# 开始学习
learnurl='https://gqti.zzdtec.com/api/event'
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
        'Cookie': 'UM_distinctid=18387262709620-07cf36fa855185-64d265e-54ab0-1838726270a7b1; CNZZDATA1278620053=427443237-1664419275-%7C1668147141',
        'host': 'qcsh.h5yunban.com','Content-Type': 'application/json;charset=UTF-8'
        , 'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
        , 'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://qcsh.h5yunban.com/youth-learning/signUp-new.php?rom=1',
        'origin': 'https://qcsh.h5yunban.com'}
    headers = {'Cookie' : 'UM_distinctid=18387262709620-07cf36fa855185-64d265e-54ab0-1838726270a7bd; CNZZDATA1278620053=427443237-1664419275-%7C1668147141','host':'qcsh.h5yunban.com'
               ,'Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/9342 MicroMessenger/8.0.28.2240(0x28001C57) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
               ,'X-Requested-With': 'XMLHttpRequest','Referer': 'https://qcsh.h5yunban.com/youth-learning/signUp-new.php?rom=1' ,'origin':'https://qcsh.h5yunban.com'}
    payload = {'url':'https%3A%2F%2Fqcsh.h5yunban.com%2Fyouth-learning%2FsignUp-new.php%3From%3D1'}
    payload1 = {'accessToken':'C2680BEB-1318-4F17-9DFD-70C7542C174E'}






    # 开始学习的参数
    learndata = json.dumps({'guid':"d401cb35-30bf-81ef-2553-ec2a81ae90e1","tc":"1664419782968","tn":"1668150714407","n":"开始学习","u":"https://h5.cyol.com/special/daxuexi/dp1bsq1us7/m.html","d":"cyol.com","r":"https://h5.cyol.com/special/daxuexi/dp1bsq1us7/index.html","w":400,"m":"[{\"c\":\"2022\",\"s\":\"24\",\"prov\":\"9\",\"city\":\"10\"}]"})
    r = requests.get(courseurl,params=payload1,headers=headers)
    print("===============get courseId")
    print(r.status_code)
    r.raise_for_status()
    print(r.apparent_encoding)
    print(r.headers)
    rs = r.text.split("\"")
    courseId = rs[rs.index('id')+2]
    print(courseId)

    dict = {'course': 'C1045', 'nid': 'N0002000600081015', 'cardNo': '颜久博'}
    dict['course'] = courseId
    joindata = json.dumps(dict)
    r = requests.post(joincourse,params=payload1,headers = headers1,data=joindata)
    # r = requests.post(learnurl, headers=headerslearn, data=learndata)
    print("==================join course")
    print (r.status_code)
    r.raise_for_status()
    print(r.apparent_encoding)
    print(r.headers)
    print (r.text)
    #
    # time_start = time.time()
    # while('1'.__eq__(postHTMLText())):
    #     time.sleep(10)
    #     tim = time.time()-time_start
    #     print('token已生效时间：'+ str(tim))
    # total = time_end = time.time()
    # print('token生效总共时间为：'+str(total))


    r = requests.get(url1, params=payload1, headers=headers)
    print("===============info")
    print(r.status_code)
    r.raise_for_status()
    print(r.apparent_encoding)
    print(r.headers)
    print(r.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
