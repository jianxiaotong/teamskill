<template>
	<section>
		<!--工具条-->
		<el-col :span="24"  class="toolbar" style="padding-bottom: 0px;">
			<el-button type="primary" @click="dialogVisible = true">添加</el-button>
		</el-col>
		<!--列表-->
		<el-table :data="list" highlight-current-row v-loading="loading" style="width: 100%;">
			<el-table-column type="index" label="序号" align="center" sortable>
			</el-table-column>
			<el-table-column prop="ip" label="IP地址" align="center">
			</el-table-column>
			<!-- <el-table-column prop="status" label="状态" align="center">
				<template slot-scope="scope">
					<i v-if="scope.row.status == 1" class="el-icon-video-pause" title="启动中"></i>
					<i v-else class="el-icon-video-play" title="未启动"></i>
				</template>
			</el-table-column> -->
			<el-table-column fixed="right" label="操作" align="center">
				<template slot-scope="scope">
					<!-- <el-button :type="scope.row.status === 0 ? this.status='启动' : this.status='关闭'" type="text" @click="register(scope.row)">
						{{this.status}}
					</el-button> -->
					<el-button type="text" @click="hubSwitch(scope.row)">
						<i v-if="scope.row.status == 1" class="el-icon-video-pause" title="启动中"></i>
						<i v-else class="el-icon-video-play" title="未启动"></i>
					</el-button>
				</template>
			</el-table-column>
		</el-table>
		
		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="size" :total="total" style="float:right;">
			</el-pagination>
		</el-col>
		
		<!-- 添加弹出窗 -->
		<el-dialog title="添加hub" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
			<el-form ref="form" :model="form" :rules="rules" label-width="80px" style="margin:20px;width:60%;min-width:600px;">
				<el-form-item label="环境IP" prop="ip">
					<el-select v-model="form.ip" placeholder="请选择IP地址">
						<el-option v-for="p in ips" :label="p.ip" :value="p.ip">
						</el-option>
					</el-select>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="addHub">添加</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>
	</section>
</template>

<script>
	import {
		getHubList,
		getEnvIps,
		addHub
	} from '../../api/api';
	export default {
		data() {
			return {
				form: {
					ip: ''
				},
				ips: [],
				loading: false,
				status: '',
				dialogVisible: false,
				list: [],
				page: 1,
				total: 0,
				size:1,
				rules: {
					ip: [{
						required: true,
						message: '请选择IP地址',
						trigger: 'change'
					}],
				},
			}
		},
		methods: {
			//修改页码，查询数据
			handleCurrentChange(val) {
				this.page = val;
				this.getHub();
			},
			//获取hub列表
			getHub() {
				//分页传参
				let para = {
					page: this.page,
					size: this.size,
				};
				this.loading = true;
				getHubList(para).then((res) => {
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
				this.dialogVisible = false,
					this.resetForm()
			},
			//添加hub
			addHub() {
				this.$refs.form.validate((valia) => {
					if (valia) {
						addHub(this.form).then((res) => {
							if (res.code == 200) {
								this.resetForm();
								this.$message.success(res.message);
								this.dialogVisible = false,
									this.getHub();
							} else {
								this.$message.error(res.message);
								this.getHub();
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
			//操作hub
			hubSwitch(row) {
				this.$confirm('此操作将启动该hub, 是否继续?', '提示', {
					confirmButtonText: '确定',
					cancelButtonText: '取消',
					type: 'warning'
				}).then(() => {
					//启动hub接口
					this.$message.success('已启动');
				}).catch(() => {
					this.$message.info('已取消启动');
				});
			},
		},
		mounted() {
			this.getHub();
			// 获取未注册的环境ip
			getEnvIps().then((res) => {
				this.ips = res.data;
			});
		},
	};
</script>
