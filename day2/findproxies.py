import urllib.request


url = "http://www.baidu.com"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
proxies = {
    "http":"219.159.38.201:56210"
}
openproxy = urllib.request.ProxyHandler(proxies)
# openproxy = urllib.request.ProxyHandler({})
# conttent = urllib.request.urlopen(url,proxies = proxies)

opener = urllib.request.build_opener(openproxy)
req = urllib.request.Request(url,headers = header)
try:
    content = opener.open(req)
except:
    print("失败！")
print(content.read().decode("utf-8"))
