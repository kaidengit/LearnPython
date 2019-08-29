import urllib.request

url = "http://www.baidu.com/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
# httpproxy_handler = urllib.request.ProxyHandler({"http" : "61.135.217.7:80"})
httpproxy_handler = urllib.request.ProxyHandler({"http" : "103.66.47.97:8080"})
nullproxy_handler = urllib.request.ProxyHandler({})

proxySwitch = True

if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

request = urllib.request.Request(url, headers=header)
response = opener.open(request)
print(response.read().decode('utf-8'))