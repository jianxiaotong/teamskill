<template>
	<section>
		<!--工具条-->
		<el-col :span="24"  class="toolbar" style="padding-bottom: 0px;">
			<el-button type="primary" @click="dialogVisible = true">添加</el-button>
		</el-col>
		<!--列表-->
		<el-table :data="list"  highlight-current-row v-loading="loading" style="width: 100%;">
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
			<el-table-column prop="hip" label="Hub IP地址" align="center">
			</el-table-column>
			<el-table-column prop="browser" label="浏览器" align="center">
			</el-table-column>
			<el-table-column prop="version" label="版本" align="center">
			</el-table-column>
			<!-- <el-table-column prop="status" label="状态" align="center">
				<template slot-scope="scope">
					<i v-if="scope.row.status == 1" class="el-icon-video-pause" title="启动中"></i>
					<i v-else class="el-icon-video-play" title="已关闭"></i>
				</template>
			</el-table-column> -->
			<el-table-column fixed="right" label="操作" align="center">
				<template slot-scope="scope">
					<el-button type="text" @click="nodeSwitch(scope.row)">
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
		<el-dialog title="添加node" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
			<el-form ref="form" :model="form" :rules="rules" label-width="80px" style="margin:20px;width:60%;min-width:600px;">
				<el-form-item label="环境IP" prop="ip">
					<el-select v-model="form.ip" placeholder="请选择环境IP">
						<el-option v-for="p in ips" :label="p.ip" :value="p.ip">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item label="Hub IP" prop="hip">
					<el-select v-model="form.hip" placeholder="请选择Hub IP">
						<el-option v-for="p in hip" :label="p.ip" :value="p.ip">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item label="浏览器" prop="browsers">
					<el-cascader v-model="form.browsers" :options="options" :props="{ expandTrigger: 'hover' }" placeholder="请选择浏览器"
					 clearable></el-cascader>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button type="primary" @click="addNode">添加</el-button>
				<el-button @click="cancel">取消</el-button>
			</span>
		</el-dialog>
	</section>
</template>

<script>
	import {
		getNodeEnvIps,
		addNode,
		getHubList,
		getNodeList
	} from '../../api/api';
	export default {
		data() {
			return {
				form: {
					ip: '',
					hip: '',
					browsers: [],
					browser: '',
					version: '',
				},
				ips: [],
				hip: [],
				page: 1,
				total: 0,
				size:1,
				loading: false,
				status: '',
				dialogVisible: false,
				list: [],
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
						// disabled: 'true',
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
						message: '请选择环境IP',
						trigger: 'change'
					}],
					hip: [{
						required: true,
						message: '请选择Hub IP',
						trigger: 'change'
					}],
					browsers: [{
						required: true,
						message: '请选择浏览器',
						trigger: 'change'
					}],
				},
			}
		},
		methods: {
			//修改页码，查询数据
			handleCurrentChange(val) {
				this.page = val;
				this.getNode();
			},
			//获取hub列表
			getNode() {
				//分页传参
				let para = {
					page: this.page,
					size: this.size,
				};
				this.loading = true;
				getNodeList(para).then((res) => {
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
			//添加node
			addNode() {
				this.$refs.form.validate((valia) => {
					if (valia) {
						this.form.browser = this.form.browsers[0];
						this.form.version = this.form.browsers[1];
						addNode(this.form).then((res) => {
							if (res.code == 200) {
								this.resetForm();
								this.$message.success(res.message);
								this.dialogVisible = false,
								this.getNode();
							} else {
								this.$message.error(res.message);
								this.getNode();
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
			//操作node
			nodeSwitch(row){
				this.$confirm('此操作将启动该node, 是否继续?', '提示', {
					confirmButtonText: '确定',
					cancelButtonText: '取消',
					type: 'warning'
				}).then(() => {
					if(row.hstatus == 0){
						this.$message.info('先启动hub才能启动该node');
					}else{
						//启动node接口
						this.$message.success('已启动');
					}
				}).catch(() => {
					this.$message.info('已取消启动');
				});
			},
		},
		mounted() {
			this.getNode();
			// 获取未注册的环境ip和注册为node的ip
			getNodeEnvIps().then((res) => {
				this.ips = res.data;
			});
			getHubList().then((res) => {
				this.hip = res.data;
			});
		},
	};
</script>
