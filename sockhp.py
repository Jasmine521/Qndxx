# Echo client program
import socket

HOST = 'open.weixin.qq.com'    # The remote host
PORT = 443              # The same port as used by the server
geturl = '''GET https://open.weixin.qq.com/connect/oauth2/authorize_reply?allow=1&snsapi_userinfo=on&uuid=081zeCl93yctHa1G&uin=Mjc4ODM0NDM0Ng==&key=322dfba25112d455285fa4b78fb98a046337128098fbf696d70ae6a469eb86d3b309253b3cdb38d2626c8269013a29ef7cb1f08970a6a611a6d10127023a82cdcf8b11d7288dd548e839744c675c683ccfdd526dc7a5a2e217cefd6a96e3a0c23c915e763224c18d2e931782c0dcc85736bd6da0103c3c7c7d7305161901faa1&pass_ticket=pCDrfNlpPQbKe3F4or7LM2uxDCLw%2Bh2hOzDboQydrMuacqo7MySiZa%2FF7UY6NHns&version=6305002e HTTP/1.1
Host: open.weixin.qq.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Referer: https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxa693f4127cc93fad&redirect_uri=https%3A%2F%2Fwx.yunban.cn%2Fwx%2FoauthInfoCallback%3Fr_uri%3Dhttps%253A%252F%252Fqcsh.h5yunban.com%252Fyouth-learning%252Fcgi-bin%252Flogin%252Fwe-chat%252Fcallback%253Fcallback%253Dhttps%25253A%25252F%25252Fqcsh.h5yunban.com%25252Fyouth-learning%25252Findex.php%2526scope%253Dsnsapi_userinfo%26source%3Dcommon&response_type=code&scope=snsapi_userinfo&state=STATE&component_appid=wx0f0063354bfd3d19&uin=Mjc4ODM0NDM0Ng%3D%3D&key=322dfba25412d455285fa4b78fb98a046337128098fbf696d70ae6a469eb86d3b309253b3cdb38d2626c8269013a29ef7cb1f08970a6a611a6d10127023a82cdcf8b11d7288dd548e839744c675c683ccfdd526dc7a5a2e217cefd6a96e3a0c23c915e763224c18d2e931782c0dcc85736bd6da0103c3c7c7d7305161901faa1&version=6305002e&exportkey=n_ChQIAhIQaooXo10IaRUcI3ygVa%2B2HxLMAQIE97dBBAEAAAAAAIgkCvjBNtkAAAAOpnltbLcz9gKNyK89dVj0TBxwII9jvu5dNmXIpOOATfgJKXt9M6IdNLiLVloX3Fr4imX1PfMP4Wk2KNdZhjgF7ud%2B4kCZgKTyVdfLMkTZZX9Itv33z9aCpcDWB4m2UYwGXSICnXNq0PmpjVT%2F1Cq241CioL%2BsubkdzLPmW9LnTmEdFDV%2FQPsQnFTgWjjKW%2BFaRMRsEAev5gAYehQP9od6oJXpyBIRxKQBDkkltqFzWzF7811jZQ%3D%3D&pass_ticket=pCDrfNlpPQbKe3F4or7LM2uxDCLw%2Bh2hOzDboQydrMuacqo7MySiZa%2FF7UY6NHns&wx_header=0
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7




'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print(s.getsockname())
    s.sendall(geturl.encode())
    s.sendall(b'Hello, world')
    s.sendall(b'Hello, worldsse')
    data = s.recv(1024)
    # while data:
    #     response +=data
    #     data = s.recv(data)
print('Received', repr(data))