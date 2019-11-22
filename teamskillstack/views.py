import MySQLdb
from django.db import connection, transaction
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
# coding=utf8
from pymongo import auth
from pymongo.auth import authenticate

from teamskillstack.models import Team,Function,Skill

#职位名称
def getFunctionName(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("SELECT function_name from `function`")
    namelist=cursor.fetchall()
    if (namelist == ()):
        code = 2002
        message = '暂无数据'
        return JsonResponse({'code': code, "message": message, "data": namelist})
    cursor.close()
    code = 200
    message = '查询成功'
    return JsonResponse({'code': code, "message": message,"data":namelist})

#团队名称
def getTeamName(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("SELECT team_name from team")
    namelist=cursor.fetchall()
    if (namelist == ()):
        code = 2002
        message = '暂无数据'
        return JsonResponse({'code': code, "message": message, "data": namelist})
    cursor.close()
    code = 200
    message = '查询成功'
    return JsonResponse({'code': code, "message": message,"data":namelist})

#权限名称
def getPermissionName(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("SELECT permission_name from Permission")
    namelist=cursor.fetchall()
    if (namelist == ()):
        code = 2002
        message = '暂无数据'
        return JsonResponse({'code': code, "message": message, "data": namelist})
    cursor.close()
    code = 200
    message = '查询成功'
    return JsonResponse({'code': code, "message": message,"data":namelist})

# 添加团队
def addTeam(request):
        teamName = request.POST['team_name']# 获取团队名
        teamComment = request.POST['team_comment']  # 获取
        try:
            # 查询是否在数据库里存在
            cursor = connection.cursor()
            cursor.execute('select team_id from team where team_name=%s', [teamName])
            tid = cursor.fetchone()
            if tid:
                return JsonResponse({'code': 2003, 'message': '团队名字已被占用，请换个名字'})
            # 创建保存点
            save_id = transaction.savepoint()
            # 添加
            cursor.execute('insert into team(team_name,team_comment) values(%s,%s)', [teamName,teamComment])
            cursor.close()
            # 成功的话保存
            transaction.savepoint_commit(save_id)
            return JsonResponse({'code': 200, 'message': '添加成功'})
        except:
            # 失败的时候回滚到保存点
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'code': 2001, 'message': '添加失败'})

#获取团队列表
def getTeamList(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    # curPage = request.GET.get('page')  # 当前页数
    # pageSize = request.GET.get('size')  # 每页几条
    # count = Team.objects.all().count()  # 总条数
    # totalPage = count / int(pageSize)  # 总页数
    # if count != 0:
    #     if count % int(pageSize) != 0:
    #         totalPage = totalPage + 1
    #         # 当页数大于总页数，直接返回
    #     if int(curPage) > totalPage:
    #         return JsonResponse({'code': 2003, "message": '当前页数大于总页数'})
    #     startnum = (int(curPage) - 1) * int(pageSize)  # 计算sql需要的起始索引
    #     endnum = int(pageSize)
    cursor.execute('select * from Team ')
    data2 = cursor.fetchall()
    cursor.close()
    return JsonResponse({'code': 200, 'message': '查询成功', 'data': data2})

#添加职能
def addFunction(request):
        teamName = request.POST['team_name']  # 获取团队名
        functionName = request.POST['function_name']
        functionComment = request.POST['function_comment']
        try:
            # 查询是否在数据库里存在
            cursor = connection.cursor()
            cursor.execute('select function_id from `function` where function_name=%s and function_comment=%s', [functionName,functionComment])
            tid = cursor.fetchone()
            if tid:
                return JsonResponse({'code': 2003, 'message': '职能已经存在,请重新输入'})
            # 查询team_id
            cursor.execute('select team_id from team where team_name=%s', [teamName])
            team_id = cursor.fetchone()[0]
            # 创建保存点
            save_id = transaction.savepoint()
            # 添加
            cursor.execute('insert into `function`(function_name,function_comment) values(%s,%s)', [functionName,functionComment])
            # 查询function_id
            cursor.execute('select function_id from `function` order by function_id desc limit 1')
            function_id = cursor.fetchone()[0]
            cursor.execute('insert into teamFunction(team_id,function_id) values(%s,%s)', [team_id, function_id])
            cursor.close()
            # 成功的话保存
            transaction.savepoint_commit(save_id)
            return JsonResponse({'code': 200, 'message': '添加成功'})
        except:
            # 失败的时候回滚到保存点
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'code': 2001, 'message': '添加失败'})

