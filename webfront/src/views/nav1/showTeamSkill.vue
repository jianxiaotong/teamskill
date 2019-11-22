<template>
	<section>

		<!--列表-->
			<el-table :data="list.slice((page-1)*size,page*size)" highlight-current-row v-loading="loading" style="width: 100%;">
			<el-table-column type="selection" width="55">
			</el-table-column>
			<el-table-column type="index"  :index="indexMethod" label="序号" align="center" width="100" sortable>
			</el-table-column>
			<el-table-column prop="team_name" label="团队" align="center" width="200" sortable>
			</el-table-column>
			<el-table-column prop="function_name" label="职能"align="center" width="200"  sortable>
			</el-table-column>
			<el-table-column prop="skill_type" label="技能类型" align="center" width="200"  sortable>
			</el-table-column>
			<el-table-column prop="skill_name" label="技能名称" align="center" width="200"  sortable>
			</el-table-column>
			<!-- <el-table-column label="操作" width="200">
				<template scope="scope">
					<el-button size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
					<el-button type="danger" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>
				</template>
			</el-table-column> -->
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
		
	</section>
</template>

<script>
	import {showTeamSkill} from '../../api/api';
	export default {
		data() {
			return {
				loading: false,
				list: [],
				page: 1,
				total: 0,
				size:10,
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
			//获取
			showTeamSkill:function() {
				//分页传参
				let para = {
					page: this.page,
					size: this.size,
				};
				this.loading = true;
				showTeamSkill(para).then((res) => {
					console.log(res.data)
					this.list = res.data;
					this.total= res.data.length;
					this.loading = false;
				});
			},
		},
		mounted:function () {
			this.showTeamSkill();
		} 
	};

</script>

<style scoped>

</style>