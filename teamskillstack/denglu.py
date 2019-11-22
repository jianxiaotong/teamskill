
# coding:utf-8
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as authenticate_old
# import sys
from smtplib import SMTP_SSL


# mail_host="smtp.mxhichina.com"

class myldapBackend:
    def authenticate(self, username=None, password=None):
        if len(password) == 0:
            return None
        try:
            smtp = SMTP_SSL("smtp.mxhichina.com", 465)
            res = smtp.login(username + "@xxxxx你的邮箱地址后缀.com", password)
            if res[0] == 235:
                return self.get_or_create_user(username, password)
            else:
                return authenticate_old(username=username, password=password)
        except:
            return authenticate_old(username=username, password=password)

    def get_or_create_user(self, username, password):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # info=sys.exc_info()
            # print(info[0],":",info[1])
            mail = username + "@xxxxx你的邮箱地址后缀.com"
            user = User(username=username, email=mail)
            user.is_staff = True
            user.is_superuser = False
            user.set_password('passwd set by mail!#..')
            user.save()
            # ug.user.add(user)
        return user