#职能列表
def getFunctionList(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    # curPage = request.GET.get('page')  # 当前页数
    # pageSize = request.GET.get('size')  # 每页几条
    # count = Function.objects.all().count()  # 总条数
    # totalPage = count / int(pageSize)  # 总页数
    # if count != 0:
    #     if count % int(pageSize) != 0:
    #         totalPage = totalPage + 1
    #         # 当页数大于总页数，直接返回
    #     if int(curPage) > totalPage:
    #         return JsonResponse({'code': 2003, "message": '当前页数大于总页数'})
    #     startnum = (int(curPage) - 1) * int(pageSize)  # 计算sql需要的起始索引
    #     endnum = int(pageSize)
    cursor.execute('select t.team_name,f.function_name,f.function_comment,f.function_id from `function`f,team t,teamFunction tf where tf.team_id=t.team_id and tf.function_id=f.function_id ')
    data2 = cursor.fetchall()
    cursor.close()
    return JsonResponse({'code': 200, 'message': '查询成功', 'data': data2})

#添加技能
def addSkill(request):
        functionName = request.POST['functionName']
        skillName = request.POST['skillName']
        skillType = request.POST['skillType']
        try:
            # 查询是否在数据库里存在
            cursor = connection.cursor()
            cursor.execute('select skill_id from skill where skill_name=%s and skill_type=%s', [skillName,skillType])
            tid = cursor.fetchone()
            if tid:
                return JsonResponse({'status': 2003, 'message': '技能已存在，请重新添加'})
            #查询function_id
            cursor.execute('select function_id from `function` where function_name=%s', [functionName])
            function_id=cursor.fetchone()[0]
            # 创建保存点
            save_id = transaction.savepoint()
            # 添加技能
            cursor.execute('insert into skill(skill_name,skill_type) values(%s,%s)', [skillName,skillType])
            #查询skill_id
            cursor.execute('select skill_id from skill order by skill_id desc limit 1')
            skill_id = cursor.fetchone()[0]
            #添加技能和职能联系
            cursor.execute('insert into skillFunction(skill_id,function_id) values(%s,%s)', [skill_id, function_id])
            cursor.close()
            # 成功的话保存
            transaction.savepoint_commit(save_id)
            return JsonResponse({'code': 200, 'message': '添加成功'})
        except:
            # 失败的时候回滚到保存点
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'code': 2001, 'message': '添加失败'})

