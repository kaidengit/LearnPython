import requests
import time
import re
url = "https://www.jupindai.com/book/87.html"
i = 1294
contenturl = "https://www.jupindai.com"

while True:
    text = requests.get(url)
    text.encoding = 'gbk'
    str = '<dd class="col-md-4"><a href="(.*?)">第'+str(i) + '章\s+(.*?)</a></dd>'
    # print(str)
    text = text.text
    print(text)
    regax = re.compile(str)
    text = regax.findall(text)
    if len(text) == 0:
        time.sleep(10)
        continue

    text = text[0]
    print(text[0],text[1])
    break

    time.sleep(50)
