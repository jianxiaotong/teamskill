import os
import random
import smtplib
import uuid
import time
from email.mime.text import MIMEText
from email.header import Header
from teamskillstack.models import EmailVerifyRecord

from django.db import connection
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from teamskill.settings import MEDIA_ROOT


sender = '1766540044@qq.com'  # 发送者邮箱
sender_pwd='bldukjbafkdrcfed' #邮件授权码


# # 跳转到主页面
# def index(request):
#     userId = request.session.get("userId")
#     if userId:
#         return render(request, 'index.html')
#     else:
#         return redirect("login/")


# 校验用户名
def valiName(request):
    name = request.GET['name']  # 用户名
    # 判断用户名是否存在
    cursor = connection.cursor()
    cursor.execute('select user_id from `user` where `name`=%s', [name])
    userId = cursor.fetchone()
    cursor.close()
    if userId:
        return JsonResponse({'code': 2001, 'message': "用户名已被占用"})
    return JsonResponse({'code': 200, 'message': "ok"})


# 校验邮箱号
def valiEmail(request):
    email = request.GET['email']
    # 判断用户名是否存在
    cursor = connection.cursor()
    cursor.execute('select user_id from `user` where email=%s', [email])
    userId = cursor.fetchone()
    cursor.close()
    if userId:
        return JsonResponse({'code': 2001, 'message': "邮箱号已被占用"})
    return JsonResponse({'code': 200, 'message': "ok"})

# 校验邮箱号
def valiEmailcode(request):
    email = request.POST['email']
    smscode = request.POST['smscode'] # 验证码
    # 判断用户名是否存在
    cursor = connection.cursor()
    cursor.execute('select code from emailRecord where email=%s', [email])
    codes = cursor.fetchone()
    cursor.close()
    if smscode == codes:
        return JsonResponse({'code': 2001, 'message': "验证码不正确"})
    else:
        return JsonResponse({'code': 200, 'message': "ok"})





# 封装一个方法直接传入邮件标题和内容
def postEmail(request):
    receivers=request.GET['email']  # 接收者邮件
    print(receivers)
    list = " "
    for i in range(6):
        n = random.randint(0, 9)
        s = str(n)
        list += s
    context = '您的验证码是：' + list  # 内容
    title = '邮件验证码'  # 标题
    # 三个参数：第一个为文本内容，第二个 设置文本格式，第三个 utf-8 设置编码
    msg = MIMEText(context, 'plain', 'utf-8')  # 发送内容
    msg['From'] = Header(sender)  # 发送者
    msg['To'] = Header(receivers, 'utf-8')  # 接收者
    msg['Subject'] = Header(title,'utf-8')  # 主题
    try:
        server = smtplib.SMTP("smtp.qq.com", 25)  # SMTP服务
        server.login(sender, sender_pwd)  # 邮箱用户名和密码  把密码改成授权码就行了
        server.sendmail(sender, receivers ,msg.as_string())  # 发送者和接收者
        #添加邮件验证表
        localTime = time.localtime(time.time())  # 获取当前时间
        formatTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)  # 格式化当前日期 ‘年-月-日 时：分：秒’
        cursor = connection.cursor()
        cursor.execute("insert into emailRecord (code, email, send_type, send_time) values (%s,%s,'注册',%s)",
                       [list, receivers, formatTime])
        return JsonResponse({'code':200,'message':list})
    except smtplib.SMTPException:
        return JsonResponse({'code':2001,'message':'获取失败，请重新获取'})


# 注册
def registerUser(request):
    name = request.POST['name'];  # 用户名
    email = request.POST['email'];  # 邮箱号
    password = request.POST['pass'];  # 密码
    localTime = time.localtime(time.time())  # 获取当前时间
    formatTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)  # 格式化当前日期 ‘年-月-日 时：分：秒’
    # 密码加密
    pwd = make_password(password, 'a')#123456
    cursor = connection.cursor()
    # 邮箱注册
    try:
        cursor.execute("insert into `user` (`name`, password, email, create_time) values (%s,%s,%s,%s)",
                           [name, pwd, email, formatTime])
        return JsonResponse({'code': 200, 'message': '注册成功'})
    except:
        return JsonResponse({'code': 2001, 'message': '注册失败'})


