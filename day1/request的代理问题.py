import requests
from lxml import etree

url = "https://www.ipip.net/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
proxies ={"http" : "61.135.217.7:80"}

res = requests.get(url,headers = header,proxies = proxies)

status=res.status_code # 状态码
print(status)
content=res.text
html=etree.HTML(content)
ip=html.xpath('//ul[@class="inner"]/li[1]/text()')[0]
print("当前请求IP地址为："+ip)

# print(res.text)
