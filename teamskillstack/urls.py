from django.urls import path
from teamskillstack import views,login


urlpatterns = [
    #获取名称
    path('getFunctionName/', views.getFunctionName),
    path('getTeamName/', views.getTeamName),
    path('getPermissionName/', views.getPermissionName),
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


    #搜索
    path('search/', views.search),

    #登录和注册
    # path('index/', views.index),
    # path('login/', views.login),
    # path('register/', views.register),
    # path('loginout/', views.loginout),

]
