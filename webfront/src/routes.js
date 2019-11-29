import Login from './views/Login.vue'
import Register from './views/Register.vue'
import NotFound from './views/404.vue'
import Home from './views/Home.vue'
import Main from './views/Main.vue'
import ShowTeamSkill from './views/nav1/showTeamSkill.vue'
import AddTeam from './views/nav1/addTeam.vue'
import TeamList from './views/nav1/teamList.vue'
import Function from './views/nav1/function.vue'
import Skill from './views/nav1/skill.vue'
import member from './views/nav2/member.vue'
import memberTeam from './views/nav2/memberTeam.vue'
import permissionList from './views/nav3/permissionList.vue'
import role from './views/nav3/roleList.vue'
import rolePerList from './views/nav3/rolePerList.vue'
import echarts from './views/charts/echarts.vue'
import teamskill from './views/charts/teamskill.vue'
import rolePer from './views/charts/rolePer.vue'
let routes = [
    {
        path: '/login',
        component: Login,
        name: '',
        hidden: true
    },
	{
	    path: '/register',
	    component: Register,
	    name: '',
	    hidden: true
	},
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true
    },
    //{ path: '/main', component: Main },
    {
        path: '/',
        component: Home,
        name: '团队技能',
        iconCls: 'el-icon-monitor',//图标样式class
        children: [
            { path: '/main', component: Main, name: '主页', hidden: true },
            { path: '/showTeamSkill', component: ShowTeamSkill, name: '团队技术栈' },
            //{ path: '/addTeam', component: AddTeam, name: '添加团队' },
            { path: '/teamList', component: TeamList, name: '团队列表' },
			{ path: '/function', component: Function, name: '职能列表' },
			{ path: '/skill', component: Skill, name: '技能列表' },
        ]
    },
    {
        path: '/',
        component: Home,
        name: '团队管理',
        iconCls: 'icon-userTeam',
        children: [
            { path: '/member', component: member, name: '成员列表' },
            { path: '/memberTeam', component: memberTeam, name: '所在团队' },
			// { path: '/demo', component: demo, name: 'demo4' },
        ]
    },
	{
	    path: '/',
	    component: Home,
	    name: '权限管理',
	    iconCls: 'icon-userquanxianguanli',
	    //leaf: true,//只有一个节点
	    children: [
	        { path: '/permission', component: permissionList, name: '权限列表' },
	        { path: '/role', component: role, name: '角色列表' },
			{ path: '/roleper', component: rolePerList, name: '角色权限' },
	    ]
	},
	{
	    path: '/',
	    component: Home,
	    name: '个人中心',
	    iconCls: 'icon-usergerenzhongxin',
	    children: [
	       { path: '/echarts', component: echarts, name: '基本信息' },
	       { path: '/teamskill', component: teamskill, name: '修改密码' }
	    ]
	},
   
    {
        path: '/',
        component: Home,
        name: 'Charts  ',
        iconCls: 'icon-usertubiao',
        children: [
            { path: '/echarts', component: echarts, name: 'echarts' },
			{ path: '/teamskill', component: teamskill, name: '技术栈' },
			{ path: '/rpcharts', component: rolePer, name: '角色权限' }
        ]
    },
    {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];

export default routes;