#技能列表
def getSkillList(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    # curPage = request.GET.get('page')  # 当前页数
    # pageSize = request.GET.get('size')  # 每页几条
    # count = Skill.objects.all().count()  # 总条数
    # totalPage = count / int(pageSize)  # 总页数
    # if count != 0:
    #     if count % int(pageSize) != 0:
    #         totalPage = totalPage + 1
    #         # 当页数大于总页数，直接返回
    #     if int(curPage) > totalPage:
    #         return JsonResponse({'code': 2003, "message": '当前页数大于总页数'})
    #     startnum = (int(curPage) - 1) * int(pageSize)  # 计算sql需要的起始索引
    #     endnum = int(pageSize)
    cursor.execute('select s.skill_id,s.skill_name,s.skill_type,f.function_name from skill s,`function` f,skillfunction sf '
                       'where s.skill_id=sf.skill_id and f.function_id=sf.function_id ')
    data2 = cursor.fetchall()
    cursor.close()
    return JsonResponse({'code': 200, 'message': '查询成功', 'data': data2})

#团队技术栈
def showTeamSkill(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    # curPage = request.GET.get('page')  # 当前页数
    # pageSize = request.GET.get('size')  # 每页几条
    # count = Skill.objects.all().count()  # 总条数
    # totalPage = count / int(pageSize)  # 总页数
    # if count != 0:
    #     if count % int(pageSize) != 0:
    #         totalPage = totalPage + 1
    #         # 当页数大于总页数，直接返回
    #     if int(curPage) > totalPage:
    #         return JsonResponse({'code': 2003, "message": '当前页数大于总页数'})
    #     startnum = (int(curPage) - 1) * int(pageSize)  # 计算sql需要的起始索引
    #     endnum = int(pageSize)
    cursor.execute('select s.skill_id,s.skill_name,s.skill_type,f.function_id,f.function_name,t.team_id,t.team_name '
                       'from skill s,`function` f,skillFunction sf,team t,teamfunction tf '
                       'where s.skill_id=sf.skill_id and f.function_id=sf.function_id and t.team_id=tf.team_id and tf.function_id=f.function_id ')
    data2 = cursor.fetchall()
    cursor.close()
    return JsonResponse({'code': 200, 'message': '查询成功', 'data': data2})

#编辑
def updateTeam(request):
    teamId = request.POST['team_id']
    teamComment = request.POST['team_comment']
    teamName = request.POST['team_name']
    try:
        # 空间名是唯一的，查询是否在数据库里存在
        cursor = connection.cursor()
        cursor.execute('select team_id from team where team_name=%s and team_comment=%s', [teamName,teamComment])
        tid = cursor.fetchone()
        if tid:
            return JsonResponse({'code': 2003, 'message': '团队已经存在，请重新输入'})
        cursor.execute('update team set team_name=%s,team_comment=%s where team_id=%s', [teamName,teamComment,teamId])
        cursor.close()
        # 成功的话
        return JsonResponse({'code': 200, 'message': '修改成功'})
    except:
        return JsonResponse({'code': 4001, 'message': '修改失败'})

#删除团队
def deleteTeam(request):
    teamId = request.POST['team_id']
    cursor = connection.cursor()
    cursor.execute('delete from team where team_id=%s', [teamId])
    cursor.close()
    return JsonResponse({'code': 200, 'message': '删除成功'})

#修改职能
def updateFunction(request):
    function_id = request.POST['function_id']
    function_comment = request.POST['function_comment']
    function_name = request.POST['function_name']
    team_name = request.POST['team_name']
    try:
        # 空间名是唯一的，查询是否在数据库里存在
        cursor = connection.cursor()
        cursor.execute('select team_id from team where team_name=%s ', [team_name])
        team_id = cursor.fetchone()

        cursor.execute('select id from teamFunction where function_id=%s and team_id=%s', [function_id,team_id])
        tid = cursor.fetchone()
        if tid:
            return JsonResponse({'code': 2003, 'message': '职能已存在，请重新输入'})
        #职能
        cursor.execute('update `function` set function_name=%s,function_comment=%s where function_id=%s', [function_name,function_comment,function_id])
        #团队职能
        cursor.execute('update teamFunction set team_id=%s where function_id=%s',[team_id, function_id])
        cursor.close()
        # 成功的话
        return JsonResponse({'code': 200, 'message': '修改成功'})
    except:
        return JsonResponse({'code': 4001, 'message': '修改失败'})

#删除职位  删除职位和团队职位表
def deleteFunction(request):
    function_id = request.POST['function_id']
    cursor = connection.cursor()
    #查询有关，有删除
    cursor.execute('select * from `function` f,teamFunction tf where f.function_id=tf.function_id and f.function_id=%s', [function_id])
    tid = cursor.fetchone()
    if tid:
        cursor.execute('delete from `function` where function_id=%s',[function_id])
        cursor.execute('delete from teamFunction  where function_id=%s', [function_id])
        cursor.close()
        return JsonResponse({'code': 200, 'message': '删除成功'})
    else:
        cursor.execute('delete from `function` where function_id=%s',[function_id])
        cursor.close()
        return JsonResponse({'code': 200, 'message': '删除成功'})

def updateSkill(request):
    skill_id = request.POST['skill_id']
    skill_name = request.POST['skill_name']
    skill_type = request.POST['skill_type']
    function_name = request.POST['function_name']
    try:
        # 空间名是唯一的，查询是否在数据库里存在
        cursor = connection.cursor()
        cursor.execute('select function_id from `function` where function_name=%s ', [function_name])
        function_id = cursor.fetchone()

        cursor.execute('select id from skillFunction where skill_id=%s and function_id=%s', [skill_id, function_id])
        tid = cursor.fetchone()
        if tid:
            return JsonResponse({'code': 2003, 'message': '技能已存在，请重新输入'})

        cursor.execute('update skill set skill_name=%s,skill_type=%s where skill_id=%s', [skill_name,skill_type,skill_id])

        cursor.execute('update skillFunction set function_id=%s where skill_id=%s', [function_id, skill_id])
        cursor.close()
        # 成功的话
        return JsonResponse({'code': 200, 'message': '修改成功'})
    except:
        return JsonResponse({'code': 4001, 'message': '修改失败'})

#删除技能 删除技能和职位技能表
def deleteSkill(request):
    skill_id = request.POST['skill_id']
    cursor = connection.cursor()
    cursor.execute('delete from skill where skill_id=%s', [skill_id])
    cursor.execute('delete from skillFunction  where skill_id=%s', [skill_id])
    cursor.close()
    return JsonResponse({'code': 200, 'message': '删除成功'})


#添加权限
def addPermission(request):
        permission_name = request.POST['permission_name']
        try:
            # 查询是否在数据库里存在
            cursor = connection.cursor()
            cursor.execute('select permission_id from Permission where permission_name=%s', [permission_name])
            tid = cursor.fetchone()
            if tid:
                return JsonResponse({'code': 2003, 'message': '权限已存在，请换个名字'})
            # 创建保存点
            save_id = transaction.savepoint()
            # 添加
            cursor.execute('insert into permission(permission_name) values(%s)', [permission_name])
            cursor.close()
            # 成功的话保存
            transaction.savepoint_commit(save_id)
            return JsonResponse({'code': 200, 'message': '添加成功'})
        except:
            # 失败的时候回滚到保存点
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'code': 2001, 'message': '添加失败'})

