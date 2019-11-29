<template>
	<div>
		<div class="register-wrapper">
			<div id="register">
				<p class="title">注册</p>
				<el-form :model="form" status-icon :rules="rules2" ref="form" label-width="0" class="demo-ruleForm">
					<el-form-item prop="name">
						<el-input type="text" v-model="form.name" @blur='blurname' auto-complete="off" placeholder="请输入用户名"></el-input>
					</el-form-item>
					<el-form-item prop="email">
						<el-input type="email" v-model="form.email" @blur='checkEmail' auto-complete="off" placeholder="请输入邮箱"></el-input>
					</el-form-item>
					<el-form-item prop="smscode" class="code">
						<el-input v-model="form.smscode" @blur='blurcode' placeholder="验证码" style="width: 174px;"></el-input>
						<el-button type="primary" :disabled='isDisabled' @click="sendCode">{{buttonText}}</el-button>
					</el-form-item>
					<el-form-item prop="pass">
						<el-input type="password" v-model="form.pass" auto-complete="off" placeholder="输入密码"></el-input>
					</el-form-item>
					<el-form-item prop="checkPass">
						<el-input type="password" v-model="form.checkPass" auto-complete="off" placeholder="确认密码"></el-input>
					</el-form-item>
					<el-form-item>
						<el-button type="primary" @click="submitForm" style="width:100%;">注册</el-button>
						<p class="login" @click="gotoLogin">已有账号？立即登录</p>
					</el-form-item>
				</el-form>
			</div>
		</div>
	</div>
</template>

<script>
	import {
		postEmail,
		registerUser,
		valiName,
		valiEmail,
		valiEmailcode
	} from '../api/api';
	export default {
		name: "Register",
		data() {
			// <!--验证邮箱是否合法-->
			let validateEmail = (rule, value, callback) => {
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
			}
			//  <!--验证码是否为空-->
			let checkSmscode = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请输入验证码'))
				} else {
					callback()
				}
			}
			// <!--验证密码-->
			let validatePass = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请设置正确格式的密码'));
				} else if (value.length < 6) {
					callback(new Error('密码长度最小6位'));
				} else {
					if (this.form.checkPass !== "") {
						this.$refs.form.validateField("checkPass");
					}
					callback()
				}
			}
			// <!--二次验证密码-->
			let validatePass2 = (rule, value, callback) => {
				if (value === "") {
					callback(new Error("请再次输入密码"));
				} else if (value !== this.form.pass) {
					callback(new Error("两次输入密码不一致!"));
				} else {
					callback();
				}
			};
			return {
				form: {
					name: "",
					email: "",
					pass: "",
					checkPass: "",
					smscode: ""
				},
				rules2: {
					name: [{
						required: true,
						message: '请输入用户名',
						trigger: 'blur',
					}, {
						min: 3,
						max: 12,
						message: '长度在 3 到 12 个字符'
					}],
					pass: [{
						required: true,
						message: '请输入密码',
						trigger: 'blur'
					}, {

						validator: validatePass,
						trigger: 'change'
					}],

					checkPass: [{
						required: true,
						message: '请输入密码',
						trigger: 'blur',
					}, {
						required: true,
						validator: validatePass2,
						trigger: 'change'
					}],
					email: [{
						required: true,
						message: '请输入邮箱地址',
						trigger: 'blur',
					}, {
						required: true,
						validator: validateEmail,
						trigger: 'change'
					}],
					smscode: [{
						required: true,
						message: '请输入验证码',
						trigger: 'blur',
					}, {
						required: true,
						validator: checkSmscode,
						trigger: 'change'
					}],
				},
				buttonText: '发送验证码',
				isDisabled: false, // 是否禁止点击发送验证码按钮
				flag: true
			}
		},
		methods: {
			//名字失去焦点
			blurname(){
				name=this.form.name
				console.log(name)
				valiName(name).then((res) => {
					if (res.code == 200) {
						this.$message.success(res.message);
					} else {
						this.resetForm();
						this.$message.error(res.message);
					}
				})
			},
			//邮箱失去焦点
			checkEmail(){
				console.log('shlsjdkfj')
				email=this.form.email
				console.log(email)
				valiEmail(email).then((res) => {
					if (res.code == 200) {
						this.$message.success(res.message);
					} else {
						this.resetForm();
						this.$message.error(res.message);
					}
				})
			},
			//验证码失去焦点
			blurcode(){
				email=this.form.email,
				code=this.form.smscode,
				valiEmailcode(email,code).then((res) => {
					if (res.code == 200) {
						this.resetForm();
						this.$message.success(res.message);
					} else {
						this.$message.error(res.message);
					}
				})
			},
			// <!--发送验证码-->
			sendCode() {
				let email = this.form.email
				console.log(email)
				this.$http.get("http://localhost:8081/api/postEmail/?email=" + email)
					.then(function(response) {
						console.log(response)
						if (response.code == 200) {
							console.log(response.message);
						} else {
							console.log(response.message);
						}
					})
			},
			// 重置表单
			resetForm() {
				this.$refs.form.resetFields();
			},
			// <!--提交注册-->
			submitForm() {
				this.$refs.form.validate((valia) => {
					if (valia) {
						registerUser(this.form).then((res) => {
							if (res.code == 200) {
								this.resetForm();
								this.$message.success(res.message);
							} else {
								this.$message.error(res.message);
							}
						})
						/* .catch((res) => {
												this.$message.error(res.message);
											}) */
					} else {
						console.log('error submit!!');
						return false;
					}
				});
			},
			// <!--进入登录页-->
			gotoLogin() {
				this.$router.push({
					path: "/login"
				});
			},
		}
	};
</script>

<style scoped>
	.loading-wrapper {
		position: fixed;
		top: 0;
		right: 0;
		left: 0;
		bottom: 0;
		background: #aedff8;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.register-wrapper img {
		position: absolute;
		z-index: 1;
	}

	.register-wrapper {
		position: fixed;
		top: 0;
		right: 0;
		left: 0;
		bottom: 0;
	}

	#register {
		max-width: 340px;
		margin: 60px auto;
		background: #fff;
		padding: 20px 40px;
		border-radius: 10px;
		position: relative;
		z-index: 9;
	}

	.title {
		font-size: 26px;
		line-height: 50px;
		font-weight: bold;
		margin: 10px;
		text-align: center;
	}

	.el-form-item {
		text-align: center;
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
		color: #2c2fd6;
	}

	.code>>>.el-form-item__content {
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.code button {
		margin-left: 20px;
		width: 140px;
		text-align: center;
	}

	.el-button--primary:focus {
		background: #409EFF;
		border-color: #409EFF;
		color: #fff;
	}
</style>
