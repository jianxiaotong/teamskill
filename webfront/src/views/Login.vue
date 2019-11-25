<template>
  <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-position="left" label-width="0px" class="demo-ruleForm login-container">
    <h3 class="title">系统登录</h3>
    <el-form-item prop="email">
	  
      <el-input type="email" v-model="ruleForm2.email" auto-complete="off" placeholder="邮箱"></el-input>
    </el-form-item>
    <el-form-item prop="password">
		
      <el-input type="password" v-model="ruleForm2.password" auto-complete="off" placeholder="密码"></el-input>
    </el-form-item>
    <el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox>
    <el-form-item style="width:100%;">
      <el-button type="primary" style="width:100%;" @click.native.prevent="handleSubmit2" :loading="logining">登录</el-button>
      <!--<el-button @click.native.prevent="handleReset2">重置</el-button>-->
    </el-form-item>
  </el-form>
</template>

<script>
  import { requestLogin } from '../api/api';
  //import NProgress from 'nprogress'
  export default {
    data() {
		//邮箱校验
		var validateEmail = (rule, value, callback) => {
		        if (value === '') {
		          callback(new Error('请正确填写邮箱'));
		        } else {
		          if (value !== '') { 
		            var reg=/^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
		            if(!reg.test(value)){
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
			          } else if(value.length < 6){
			            callback(new Error('密码长度最小6位'));
			          }else{
			            callback();
			          }
			        };
      return {
        logining: false,
        ruleForm2: {
		  account: '',
		  password: '',					
        },
        rules2: {
          account: [
            { required: true,
			 message: '请输入邮箱地址', 
			 trigger: 'blur',
			 },
			{
				validator: validateEmail,
				trigger: 'blur'
			}
            //{ validator: validaePass }
          ],
          password: [
            { 
			required: true, 
			message: '请输入密码', 
			trigger: 'blur' ,
			},
			{
				validator: validatePass,
				trigger: 'blur'
			},
			{
				max: 20,
				message: '6-20个字符',
				trigger: 'blur'
			},
			
            //{ validator: validaePass2 }
          ]
        },
        checked: true
      };
    },
    methods: {
      handleReset2() {
        this.$refs.ruleForm2.resetFields();
      },
      handleSubmit2(ev) {
        var _this = this;
        this.$refs.ruleForm2.validate((valid) => {
          if (valid) {
            //_this.$router.replace('/table');
            this.logining = true;
            //NProgress.start();
            var loginParams = { username: this.ruleForm2.account, password: this.ruleForm2.password };
            requestLogin(loginParams).then(data => {
              this.logining = false;
              console.log(data);
              //NProgress.done();
              let { msg, code, user } = data;
              if (code !== 200) {
                this.$message({
                  message: msg,
                  type: 'error'
                });
              } else {
                sessionStorage.setItem('user', JSON.stringify(user));
                this.$router.push({ path: '/table' });
              }
            });
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      }
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
  }
</style>