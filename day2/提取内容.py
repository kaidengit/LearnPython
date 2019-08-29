import requests
import re
url = "https://www.jupindai.com/book/87/23974066.html"

text = requests.get(url)
text.encoding = 'gbk'
# print(text.text)


title = re.findall('<h1 class="readTitle">(.*?)</h1>',text.text)[0]
print(title)
# \s:匹配任意的空白字符，\S:非空白字符
pat = '<div class="panel-body" id="htmlContent">([\s\S]*?)</div>'
regx = re.compile(pat)
sr = regx.findall(text.text)[0]
sr = re.sub("&nbsp;","",sr)
sr = re.sub("<br />","",sr)
print(sr)