#权限列表
def getPermissionList(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute('select * from permission ')
    data2 = cursor.fetchall()
    cursor.close()
    return JsonResponse({'code': 200, 'message': '查询成功', 'data': data2})

#修改权限
def updatePermission(request):
    permission_id = request.POST['permission_id']
    permission_name = request.POST['permission_name']
    try:
        # 空间名是唯一的，查询是否在数据库里存在
        cursor = connection.cursor()
        cursor.execute('select permission_id from permission where permission_name=%s', [permission_name])
        tid = cursor.fetchone()
        if tid:
            return JsonResponse({'code': 2003, 'message': '权限已经存在，请重新输入'})
        cursor.execute('update permission set permission_name=%s where permission_id=%s', [permission_name,permission_id])
        cursor.close()
        # 成功的话
        return JsonResponse({'code': 200, 'message': '修改成功'})
    except:
        return JsonResponse({'code': 4001, 'message': '修改失败'})

#删除权限
def deletePermission(request):
    permission_id = request.POST['permission_id']
    cursor = connection.cursor()
    cursor.execute('delete from permission where permission_id=%s', [permission_id])
    cursor.close()
    return JsonResponse({'code': 200, 'message': '删除成功'})

#添加角色
def addRole(request):
        permission_name=request.POST['permission_name']
        role_name = request.POST['role_name']
        try:
            # 查询是否在数据库里存在
            cursor = connection.cursor()
            cursor.execute('select role_id from role where role_name=%s', [role_name])
            tid = cursor.fetchone()
            if tid:
                return JsonResponse({'code': 2003, 'message': '权限已存在，请换个名字'})
            # 创建保存点
            save_id = transaction.savepoint()
            # 查询
            cursor.execute('select permission_id from permission where permission_name=%s', [permission_name])
            permission_id = cursor.fetchone()[0]
            # 添加
            cursor.execute('insert into role(role_name) values(%s)', [role_name])
            # 查询function_id
            cursor.execute('select role_id from role order by role_id desc limit 1')
            role_id = cursor.fetchone()[0]
            cursor.execute('insert into permissionRole(permission_id,role_id) values(%s,%s)', [permission_id,role_id])
            cursor.close()
            # 成功的话保存
            transaction.savepoint_commit(save_id)
            return JsonResponse({'code': 200, 'message': '添加成功'})
        except:
            # 失败的时候回滚到保存点
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'code': 2001, 'message': '添加失败'})

#角色列表
def getRoleList(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill',cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute('select r.role_id,r.role_name,p.permission_name,p.permission_id '
                   'from role r ,permissionRole pr,permission p where r.role_id=pr.role_id and pr.permission_id=p.permission_id  ')
    data2 = cursor.fetchall()
    cursor.close()
    return JsonResponse({'code': 200, 'message': '查询成功', 'data': data2})

