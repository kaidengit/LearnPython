import urllib.request
url = "https://www.baidu.com"
res = urllib.request.urlopen(url)
print(res.info())
print(res.read())
