<template>
	<el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-position="left" label-width="0px" class="demo-ruleForm login-container">
		<h3 class="title">登录</h3>
		<el-form-item prop="email">

			<el-input type="email" v-model="ruleForm2.email" auto-complete="off" placeholder="邮箱"></el-input>
		</el-form-item>
		<el-form-item prop="password">

			<el-input type="password" v-model="ruleForm2.password" auto-complete="off" placeholder="密码"></el-input>
		</el-form-item>
		<el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox>
		<el-form-item style="width:100%;">
			<el-button type="primary" style="width:100%;" @click="handleSubmit2" :loading="logining">登录</el-button>
			<!-- <el-button @click.native.prevent="handleReset2">重置</el-button> -->
			<p class="login" @click="gotoregister">没有账号？前去注册</p>
		</el-form-item>
	</el-form>
</template>

<script>
	import {
		requestLogin
	} from '../api/api';
	//import NProgress from 'nprogress'
	export default {
		data() {
			//邮箱校验
			var validateEmail = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请正确填写邮箱'));
				} else {
					if (value !== '') {
						var reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
						if (!reg.test(value)) {
							callback(new Error('请输入有效的邮箱'));
						}
					}
					callback();
				}
			};
			//密码
			var validatePass = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请设置正确格式的密码'));
				} else if (value.length < 6) {
					callback(new Error('密码长度最小6位'));
				} else {
					callback();
				}
			};
			return {
				logining: false,
				ruleForm2: {
					email: 'jianxiaotong1@126.com',
					password: '123456',
				},
				rules2: {
					email: [{
							required: true,
							message: '请输入邮箱地址',
							trigger: 'blur',
						},
						{
							validator: validateEmail,
							trigger: 'blur'
						}
						//{ validator: validaePass }
					],
					password: [{
							required: true,
							message: '请输入密码',
							trigger: 'blur',
						},
						{
							validator: validatePass,
							trigger: 'blur'
						},
						{
							max: 12,
							message: '3-12个字符',
							trigger: 'blur'
						},

						//{ validator: validaePass2 }
					]
				},
				checked: true
			};
		},
		methods: {
			// 重置表单
			resetForm() {
				this.$refs.ruleForm2.resetFields();
			},
			// handleReset2() {
			// 	this.$refs.ruleForm2.resetFields();
			// },
			handleSubmit2() {
				this.$refs.ruleForm2.validate((valia) => {
					if (valia) {
						requestLogin(this.ruleForm2).then((res) => {
							console.log(res)
							if (res.code == 200) {
								this.$message.success(res.message);							
								this.resetForm();
								this.$router.push({path:"/"});
								window.localStorage.setItem('useremail', res.useremail)
								
							} else {
								this.$message.error(res.message);
								
							}
						})
					} else {
						return false;
					}
				});
			},
			gotoregister() {
				this.$router.push({
					path: "/register"
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
	.login-container {
		/*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
		-webkit-border-radius: 5px;
		border-radius: 5px;
		-moz-border-radius: 5px;
		background-clip: padding-box;
		margin: 180px auto;
		width: 350px;
		padding: 35px 35px 15px 35px;
		background: #fff;
		border: 1px solid #eaeaea;
		box-shadow: 0 0 25px #cac6c6;

		.title {
			margin: 0px auto 40px auto;
			text-align: center;
			color: #505458;
		}

		.remember {
			margin: 0px 0px 35px 0px;
		}

		.login {
			margin-top: 10px;
			font-size: 14px;
			line-height: 22px;
			color: #1ab2ff;
			cursor: pointer;
			text-align: left;
			text-indent: 8px;
			width: 160px;
		}

		.login:hover {
			color: blue;
		}

	}
</style>