# 登录
def userLogin(request):
        email = request.POST['email']
        password = request.POST['password']
        cursor = connection.cursor()

        # 邮箱登录
        # 判断用户是否存在
        cursor.execute('select user_id,`name`,password,icon from `user` where email=%s', [email])
        user = cursor.fetchone()
        if user:
            # 判断密码是否正确  第一个参数明文 第二个密文
            ret = check_password(password, user[2])
            if ret:
                # 用户存session
                request.session['name'] = user[1]
                # request.session['user_id'] = user[0]
                # request.session['icon'] = user[3]
                useremail=user[1]
                return JsonResponse({'code': 200, 'message': '登陆成功','useremail':useremail})
            else:
                return JsonResponse({'code': 2001, 'message': '密码错误'})
        else:
            return JsonResponse({'code': 2002, 'message': '用户不存在'})


# 退出登录
def logout(request):
    # 清除sessoin
    request.session.clear();
    return HttpResponseRedirect('/login/')  # 跳转到登录页面




# 上传图片
def uploadImg(request):
    # 获取文件
    f1 = request.FILES['pic']
    # 通过uuid为文件重命名
    name = str(uuid.uuid1()) + "." + f1.name.split('.')[1]
    # 项目里的绝对路径
    fname = os.path.join(MEDIA_ROOT, name)
    # 上传到项目
    with open(fname, 'wb+') as pic:
        for c in f1.chunks():
            pic.write(c)
    # 把头像路径添加到数据库
    cursor = connection.cursor()
    userId = request.session['userId']
    # 获取当前数据库的头像路径
    cursor.execute('select icon from user where user_id=%s',[userId])
    img=cursor.fetchone()[0]
    # 如果是默认的头像不删除直接替换，否则删除后再替换
    path = MEDIA_ROOT
    if img!="1.jpg":
        os.remove(os.path.join(path, img))
    cursor.execute('update user set icon=%s where user_id=%s', [name, userId])
    cursor.close()
    request.session['icon'] = name;
    # 重定向到个人中心
    return HttpResponseRedirect('/personal/')


# 获取个人信息
def getUser(request):
    userId = request.session['userId']
    cursor = connection.cursor()
    cursor.execute('select user_id, password,user_name, email, phone, icon, cre_date from user where user_id=%s', [userId])
    result = cursor.fetchone()
    return JsonResponse({"result": result})


# 查看密码是否正确
def conpwd(request):
    password=request.POST['password']
    userId = request.session['userId']
    cursor = connection.cursor()
    cursor.execute('select password from user where user_id=%s',[userId])
    result = cursor.fetchone()[0]
    # 判断密码是否正确
    ret = check_password(password, result)
    if ret:
        return JsonResponse({"status":200})
    else:
        return JsonResponse({"status":2001,"message":"密码错误"})


#修改密码
def modifyPwd(request):
    npwd = request.POST['npassword']
    userId = request.session['userId']
    # 密码加密
    npwd = make_password(npwd, 'a')
    # 修改
    cursor = connection.cursor()
    try:
        cursor.execute('update user set password=%s where user_id=%s',[npwd,userId])
        return JsonResponse({"status":200,"message":"修改成功"})
    except:
        return JsonResponse({"status":2003,"message":"修改失败"})

# 个人中心的重置密码页面
def resetPassword(request):
    return render(request, 'resetPassword.html');

# 登录的重置密码页面
def resetPwd(request):
    return render(request, 'resetPwd.html');

# 重置密码
def updatePwd(request):
    pwd=request.POST['pwd']
    email = request.POST['email']
    userId = request.session['userId']
    # 密码加密
    pwd = make_password(pwd, 'a')
    # 修改
    cursor = connection.cursor()
    # 查找该用户是否通绑定邮箱
    cursor.execute('select user_id from user where email=%s and user_id=%s',[email,userId])
    user=cursor.fetchone()
    print(user)
    if user:
        try:
            cursor.execute('update user set password=%s where user_id=%s', [pwd, userId])
            return JsonResponse({"status": 200, "message": "修改成功"})
        except:
            return JsonResponse({"status": 2003, "message": "修改失败"})
    else:
        return JsonResponse({"status": 2001, "message": "用户不存在"})


# 绑定邮箱
def bindEmail(request):
    email = request.POST['email']
    userId = request.session['userId']
    # 修改
    cursor = connection.cursor()
    try:
        cursor.execute('update user set email=%s where user_id=%s', [email, userId])
        return JsonResponse({"status": 200, "message": "绑定成功"})
    except:
        return JsonResponse({"status": 2003, "message": "绑定失败"})