#修改角色
def updateRole(request):
    role_id = request.POST['role_id']
    role_name = request.POST['role_name']
    try:
        # 空间名是唯一的，查询是否在数据库里存在
        cursor = connection.cursor()
        cursor.execute('select role_id from role where role_name=%s', [role_name])
        tid = cursor.fetchone()
        if tid:
            return JsonResponse({'code': 2003, 'message': '权限已经存在，请重新输入'})
        cursor.execute('update role set role_name=%s where role_id=%s', [role_name,role_id])
        cursor.close()
        # 成功的话
        return JsonResponse({'code': 200, 'message': '修改成功'})
    except:
        return JsonResponse({'code': 4001, 'message': '修改失败'})

#删除角色 删除权限和权限角色
def deleteRole(request):
    role_id = request.POST['role_id']
    cursor = connection.cursor()
    # 查询有关，有删除
    cursor.execute('select * from role r,permissionRole pr where r.role_id=pr.role_id and r.role_id=%s', [role_id])
    tid = cursor.fetchone()
    if tid:
        cursor.execute('delete from role where role_id=%s', [role_id])
        cursor.execute('delete from permissionRole  where role_id=%s', [role_id])
        cursor.close()
        return JsonResponse({'code': 200, 'message': '删除成功'})
    else:
        cursor.execute('delete from role where role_id=%s', [role_id])
        cursor.close()
        return JsonResponse({'code': 200, 'message': '删除成功'})


# 通过用户名查询用户
def serachUser(request):
    # 获取用户名和协作空间名
    userName = request.POST['name']
    teamName = request.POST['team_name']
    cursor = connection.cursor()
    # 查询用户是否是该协作空间的协作者
    cursor.execute('select u.user_id from user u,team t,team_member tm ' +
                   'where u.user_id=tm.user_id and tm.team_id=t.team_id and u.user_name="' + userName + '" and t.team_name="' + teamName + '"')
    userId = cursor.fetchone()
    if userId:
        cursor.close()
        return JsonResponse({'status': 1002, 'message': '该用户已经添加过了'})
    else:
        # 查询该用户的信息
        cursor.execute('select user_id,user_name,icon from user where user_name="' + userName + '" ')
        result = cursor.fetchone()
        cursor.close()
        if result:
            return JsonResponse({'status': 200, 'message': result})
        else:
            return JsonResponse({'status': 1002, 'message': '用户不存在'})

#给团队添加成员
def addMember(request):
    # 获取用户、空间、角色
    user_id = request.POST['user_id']
    team_id = request.POST['team_id']
    role_id = request.POST['role_id']

    # 判断此登录的用户,只有角色是管理员才有权限添加
    cursor = connection.cursor()
    cursor.execute(
        'select DISTINCT role_name from role r,memeberrole mr,teammemeber tm,user u ,team t where r.role_id=mr.role_id '
        'and mr.team_member_id=tm.team_member_id and t.team_id=tm.team_id and tm.user_id=u.user_id and u.user_id=%s and t.team_id=%s',
        [user_id, team_id])
    result = cursor.fetchone()
    if result[0] == '管理员' :
        try:
            # 创建保存点
            save_id = transaction.savepoint()
            # 把用户添加到协作空间里
            cursor.execute('insert into teammemeber(team_id,user_id) values(%s,%s)', [team_id, user_id])
            # 查询插入的协作空间成员的id
            cursor.execute('select team_member_id from teammemeber order by team_member_id desc limit 1')
            team_id = cursor.fetchone()
            # 把人员与角色绑定
            cursor.execute('insert into memeberrole(team_member_id,role_id) values(%s,%s)', [team_id, role_id])
            # 成功的话保存
            code = 200
            message = '添加成功'
            transaction.savepoint_commit(save_id)
        except:
            # 失败的时候回滚到保存点
            code = 4001
            message = '添加失败'
            transaction.savepoint_rollback(save_id)
        return JsonResponse({'code': code, 'message': message})
    else:
        return JsonResponse({'code': 2002, 'message': '抱歉，您没有权限'})

