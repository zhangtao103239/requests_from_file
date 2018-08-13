# requests_from_file
从火狐文件中创造requests请求体

因为某种原因，我需要从火狐等浏览器中抓取请求信息，每次都自己根据请求构造太过麻烦，所以用这个来帮我从文件中读取请求配置

## install
使用pip
```python
pip install requests_from_file
```
## 使用方法
```python
from requests_from_file import requestFactory
factory=requestsFactory(headerFileName="http/header/file",contentFileName="http/heade/content/file")
factory.params
r = factory.request()
```
其中 headerFile 是从火狐等浏览器抓取下来的请求头文件，他的样子如下图所示
```
GET /tax_view?keyno=3ceaa2674e137a392d9986ad2f02aa28&ajaxflag=1 HTTP/1.1
Host: www.qichacha.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://www.qichacha.com
X-Requested-With: XMLHttpRequest
Cookie: name=cookie;url=ssss;
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
```
而如果是post请求，那么post参数有两种形式，
1. 以json形式发送的，请以
```
Json:[other:params]
```
形式附加在header文件最后
2. 以multipart发送的，请另存一个文件，并传递给contentFileName参数


## 结果
读入文件后，相应的参数以 headers,json,data,cookies形式（和requests对应）保存在params内，
并可以使用requests.request的方法直接请求，也可以使用requestFactory的request方法请求
