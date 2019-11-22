<template>
	<section>
		<!--工具条-->
		<el-col :span="1" class="grid" style="padding-bottom: 0px;">
			<el-button type="primary" @click="dialogCreateVisible  = true">添加</el-button>
		</el-col>
		<!--列表-->
		<el-table :data="list"  highlight-current-row v-loading="loading" style="width: 100%;">
			<el-table-column type="index" :index="indexMethod" label="序号" align="center" sortable>
			</el-table-column>
			<el-table-column prop="team_name" label="团队名称" align="center">
			</el-table-column>
		    <el-table-column prop="function_name" label="职能名称" align="center">
		    </el-table-column>
			<el-table-column prop="function_comment" label="介绍" align="center">
			</el-table-column>
			<el-table-column label="操作" width="300">
				<template slot-scope="scope">
					<el-button type="primary" size="small" @click="editFunction(scope.row)">编辑</el-button>
					<el-button type="danger" size="small" @click=" delFunction(scope.row) ">删除</el-button>
				</template>
			</el-table-column>
		</el-table>
		
		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-pagination 
			layout="prev, pager, next" 
			@size-change="handleSizeChange"
			@current-change="handleCurrentChange"
			:current-page="page"
			:page-size="size" 
			:total="total" 
			style="float:right;">
			</el-pagination>
		</el-col>
		<!-- 添加弹出窗 -->
		<el-dialog title="添加职能" :visible.sync="dialogCreateVisible" :close-on-click-modal="false" :close-on-press-escape="false"
		 width="30%" :before-close="handleClose">
			<el-form id="#form" ref="form" :model="form" :rules="rules" label-width="80px">
				<el-form-item label="团队名称" prop="team_name">
					<el-select v-model="form.team_name" placeholder="选择团队">
						<el-option v-for="p in teamNames" :label="p.team_name" :value="p.team_name">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item label="职能名称" prop="function_name">
					<el-input v-model="form.function_name" placeholder="职能名称" clearable></el-input>
				</el-form-item>
				<el-form-item label="职能介绍" prop="function_comment">
					<el-input v-model="form.function_comment" placeholder="职能介绍" clearable></el-input>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="addFunction" :loading="createLoading">添加</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>
		
		<!-- 编辑弹出窗 -->
		<el-dialog title="编辑" :visible.sync="dialogUpdateVisible" width="50%" :before-close="handleClose"
		 :close-on-click-modal="false" :close-on-press-escape="false">
			<el-form id="#update" ref="update" :model="update" :rules="updateRules" label-width="80px">
				<el-form-item label="团队" prop="team_name">
					<el-select v-model="update.team_name" placeholder="请选择团队">
						<el-option v-for="p in teamNames" :label="p.team_name" :value="p.team_name">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item label="职能名称" prop="function_name">
					<el-input v-model="update.function_name" placeholder="新的团队名" clearable></el-input>
				</el-form-item>
				<el-form-item label="职能介绍" prop="function_comment">
					<el-input v-model="update.function_comment" placeholder="请输入简介" clearable></el-input>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="updateFunction" :loading="updateLoading">确定</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>
		
	</section>
</template>

<script>
	import {
		addFunction,
		getFunctionList,
		getTeamName,
		updateFunction,
		deleteFunction
	} from '../../api/api';
	export default {
		data() {
			return {				
				teamNames:[],
				page: 1,
				total: 0,
				size:10,
				loading: false,
				status: '',
				dialogVisible: false,
				list: [],
				form: {
					team_name:'',
					function_name:'',
					function_comment:'',					
				},
				rules: {
					team_name: [{
						required: true,
						message: '请选择团队',
						trigger: 'change'
					}],
					function_name: [{
						required: true,
						message: '请输入职能名称',
						trigger: 'change'
					}],
					function_comment: [{
						required: false,
						message: '请输入职能介绍',
						trigger: 'change'
					}],
				},
				update: {
					team_name:'',
					function_name:'',
					function_comment:'',
				},
				updateRules: {
					team_name: [{
						required: true,
						message: '请选择团队',
						trigger: 'change'
					}],
					function_name: [{
						required: false,
						message: '请输入职能名称',
						trigger: 'blur'
					}, ],
					function_comment: [{
						required: false,
						message: '请输入职能介绍',
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
			indexMethod(index){
				return (index+1)+(this.page-1)*this.size
			},
			//获取hub列表
			getFunctionList() {
				//分页传参
				let para = {
					page: this.page,
					size: this.size,
				};
				this.loading = true;
				getFunctionList(para).then((res) => {
					this.list = res.data;
					this.total= res.data.length;
					this.loading = false;
				});
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
			// 重置表单
			resetForm() {
				this.$refs.form.resetFields();
			},
			//添加职能
			addFunction() {
				this.$refs.form.validate((valia) => {
					if (valia) {
						this.createLoading = true;
						addFunction(this.form).then((res) => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.dialogCreateVisible = false;
								this.createLoading = false;
								this.resetForm();								
								this.getFunctionList();
							} else {
								this.$message.error(res.message);
								this.getFunctionList();
							}
						})
					} else {
						return false;
					}
				});
			},
		
			//编辑
			editFunction(team) {
				this.update.function_id = team.function_id;
				this.update.team_name = team.team_name;
				this.update.function_name = team.function_name;
				this.update.function_comment = team.function_comment;
				this.dialogUpdateVisible = true;
			},
			// 更新
			updateFunction() {
				this.$refs.update.validate((valid) => {
					if (valid) {
						this.updateLoading = true;
						updateFunction(this.update).then(res => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.dialogUpdateVisible = false;
								this.updateLoading = false;
								this.getFunctionList();
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
			delFunction(team) {
				this.$confirm('此操作将永久删除团队, 是否继续?', '提示', {
					type: 'warning'
				}).then(() => {
					deleteFunction(team).then(res => {
						if (res.code == 200) {						
							this.$message.success( res.message);
							this.getFunctionList();
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
			this.getFunctionList();
			// 获取
			getTeamName().then((res) => {
				this.teamNames = res.data;
			});
		},
	};
</script>