#显示成员列表
def memberList(request):
    db = MySQLdb.connect(host='172.16.80.156', user='root', passwd='123456', db='teamskill', cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute('select t.team_name,u.name,u.email,r.role_name from team t ,user u ,teamMemeber tm,memeberRole mr,role r '
                   'where tm.team_id=t.team_id and tm.user_id=u.user_id and mr.team_member_id=tm.team_member_id and mr.role_id=r.role_id')
    data2 = cursor.fetchall()
    cursor.close()
    return JsonResponse({'code': 200, 'message': '查询成功', 'data': data2})

#编辑成员
def updateMember(request):
    user_id = request.POST['user_id']
    team_id = request.POST['team_id']
    role_id = request.POST['role_id']
    # 判断此登录的用户,只有角色是管理员才有权限编辑
    cursor = connection.cursor()
    cursor.execute(
        'select DISTINCT role_name from role r,memeberrole mr,teammemeber tm,user u ,team t where r.role_id=mr.role_id '
        'and mr.team_member_id=tm.team_member_id and t.team_id=tm.team_id and tm.user_id=u.user_id and u.user_id=%s and t.team_id=%s',
        [user_id, team_id])
    result = cursor.fetchone()
    if result[0] == '管理员':
        try:
            # 创建保存点
            save_id = transaction.savepoint()
            # 修改
            cursor.execute('insert into teammemeber(team_id,user_id) values(%s,%s)', [team_id, user_id])
            # 查询插入的协作空间成员的id
            cursor.execute('select team_member_id from teammemeber order by team_member_id desc limit 1')
            team_id = cursor.fetchone()
            # 把人员与角色绑定
            cursor.execute('insert into memeberrole(team_member_id,role_id) values(%s,%s)', [team_id, role_id])
            # 成功的话保存
            code = 200
            message = '修改成功'
            transaction.savepoint_commit(save_id)
        except:
            # 失败的时候回滚到保存点
            code = 4001
            message = '修改失败'
            transaction.savepoint_rollback(save_id)
        return JsonResponse({'code': code, 'message': message})
    else:
        return JsonResponse({'code': 2002, 'message': '抱歉，您没有权限'})

#删除成员
def deleteMember(request):
    memRoleId = request.POST.get('memRoleId')  # 成员角色id
    teamName = request.POST['teamName']
    # 获取session里存放的username
    username = request.session.get('username')
    # 判断此登录的用户是否是管理员或者超级管理员，只有角色是管理员才有权限修改
    cursor = connection.cursor()
    cursor.execute(
        'select DISTINCT role_name from role r,member_role mr,team_member tm,user u ,team t where r.role_id=mr.role_id '
        'and mr.team_mem_id=tm.team_mem_id and t.team_id=tm.team_id and tm.user_id=u.user_id and u.user_name=%s and t.team_name=%s',
        [username, teamName])
    result = cursor.fetchone()
    if result[0] == '管理员' or result[0] == '超级管理员':
        # 创建保存点
        saveId = transaction.savepoint()
        try:
            # 移除角色
            cursor.execute(
                'delete tm,mr from team_member tm,member_role mr where tm.team_mem_id=mr.team_mem_id and mr.mem_role_id=' + memRoleId)
            cursor.close()
            # 成功的话保存
            status = 200
            message = '移除成功'
            transaction.savepoint_commit(saveId)
        except:
            # 失败的时候回滚到保存点
            status = 4001
            message = '移除失败'
            transaction.savepoint_rollback(saveId)
        return JsonResponse({'status': status, 'message': message})
    else:
        return JsonResponse({'status': 2002, 'message': '抱歉，您没有权限'})

# 查询成员、技能
def search(request):
    cursor = connection.cursor()
    searchCondition = request.POST.get("searchCondition")  # 获取查询条件
    searchedFiles = []
    files = {}
    # 获取username
    username = request.session['username']
    # 查文件
    cursor.execute(
        "select file_id from file where file_name like '%" + searchCondition + "%'")
    selFileIds = cursor.fetchall()
    return JsonResponse({'code': 2002, 'message': '抱歉，您没有权限'})










#登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/home/')
            request.session["uid"] = user.id
            return response
        else:
            return render_to_response('login.html')
    else:
        # return HttpResponseRedirect('/login/')
        return render_to_response('login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('login.html')



