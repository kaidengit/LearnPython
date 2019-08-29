import re
import requests
import smtplib
import time
from email.mime.text import MIMEText  # 导入 email 模块，MIMEText 和 Header 主要用来完邮件内容与邮件标题的定义。
from email.header import Header
from email.utils import formataddr

import logging

LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "#配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' #配置输出时间的格式，注意月份和天数不要搞乱了

logging.basicConfig(level=logging.WARNING,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    filename=r"test.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )



title = ""
i = 1294
def refresh():
    url = "http://www.jupindai.com/book/87.html"
    text = requests.get(url)
    text.encoding = 'gbk'
    sr = '<dd class="col-md-4"><a href="(.*?)">第' + str(i) + '章\s+(.*?)</a></dd>'
    # print(str)
    text = text.text
    # print(text)

    regx = re.compile(sr)
    sr =""
    text = regx.findall(text)
    if len(text) == 0:
        return sr
    print(text)
    text = text[0]
    sr =  "http://www.jupindai.com" +text[0]
    print(sr, text[1])
    return sr

def parser(text):
    global title
    url = text
    content = requests.get(url)
    content.encoding = 'gbk'

    text = content.text
    title = re.findall('<h1 class="readTitle">(.*?)</h1>', text)[0]
    print(title)
    # \s:匹配任意的空白字符，\S:非空白字符
    pat = '<div class="panel-body" id="htmlContent">([\s\S]*?)</div>'
    regx = re.compile(pat)
    sr = regx.findall(text)[0]
    sr = re.sub("&nbsp;", "", sr)
    sr = re.sub("<br />", "", sr)
    sr = re.sub("&amp;lt;/div&amp;gt;", "", sr)

    # print(sr)
    return sr

def spider():
    """爬取实现"""
    #1.抓取小说主页，判断是否有更新,有更新返回url
    text = refresh()
    content = ""
    #2.抓取详细界面
    if text != "":
        content = parser(text)
    #3.返回内容
    return content

def sends(content):
    """接受内容，并发送内容"""
    sender = "572245955@qq.com"
    passward = "bgjixsfzcmjdbede"
    subject = title
    receive = "572245955@qq.com"

    msg = MIMEText(content)
    msg['Subject'] = Header(subject)
    msg['From'] = formataddr(["小尘机器人",sender])
    msg['To'] = formataddr(['主人',sender])
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com',465)
        server.login(sender,passward)
        server.sendmail(sender,receive,msg.as_string())
    except:
        logging.error("发送失败！！")
        print("发送失败")


if __name__ == "__main__":
    """自动小说发送器"""
    while True:
        # 1. 自动爬取小说主页，返回小说内容
        content = spider()
        if content =="":
            debug = "第" +str(i) +"章还未更新！"
            print(debug)
            logging.warning(debug)
            time.sleep(10)
            continue

        # 2. 使用smtp服务器发送邮件
        sends(content)
        i+=1
        logging.debug(title+"发送成功！！！")
