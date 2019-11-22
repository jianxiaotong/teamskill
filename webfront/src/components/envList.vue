<template>
	<section>
		<!--工具条-->
		<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-button type="primary" @click="dialogVisible = true">添加</el-button>
		</el-col>
		
		<!--列表-->
		<el-table :data="list.slice((page-1)*size,page*size)" highlight-current-row v-loading="loading" style="width: 100%;">
			<el-table-column type="index" label="序号" align="center" sortable>
			</el-table-column>
			<el-table-column prop="os" label="操作系统" align="center">
				<template slot-scope="scope">
					<img src="../../assets/Windows.png" class="img" />
					<span style="margin-left: 10px">{{ scope.row.os }}</span>
				</template>
			</el-table-column>
			<el-table-column prop="ip" label="IP地址" align="center">
			</el-table-column>
			<el-table-column prop="name" label="系统用户" align="center">
			</el-table-column>
			<el-table-column prop="password" label="密码" align="center">
			</el-table-column>
			<el-table-column prop="state" label="状态" align="center">
				<template slot-scope="scope">
					<i v-if="scope.row.state == 1" class="el-icon-video-pause" title="启动中"></i>
					<i v-else class="el-icon-video-play" title="未启动"></i>
				</template>
			</el-table-column>
		</el-table>
		
		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="size" :total="total" style="float:right;">
			</el-pagination>
		</el-col>
		
		<!-- 添加弹出窗 -->
		<el-dialog title="添加环境" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
			<el-form ref="form" :model="form" :rules="rules" label-width="80px" style="margin:20px;width:60%;min-width:600px;">
				<el-form-item label="IP地址" prop="ip">
					<el-input v-model.trim="form.ip" placeholder="请输入IP地址" clearable></el-input>
				</el-form-item>
				<el-form-item label="操作系统" prop="os">
					<el-select v-model="form.os" placeholder="请选择操作系统" clearable>
						<el-option label="Windows 10" value="Windows 10">
							<img src="../../assets/Windows.png" class="img" />
							<span class="span">Windows 10</span>
						</el-option>
						<el-option label="Windows 8.1" value="Windows 8.1" disabled>
							<img src="../../assets/Windows.png" class="img" />
							<span class="span">Windows 8.1</span>
						</el-option>
						<el-option label="Windows 8" value="Windows 8" disabled>
							<img src="../../assets/Windows.png" class="img" />
							<span class="span">Windows 8</span>
						</el-option>
						<el-option label="Windows 7" value="Windows 7" disabled>
							<img src="../../assets/Windows.png" class="img" />
							<span class="span">Windows 7</span>
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item label="登录用户" prop="name">
					<el-input v-model.trim="form.name" placeholder="请输入登录用户" clearable></el-input>
				</el-form-item>
				<el-form-item label="登录密码" prop="password">
					<el-input type="password" v-model.trim="form.password" placeholder="请输入登录密码" show-password></el-input>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="submitForm">添加</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>
	</section>
</template>
<script>
	import {
		getEnvList,
		addEnv,
	} from '../../api/api';
	export default {
		data() {
			var validcodeip = (rule, value, callback) => {
				const reg =
					/^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
				if (reg.test(value)) {
					callback();
				} else {
					return callback(new Error('输入格式不合法！'));
				}
			};
			return {
				loading: false,
				status: '',
				list: [],
				dialogVisible: false,
				page: 1,
				total: 0,
				size:10,
				form: {
					ip: '',
					os: '',
					name: '',
					password: '',
				},
				options: [{
						value: 'Chrome',
						label: 'Chrome',
						children: [{
							value: '77',
							label: '77',
						}, {
							value: '76',
							label: '76',
						}]
					},
					{
						value: 'FireFox',
						label: 'FireFox',
						disabled: 'true',
						children: [{
							value: '69',
							label: '69',
						}, {
							value: '68',
							label: '68',
						}]
					}
				],
				rules: {
					ip: [{
							required: true,
							message: '请输入IP地址',
							trigger: 'blur'
						},
						{
							validator: validcodeip,
							trigger: 'blur'
						}
					],
					os: [{
						required: true,
						message: '请选择操作系统',
						trigger: 'change'
					}],
					name: [{
							required: true,
							message: '请输入登录用户',
							trigger: 'blur'
						},
						{
							max: 20,
							message: '最多 20 个字符',
							trigger: 'blur'
						}
					],
					password: [{
						required: true,
						message: '请输入登录密码',
						trigger: 'blur'
					}, ],
				},
			}
		},
		methods: {
			//修改页码，查询数据
			handleCurrentChange(val) {
				this.page = val;
				this.getEnv();
			},
			//获取环境列表
			getEnv: function() {
				//分页传参
				let para = {
					page: this.page,
					size: this.size,
				};
				this.loading = true;
				getEnvList(para).then((res) => {
					this.list = res.data;
					this.total= res.data.length;
					this.loading = false;
				});
			},
			// 添加环境
			submitForm() {
				this.$refs.form.validate((valia) => {
					if (valia) {
						addEnv(this.form).then((res) => {
							if (res.code == 200) {
								this.resetForm();
								this.$message.success(res.message);
								this.dialogVisible = false,
								this.getEnv();
							} else {
								this.$message.error(res.message);
								this.getEnv();
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
			// 单选框值 角色改变 重置表单
			rChange() {
				this.resetForm();
				this.form.role = this.role;
			},
			//弹窗点右上角取消按钮
			handleClose(done) {
				this.$confirm('确认关闭？')
					.then(_ => {
						done();
						this.resetForm()
					})
					.catch(_ => {});
			},
			//点击取消按钮
			cancel() {
				this.dialogVisible = false,
					this.resetForm()
			},
		},
		mounted() {
			this.getEnv();
		},
	};
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

	[class^=el-icon-] {
		font-size: x-large;
	}
</style>
