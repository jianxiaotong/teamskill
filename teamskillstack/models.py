from django.db import models

# Create your models here.

#团队
class Team(models.Model):
    team_id=models.AutoField(primary_key=True)
    team_name=models.CharField(u'团队名称', max_length=32)
    team_comment=models.TextField(u'简介',null=True,blank=True)
    team_creator = models.IntegerField(u'团队创建者',null=True, blank=True)
    team_create = models.DateTimeField(u'创建时间',null=True, blank=True)

    class Meta:
        db_table = 'team'

#职能 管理、测试、前端、后端、运维
class Function(models.Model):
    function_id = models.AutoField(primary_key=True)
    function_name=models.CharField(u'职能名称', max_length=32)
    function_comment = models.TextField(u'介绍', null=True, blank=True)

    class Meta:
        db_table = 'function'

#技能
class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name=models.CharField(u'技能名称', max_length=32,null=True,blank=True)
    skill_type = models.CharField(u'技能类型', max_length=32,null=True,blank=True)
    class Meta:
        db_table = 'skill'

#一个团队多个职能
class TeamFunction(models.Model):
    id = models.AutoField(primary_key=True)
    team_id = models.IntegerField(u'团队id')
    function_id = models.IntegerField(u'职能id')
    class Meta:
        db_table = 'teamFunction'

#一个职能多个技能
class SkillFunction(models.Model):
    id = models.AutoField(primary_key=True)
    skill_id = models.IntegerField(u'技能id')
    function_id = models.IntegerField(u'职能id')
    class Meta:
        db_table = 'skillFunction'

#用户
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name=models.CharField(u'用户名', max_length=100,unique=True,null=True, blank=True)
    email = models.EmailField(u'邮箱',unique=True,null=True, blank=True)
    password = models.CharField(u'密码', max_length=100)
    icon = models.CharField(u'头像', max_length=150, null=True, blank=True)
    create_time =  models.DateTimeField(u'创建时间',null=True, blank=True)
    class Meta:
        db_table = 'user'

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(u'角色名称',max_length=20)

    class Meta:
        db_table = 'role'

class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(u'权限名称',max_length=50)

    class Meta:
        db_table = 'permission'

class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(u'用户id')
    role_id = models.IntegerField(u'角色id')

    class Meta:
        db_table = 'userRole'

class PermissionRole(models.Model):
    per_role_id = models.AutoField(primary_key=True)
    permission_id = models.IntegerField(u'权限id')
    role_id = models.IntegerField(u'角色id')

    class Meta:
        db_table = 'permissionRole'

#团队有哪些成员
class TeamMemeber(models.Model):
    team_member_id = models.AutoField(primary_key=True)
    team_id = models.IntegerField(u'团队id')
    user_id = models.IntegerField(u'用户id')

    class Meta:
        db_table = 'teamMemeber'

#团队成员的角色
class MemeberRole(models.Model):
    member_role_id = models.AutoField(primary_key=True)
    team_member_id = models.IntegerField(u'团队成员id')
    role_id = models.IntegerField(u'角色id')

    class Meta:
        db_table = 'memeberRole'




