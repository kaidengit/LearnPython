import requests

url = "http://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

proxies = {
    "https":"61.135.217.7:80",
     "http":"61.135.217.7:80"
}
try:
    content = requests.get(url,headers = headers,proxies = proxies,timeout = 5)
except Exception as f:
    print(f)
else:
    print(content)