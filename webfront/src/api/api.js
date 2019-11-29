import axios from './axioses'
let base = 'http://localhost:8081';
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'



export const getUserList = params => { return axios.get(`${base}/user/list`, { params: params }); };

export const getUserListPage = params => { return axios.get(`${base}/user/listpage`, { params: params }); };

export const removeUser = params => { return axios.get(`${base}/user/remove`, { params: params }); };

export const batchRemoveUser = params => { return axios.get(`${base}/user/batchremove`, { params: params }); };

export const editUser = params => { return axios.get(`${base}/user/edit`, { params: params }); };

export const addUser = params => { return axios.get(`${base}/user/add`, { params: params }); };


//登录
export const requestLogin = params => { return axios.post(`${base}/api/userLogin/`, params).then(res => res); };
//注册发邮件
export const postEmail = params => { return axios.get(`${base}/api/postEmail/`, params).then(res => res); };
//注册
export const registerUser = params => { return axios.post(`${base}/api/registerUser/`, params).then(res => res); };



export const valiName = params => { return axios.get(`${base}/api/valiName/?name=`+params).then(res => res); };
export const valiEmail = params => { return axios.get(`${base}/api/valiEmail/?email=`, +params).then(res => res); };
export const valiEmailcode = params => { return axios.post(`${base}/api/valiEmailcode/`, params).then(res => res); };



//查询职能名称
export const getFunctionName = params => { return axios.post(`${base}/api/getFunctionName/`, params).then(res => res); };

//查询团队名称
export const getTeamName = params => { return axios.post(`${base}/api/getTeamName/`, params).then(res => res); };

//查询权限名称
export const getPermissionName = params => { return axios.post(`${base}/api/getPermissionName/`, params).then(res => res); };

//查询成员名称
export const getMemberName = params => { return axios.post(`${base}/api/getMemberName/`, params).then(res => res); };

//查询角色名称
export const getRoleName = params => { return axios.post(`${base}/api/getRoleName/`, params).then(res => res); };

//该成员加入的团队
export const getAllTeam = params => { return axios.post(`${base}/api/getAllTeam/`, params).then(res => res); };



//团队列表
export const getTeamList = params => { return axios.get(`${base}/api/getTeamList/`, params).then(res => res); };

//添加团队
export const addTeam = params => { return axios.post(`${base}/api/addTeam/`, params).then(res => res); };

//职能列表
export const getFunctionList = params => { return axios.get(`${base}/api/getFunctionList/`, params).then(res => res); };

//添加职能
export const addFunction = params => { return axios.post(`${base}/api/addFunction/`, params).then(res => res); };

//技能列表
export const getSkillList = params => { return axios.get(`${base}/api/getSkillList/`, params).then(res => res); };

//添加技能
export const addSkill = params => { return axios.post(`${base}/api/addSkill/`, params).then(res => res); };

//团队技术栈
export const showTeamSkill = params => { return axios.get(`${base}/api/showTeamSkill/`, params).then(res => res); };



//编辑团队
export const updateTeam = params => { return axios.post(`${base}/api/updateTeam/`, params).then(res => res); };

//删除团队
export const deleteTeam = params => { return axios.post(`${base}/api/deleteTeam/`, params).then(res => res); };

//编辑职能
export const updateFunction = params => { return axios.post(`${base}/api/updateFunction/`, params).then(res => res); };

//删除职能
export const deleteFunction = params => { return axios.post(`${base}/api/deleteFunction/`, params).then(res => res); };

//编辑技能
export const updateSkill = params => { return axios.post(`${base}/api/updateSkill/`, params).then(res => res); };

//删除技能
export const deleteSkill = params => { return axios.post(`${base}/api/deleteSkill/`, params).then(res => res); };


//权限列表
export const getPermissionList = params => { return axios.get(`${base}/api/getPermissionList/`, params).then(res => res); };

//添加权限
export const addPermission = params => { return axios.post(`${base}/api/addPermission/`, params).then(res => res); };

//编辑权限
export const updatePermission = params => { return axios.post(`${base}/api/updatePermission/`, params).then(res => res); };

//删除权限
export const deletePermission = params => { return axios.post(`${base}/api/deletePermission/`, params).then(res => res); };



//角色列表
export const getRoleList = params => { return axios.get(`${base}/api/getRoleList/`, params).then(res => res); };

//添加角色
export const addRole = params => { return axios.post(`${base}/api/addRole/`, params).then(res => res); };

//编辑角色
export const updateRole = params => { return axios.post(`${base}/api/updateRole/`, params).then(res => res); };

//删除角色
export const deleteRole = params => { return axios.post(`${base}/api/deleteRole/`, params).then(res => res); };



//添加角色权限
export const addRolePer = params => { return axios.post(`${base}/api/addRolePer/`, params).then(res => res); };

//角色权限列表
export const getRolePerList = params => { return axios.get(`${base}/api/getRolePerList/`, params).then(res => res); };

//编辑角色权限
export const updateRolePer = params => { return axios.post(`${base}/api/updateRolePer/`, params).then(res => res); };

//删除角色权限
export const deleteRolePer = params => { return axios.post(`${base}/api/deleteRolePer/`, params).then(res => res); };



//团队成员列表
export const memberList = params => { return axios.get(`${base}/api/memberList/`, params).then(res => res); };

//添加团队成员
export const addMember = params => { return axios.post(`${base}/api/addMember/`, params).then(res => res); };

//编辑团队成员
export const updateMember = params => { return axios.post(`${base}/api/updateMember/`, params).then(res => res); };

//删除团队成员
export const deleteMember = params => { return axios.post(`${base}/api/deleteMember/`, params).then(res => res); };

//查询普通成员
export const serachTeamUser = params => { return axios.post(`${base}/api/serachTeamUser/`, params).then(res => res); };

//查询管理员
export const serachTeamAdmin = params => { return axios.post(`${base}/api/serachTeamAdmin/`, params).then(res => res); };

//通过用户名查询用户
export const serachUser = params => { return axios.post(`${base}/api/serachUser/`, params).then(res => res); };


