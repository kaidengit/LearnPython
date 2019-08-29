import requests
import re

url = "http://acm.zzuli.edu.cn/problemset.php?page=1"
html = requests.get(url)
html.encoding = "utf-8"
print(html.text)

restr = """<a\shref='problem\.php\?id=(\d+)'>(.*?)</a>"""
regax = re.compile(restr)
ks = regax.findall(html.text)
print(ks)


