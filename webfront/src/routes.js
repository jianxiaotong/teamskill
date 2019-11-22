import Login from './views/Login.vue'
import NotFound from './views/404.vue'
import Home from './views/Home.vue'
import Main from './views/Main.vue'
import ShowTeamSkill from './views/nav1/showTeamSkill.vue'
import AddTeam from './views/nav1/addTeam.vue'
import TeamList from './views/nav1/teamList.vue'
import Function from './views/nav1/function.vue'
import Skill from './views/nav1/skill.vue'
import member from './views/nav2/member.vue'
import Page5 from './views/nav2/Page5.vue'
import demo from './views/nav2/demo.vue'
import permissionList from './views/nav3/permissionList.vue'
import role from './views/nav3/roleList.vue'
import echarts from './views/charts/echarts.vue'
import teamskill from './views/charts/teamskill.vue'
let routes = [
    {
        path: '/login',
        component: Login,
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
            { path: '/addTeam', component: AddTeam, name: '添加团队' },
            { path: '/teamList', component: TeamList, name: '团队列表' },
			{ path: '/function', component: Function, name: '职能列表' },
			{ path: '/skill', component: Skill, name: '技能列表' },
        ]
    },
    {
        path: '/',
        component: Home,
        name: '团队管理',
        iconCls: 'fa fa-id-card-o',
        children: [
            { path: '/member', component: member, name: '成员列表' },
   //          { path: '/page5', component: Page5, name: '页面5' },
			// { path: '/demo', component: demo, name: 'demo4' },
        ]
    },
	{
	    path: '/',
	    component: Home,
	    name: '权限管理',
	    iconCls: 'fa fa-address-card',
	    //leaf: true,//只有一个节点
	    children: [
	        { path: '/permission', component: permissionList, name: '权限列表' },
	        { path: '/role', component: role, name: '角色列表' }
	    ]
	},
	{
	    path: '/',
	    component: Home,
	    name: '个人中心',
	    iconCls: 'fa fa-address-card',
	    children: [
	       { path: '/echarts', component: echarts, name: 'echarts' },
	       { path: '/teamskill', component: teamskill, name: 'teamskill' }
	    ]
	},
   
    {
        path: '/',
        component: Home,
        name: 'Charts',
        iconCls: 'fa fa-bar-chart',
        children: [
            { path: '/echarts', component: echarts, name: 'echarts' },
			{ path: '/teamskill', component: teamskill, name: 'teamskill' }
        ]
    },
    {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];

export default routes;