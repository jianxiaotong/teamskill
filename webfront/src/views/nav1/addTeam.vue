<template>
	<el-form ref="form" :model="form" :rules="rules" label-width="80px" style="margin:20px;width:60%;min-width:600px;">
		<el-form-item label="团队名称" prop="teamName">
			<el-input v-model.trim="form.teamName" placeholder="请输入团队名称" clearable></el-input>
		</el-form-item>
		<el-form-item label="团队简介" prop="teamComment">
			<el-input v-model.trim="form.teamComment" placeholder="请输入团队简介" clearable></el-input>
		</el-form-item>
		<el-form-item>
			<el-button type="primary" @click="submitForm">立即添加</el-button>
			<el-button @click="resetForm">重置</el-button>
		</el-form-item>
	</el-form>
</template>

<script>
	import {
		addTeam,
	} from '../../api/api';
	export default {
		data() {
			return {
				form: {
					teamName: '',
					teamComment: '',
				},
				rules: {
					teamName: [{
							required: true,
							message: '请输入团队名称',
							trigger: 'blur'
						},
					],
					teamComment: [{
							required: false,
							message: '请输入团队简介',
							trigger: 'blur'
						},
					],
				},
			}
		},
		methods: {
			// 添加环境 
			submitForm() {
				this.$refs.form.validate((valia) => {
					if (valia) {
						addTeam(this.form).then((res) => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.resetForm();
							}else{
								this.$message.error(res.message);
							}
						})
					} else {
						console.log('error submit!!');
						return false;
					}
				});
			},
			// 重置表单 
			resetForm() {
				this.$refs.form.resetFields();
			},
		},
	}
</script>

<style>
	.img {
		width: 1.25rem;
		height: 1.25rem;
		vertical-align: middle;
	}

	.span {
		margin-left: 10px;
		vertical-align: middle;
	}
</style>
