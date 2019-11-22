<template>
	<section>
		<!--工具条-->

		<el-col :span="1" class="grid" style="padding-bottom: 0px;">
			<el-button type="primary" @click="dialogCreateVisible  = true">添加</el-button>
		</el-col>

		<!--列表-->
		<el-table :data="list.slice((page-1)*size,page*size)" highlight-current-row v-loading="loading" style="width: 100%;">
			<el-table-column type="index" :index="indexMethod" label="序号" align="center" sortable>
			</el-table-column>
			<el-table-column prop="permission_name" label="权限名称" align="center">
			</el-table-column>
			<el-table-column label="操作" width="300">
				<template slot-scope="scope">
					<el-button type="primary" size="small" @click="editPermission(scope.row)">编辑</el-button>
					<el-button type="danger" size="small" @click=" delPermission(scope.row) ">删除</el-button>
				</template>
			</el-table-column>
		</el-table>

		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-pagination layout="prev, pager, next" @size-change="handleSizeChange" @current-change="handleCurrentChange"
			 :current-page="page" :page-size="size" :total="total" style="float:right;">
			</el-pagination>
		</el-col>

		<!-- 添加弹出窗 -->
		<el-dialog title="添加权限" :visible.sync="dialogCreateVisible" :close-on-click-modal="false" :close-on-press-escape="false"
		 width="30%" :before-close="handleClose">
			<el-form id="#form" ref="form" :model="form" :rules="rules" label-width="80px">
				<el-form-item label="权限名称" prop="permission_name">
					<el-input v-model="form.permission_name" placeholder="权限名称" clearable></el-input>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="addPermission" :loading="createLoading">添加</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>

		<!-- 编辑弹出窗 -->
		<el-dialog title="编辑" :visible.sync="dialogUpdateVisible" width="50%" :before-close="handleClose"
		 :close-on-click-modal="false" :close-on-press-escape="false">
			<el-form id="#update" ref="update" :model="update" :rules="updateRules" label-width="80px">
				<el-form-item label="权限名称" prop="permission_name">
					<el-input v-model="update.permission_name" placeholder="权限名称" clearable></el-input>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="updatePermission" :loading="updateLoading">确定</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>


	</section>
</template>
<script>
	import {
		getPermissionList,
		updatePermission,
		addPermission,
		deletePermission
	} from '../../api/api';

	export default {
		data() {
			return {
				loading: false,
				status: '',
				list: [],
				page: 1,
				total: 0,
				size: 10,
				form: {
					permission_name: '',
				},
				update: {
					permission_name: '',
				},
				rules: {
					permission_name: [{
						required: false,
						message: '请输入权限名字',
						trigger: 'blur'
					}]
				},
				updateRules: {
					permission_name: [{
						required: false,
						message: '请输入权限名字',
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
			getPermissionList: function() {
				//分页传参
				let para = {
					page: this.page,
					size: this.size,
				};
				this.loading = true;
				getPermissionList(para).then((res) => {
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
			addPermission() {
				this.$refs.form.validate((valid) => {
					if (valid) {
						this.createLoading = true;
						addPermission(this.form).then(res => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.dialogCreateVisible = false;
								this.createLoading = false;
								this.resetForm();
								this.getPermissionList();
							} else {
								this.$message.error(res.message);
								this.getPermissionList();

							}
						})
					}
				});
			},
			//编辑
			editPermission(team) {
				this.update.permission_id = team.permission_id;
				this.update.permission_name = team.permission_name;
				this.dialogUpdateVisible = true;
			},
			// 更新
			updatePermission() {
				this.$refs.update.validate((valid) => {
					if (valid) {
						this.updateLoading = true;
						updatePermission(this.update).then(res => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.dialogUpdateVisible = false;
								this.updateLoading = false;
								this.getPermissionList();
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
			delPermission(team) {
				this.$confirm('此操作将永久删除团队, 是否继续?', '提示', {
					type: 'warning'
				}).then(() => {
					
					deletePermission(team).then(res => {
						if (res.code == 200) {
							this.$message.success(res.message);
							this.getPermissionList();
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
			this.getPermissionList();
		},
	};
</script>


