from django.urls import path
from teamskillstack import views,login


urlpatterns = [
    #角色权限
    path('getRolePer/',views.getRolePer),
    #获取名称
    path('getFunctionName/', views.getFunctionName),
    path('getTeamName/', views.getTeamName),
    path('getPermissionName/', views.getPermissionName),
    path('getRoleName/', views.getRoleName),

    #团队成员
    path('serachTeamUser/', views.serachTeamUser),
    path('serachTeamAdmin/', views.serachTeamAdmin),
    path('serachUser/', views.serachUser),



    #添加和列表
    path('addTeam/', views.addTeam),
    path('getTeamList/', views.getTeamList),
    path('addFunction/', views.addFunction),
    path('getFunctionList/', views.getFunctionList),
    path('addSkill/', views.addSkill),
    path('getSkillList/', views.getSkillList),
    path('showTeamSkill/', views.showTeamSkill),
    path('memberList/', views.memberList),
    path('addMember/', views.addMember),
    path('getPermissionList/', views.getPermissionList),
    path('addPermission/', views.addPermission),
    path('getRoleList/', views.getRoleList),
    path('addRole/', views.addRole),
    path('addRolePer/', views.addRolePer),
    path('getRolePerList/', views.getRolePerList),




    #修改和删除
    path('updateTeam/', views.updateTeam),
    path('deleteTeam/', views.deleteTeam),
    path('updateFunction/', views.updateFunction),
    path('deleteFunction/', views.deleteFunction),
    path('updateSkill/', views.updateSkill),
    path('deleteSkill/', views.deleteSkill),
    path('updateMember/', views.updateMember),
    path('deleteMember/', views.deleteMember),
    path('updatePermission/', views.updatePermission),
    path('deletePermission/', views.deletePermission),
    path('updateRole/', views.updateRole),
    path('deleteRole/', views.deleteRole),
    path('updateRolePer/', views.updateRolePer),
    path('deleteRolePer/', views.deleteRolePer),


    #搜索


    #登录和注册
    # path('index/', views.index),
    # path('login/', views.login),
    # path('register/', views.register),
    # path('loginout/', views.loginout),

]
