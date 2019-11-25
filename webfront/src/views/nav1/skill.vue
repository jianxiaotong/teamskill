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
			<el-table-column prop="function_name" label="职能" align="center">
			</el-table-column>
			<el-table-column prop="skill_type" label="技能类型" align="center">
			</el-table-column>
			<el-table-column prop="skill_name" label="技能名称" align="center">
			</el-table-column>
			<el-table-column label="操作" width="300">
				<template slot-scope="scope">
					<el-button type="primary" size="small" @click="editSkill(scope.row)">编辑</el-button>
					<el-button type="danger" size="small" @click=" delSkill(scope.row) ">删除</el-button>
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
		<el-dialog title="添加技能" :visible.sync="dialogCreateVisible" width="30%" :before-close="handleClose">
			<el-form ref="form" :model="form" :rules="rules" label-width="80px">
				<el-form-item label="职能名称" prop="function_name">
					<el-select v-model="form.function_name" placeholder="请选择职能">
						<el-option v-for="p in functionNames" :label="p.function_name" :value="p.function_name">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item label="技能类型" prop="skill_type">
					<el-input v-model.trim="form.skill_type" placeholder="请输入技能类型" clearable></el-input>
				</el-form-item>
				<el-form-item label="技能名称" prop="skill_name">
					<el-input v-model.trim="form.skill_name" placeholder="请输入技能名称" clearable></el-input>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="addSkill">添加</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>
		
		<!-- 编辑弹出窗 -->
		<el-dialog title="编辑" :visible.sync="dialogUpdateVisible" width="50%" :before-close="handleClose"
		 :close-on-click-modal="false" :close-on-press-escape="false">
			<el-form id="#update" ref="update" :model="update" :rules="updateRules" label-width="80px">
				<el-form-item label="职能名称" prop="function_name">
					<el-select v-model="update.function_name" placeholder="请选择职能">
						<el-option v-for="p in functionNames" :label="p.function_name" :value="p.function_name">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item label="技能名称" prop="skill_type">
					<el-input v-model="update.skill_type" placeholder="请输入技能类型" clearable></el-input>
				</el-form-item>
				<el-form-item label="技能类型" prop="skill_name">
					<el-input v-model="update.skill_name" placeholder="请输入技能名称" clearable></el-input>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="updateSkill" :loading="updateLoading">确定</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>
	</section>
</template>

<script>
	import {
		getSkillList,
		getFunctionName,
		addSkill,
		updateSkill,
		deleteSkill
	} from '../../api/api';
	export default {
		data() {
			return {
				functionNames: [],
				loading: false,
				status: '',
				dialogVisible: false,
				list: [],
				page: 1,
				total: 0,
				size:10,
			form: {
				skill_type:'',
				function_name:'',
				skill_name:'',					
			},
			rules: {
				skill_name: [{
					required: false,
					message: '请输入职能名称',
					trigger: 'change'
				}],
				function_name: [{
					required: true,
					message: '请选择职能',
					trigger: 'change'
				}],
				skill_type: [{
					required: false,
					message: '请输入职能介绍',
					trigger: 'change'
				}],
			},
			update: {
				skill_type:'',
				skill_name:'',	
				function_name:'',
			},
			updateRules: {
				skill_name: [{
					required: false,
					message: '请输入职能名称',
					trigger: 'change'
				}],
				skill_type: [{
					required: false,
					message: '请输入职能介绍',
					trigger: 'change'
				}],
				function_name: [{
					required: true,
					message: '请选择职能',
					trigger: 'change'
				}],
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
				//this.getSkillList();
			},
			//修改页码，查询数据
			handleSizeChange(size) {
				this.size = size;
			},
			indexMethod(index){
				return (index+1)+(this.page-1)*this.size
			},
			//获取技能列表
			getSkillList() {
				//分页传参
				let para = {
					page: this.page,
					size: this.size,
				};
				this.loading = true;
				getSkillList(para).then((res) => {
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
			//添加
			addSkill() {
				this.$refs.form.validate((valia) => {
					if (valia) {
						addSkill(this.form).then((res) => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.dialogCreateVisible = false;
								this.createLoading = false;
								this.resetForm();								
								this.getSkillList();
							} else {
								this.$message.error(res.message);
								this.getSkillList();
							}
						})
					} else {
						return false;
					}
				});
			},
			// 重置表单 
			resetForm() {
				this.$refs.form.resetFields();
			},
			//编辑
			editSkill(team) {
				this.update.skill_id = team.skill_id;
				this.update.function_name = team.function_name;				
				this.update.skill_name = team.skill_name;
				this.update.skill_type = team.skill_type;
				this.dialogUpdateVisible = true;
			},
			// 更新
			updateSkill() {
				this.$refs.update.validate((valid) => {
					if (valid) {
						this.updateLoading = true;
						updateSkill(this.update).then(res => {
							if (res.code == 200) {
								this.$message.success(res.message);
								this.dialogUpdateVisible = false;
								this.updateLoading = false;
								this.getSkillList();
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
			delSkill(team) {
				this.$confirm('此操作将永久删除团队, 是否继续?', '提示', {
					type: 'warning'
				}).then(() => {
					deleteSkill(team).then(res => {
						if (res.code == 200) {						
							this.$message.success( res.message);
							this.getSkillList();
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
			this.getSkillList();
			// 获取职能名称
			getFunctionName().then((res) => {
				this.functionNames = res.data;
			});
		},
	};
</script>
