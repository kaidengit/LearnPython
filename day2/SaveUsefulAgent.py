import requests
import json
import gevent
from gevent import monkey
url = "http://www.baidu.com"
monkey.patch_all()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
def extract():
    with open("pro.json","r") as f:
        sr = f.read()
    dic = json.loads(sr)
    return dic

def trymd():
    proxies = {
        "https": "61.135.217.7:80",
        "http": "61.135.217.7:80"
    }
    try:
        requests.get(url,headers = headers,proxies = proxies)
    except Exception as f:
        print("Wrong!!!",f)
        return
def requ(proxy,b):
    try:
        requests.get(url, headers=headers, proxies=proxy, timeout=3)
        lst.append(b)
        print("可用proxies:", len(lst))
    except Exception as f:
        print("Wrong!!", f)

lst = list()
def main(dic):

    dic[10] = "61.135.217.7:80"
    for a,b in dic.items():
        # 增加线程，加快测试
        proxy = dict()
        proxy['http'] = b
        proxy['https'] = b
        g1 = gevent.spawn(requ,proxy,b)
    g1.join()


def writeJson():
    dic = dict()
    for i,proxy in enumerate(lst):
        dic[i] = proxy
    with open("useful.json",'a+') as f:
        f.write(json.dumps(dic))

if __name__ == "__main__":
    """爬取可用的proxy"""
    # 1.从文件提取所以proxy
    dic = extract() #提取
    # 2.测试模块是否可用
    trymd()
    # 3.测试可用的proxy，放入队列
    main(dic)
    # 4.编码为json格式放入文件
    writeJson()