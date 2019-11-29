#
# import random
# import smtplib
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# list = " "
# for i in range(4):
#     n = random.randint(0, 9)
#     s = str(n)
#     list += s
# context = '您的验证码是：' + list  # 内容
# title = 'SMTP 邮件验证码'  # 标题
# # mail_msg = """
# # <p>邮件验证码...</p>
# # <p><a href="http://www.runoob.com">这是一个链接</a></p>
# # """
# msg = MIMEText(context, 'html', 'utf-8') # 发送内容
# msg['From'] = formataddr(["from", '1766540044@qq.com'])  # 发件人
# msg['To'] = formataddr(["to", 'jianxiaotong1@126.com'])  # 收件人
# msg['Subject'] =  Header(title)  # 主题
#
# server = smtplib.SMTP("smtp.qq.com", 25) # SMTP服务
# server.login("1766540044@qq.com", "bldukjbafkdrcfed") # 邮箱用户名和密码  把密码改成授权码就行了
# server.sendmail('1766540044@qq.com', ['jianxiaotong1@126.com', ], msg.as_string()) # 发送者和接收者
# server.quit()
#
