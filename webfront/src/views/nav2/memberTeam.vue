<template>
	<section>
		<!--工具条-->


		<!--列表-->
		<el-table :data="list.slice((page-1)*size,page*size)" highlight-current-row v-loading="loading" style="width: 100%;">
			<el-table-column type="index" :index="indexMethod" label="序号" align="center" sortable>
			</el-table-column>
			<el-table-column prop="team_name" label="团队" align="center">
			</el-table-column>
			<el-table-column prop="role_name" label="角色" align="center">
			</el-table-column>
		</el-table>

		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-pagination layout="prev, pager, next" @size-change="handleSizeChange" @current-change="handleCurrentChange"
			 :current-page="page" :page-size="size" :total="total" style="float:right;">
			</el-pagination>
		</el-col>

		

		

	</section>
</template>
<script>
	import {
		getAllTeam,
		updateTeam,
		getTeamName,
		addTeam,
		deleteTeam
	} from '../../api/api';

	export default {
		data() {
			return {
				loading: false,
				status: '',
				list: [],
				dialogVisible: false,
				page: 1,
				total: 0,
				size: 10,
				total_rows: 0,
				form: {
					team_name: '',
					team_comment: '',
				},

				update: {
					team_name: '',
					team_comment: '',
					team_id: '',
				},
				rules: {
					team_name: [{
						required: false,
						message: '请输入团队名称',
						trigger: 'blur'
					}, {
						min: 3,
						max: 15,
						message: '长度在 3 到 15 个字符'
					}],
					team_comment: [{
						required: false,
						message: '请输入团队简介',
						trigger: 'blur'
					}, ],
				},
				updateRules: {
					team_name: [{
						required: false,
						message: '请输入团队名称',
						trigger: 'blur'
					}, ],
					team_comment: [{
						required: false,
						message: '请输入团队简介',
						trigger: 'blur'
					}, ],
				},
				dialogCreateVisible: false, //创建对话框的显示状态
				dialogUpdateVisible: false, //编辑对话框的显示状态

				createLoading: false,
				updateLoading: false,
			}
		},
		methods: {
			//修改页码，查询数据
			handleCurrentChange(val) {
				this.page = val;
			},
			//修改页码，查询数据
			handleSizeChange(size) {
				this.size = size;
			},
			indexMethod(index) {
				return (index + 1) + (this.page - 1) * this.size
			},
			
			//获取环境列表
			getAllTeam: function() {
				//分页传参
				let para = {
					page: this.page,
					size: this.size,
				};
				this.loading = true;
				getAllTeam(para).then((res) => {
					console.log(res.data)
					this.list = res.data;
					this.total = res.data.length;
					this.loading = false;
				});
			},
			// 重置表单 
			resetForm() {
				this.$refs.form.resetFields();
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
				this.dialogCreateVisible = false,
				this.dialogUpdateVisible = false,
				this.resetForm()
			},

			//创建
			addTeam() {
				this.$refs.form.validate((valid) => {
					if (valid) {
						this.createLoading = true;
						addTeam(this.form).then(res => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.dialogCreateVisible = false;
								this.createLoading = false;
								this.resetForm();
								this.getAllTeam();
							} else {
								this.$message.error(res.message);
								this.getAllTeam();

							}
						})
					}
				});
			},
			//编辑
			editTeam(team) {
				this.update.team_id = team.team_id;
				this.update.team_name = team.team_name;
				this.update.team_comment = team.team_comment;
				this.dialogUpdateVisible = true;
			},
			// 更新
			updateTeam() {
				this.$refs.update.validate((valid) => {
					if (valid) {
						this.updateLoading = true;
						updateTeam(this.update).then(res => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.dialogUpdateVisible = false;
								this.updateLoading = false;
								this.getAllTeam();
							} else {
								this.$message.error(res.message);
								this.dialogUpdateVisible = false;
								this.updateLoading = false;
							}
						})
					}
				});
			},

			// 删除
			delTeam(team) {
				this.$confirm('此操作将永久删除团队, 是否继续?', '提示', {
					type: 'warning'
				}).then(() => {
					
					deleteTeam(team).then(res => {
						if (res.code == 200) {
							this.$message.success(res.message);
							this.getAllTeam();
						} else {
							this.$message.error(res.message);
						}

					})
				}).catch(() => {
                    this.$message.info('已取消操作!');
                });
			},
		},
		mounted() {
			this.getAllTeam();
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
