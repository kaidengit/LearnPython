import smtplib  # 导入 smtplib 发邮件模块，从面的脚本，邮件的发送、接收等相关服务，全部由 smtplib.SMTP 方法来完成
from email.mime.text import MIMEText  # 导入 email 模块，MIMEText 和 Header 主要用来完邮件内容与邮件标题的定义。
from email.header import Header
from email.utils import formataddr

def emailtxt(sources):
    #sender, receiver, subject, content


    sender = '572245955@qq.com'  #发送邮箱
    receiver = '122939425@qq.com'  #接收邮箱
    subject = '测试邮箱'  #发送邮件主题
    content=open(sources,'rb').read()  #以二进制方式读取内容，好转码
    smtpserver = 'smtp.qq.com'   #发送邮箱服务器，这是QQ邮箱。
    password = "bgjixsfzcmjdbede"   #发送邮箱用户/密码,这个需要在邮箱设置里面去找

    msg = MIMEText(content.decode("utf-8"))   #邮件正文,转码成utf-8格式
    msg['Subject'] = Header(subject)  #邮件主题,如果有编码，在后面添加
    msg['From'] = formataddr(["栋哥", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["辣鸡", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

    server = smtplib.SMTP_SSL(smtpserver, 465)
    print("连接邮箱")

    server.login(sender,password)
    print("登录邮箱")

    server.sendmail(sender,receiver,msg.as_string())
    print("发送成功")
    server.quit()


if __name__=='__main__':
    emailtxt("kangdong.txt")
