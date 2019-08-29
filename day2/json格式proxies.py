from selenium import webdriver
import re
import json

url = "http://www.xiladaili.com/https/"
brower = webdriver.Firefox()

lst = list()
def parse(url):
    try:
        brower.get(url)
    except Exception as f:
        print("Wrong!")
        return
    print(brower.page_source)
    regax = re.compile("<tr>\s+<td>(.*?)</td>")
    lit = regax.findall(brower.page_source)
    lst.extend(lit)
def load():
    dic = dict()
    for i,proxy in enumerate(lst):
        dic[i]=proxy
    with open('pro.json','a+') as f:
        f.write(json.dumps(dic))

if __name__ == "__main__":
    # 1,提取proxy，保存到链表
    for page in range(100):
        page = url + str(page)
        parse(page)

    # 2，写入json文件
    load()
    # brower.get(url)
    # print(brower.page_source)
    # brower.close()