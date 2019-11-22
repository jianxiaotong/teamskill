<template>
	<div>
		 Clicked: {{ getCount }} times
		<el-button :plain="true" @click="open">打开详细</el-button>
		<el-button :plain="true" @click="openVn">打开详细</el-button>
		<el-button :plain="true" @click="changeList" type="warning">添加列表</el-button>
		<div class="mydiv">
			<dl>
				<dt>
				<el-card shadow="always" class="cc" header="header">
				this is a card
			</el-card>
			</dt>
				<dt>
				<el-card shadow="always" class="cc" header="header">
				this is a card
			</el-card>
			</dt>
			</dl>

		</div>
		<div class="mydiv">
			<dl>
				<dt v-on:mouseover="mouseOver(item.id)" @mouseleave="mouseLeave" v-for="item,index in list" :key="item.id">
					<!--
				<el-card shadow="always" class="cc"  :style="{'background-color':(showId==item.id ? '#454217':'')}" v-if="(showTest=='' ? true : (showId==item.id ? false :true))">

                    -->
				<el-card shadow="always" class="cc"  :style="{'background-color':(showId==item.id ? '#454217':'')}" v-if="item.show">
				{{item.msg}}
				<i class="el-icon-edit myi" v-show="showId==item.id" @click="changeItem(index)"></i>
				<i class="el-icon-delete myi"  v-show="showId==item.id" @click="deleteItem(item.id)"></i>
			    </el-card>
			    <div v-else>
			    	<el-input
                type="textarea"
                class="my-text"
                :autosize="{ minRows: 2, maxRows: 4}"
				placeholder="请输入内容"
				v-model="item.msg">{{item.msg}}
				
				</el-input>
				<el-button :plain="true" size="small" @click="item.show=true">save</el-button>
			    </div>
			    
			    
			</dt>
			</dl>
		</div>
	</div>
</template>

<script>
	import { mapGetters } from 'vuex'
	import { mapActions } from 'vuex'
	var ma = new Map();
	var cardlist = [{
		msg: "1111",
		id: "1",
		show: true
	}, {
		msg: "2222",
		id: "2",
		show: true
	}, {
		msg: "33333",
		id: "3",
		show: true
	}, {
		msg: "44444",
		id: "4",
		show: true
	}];
	for(var j = 0, len = cardlist.length; j < len; j++) {
		ma.set(cardlist[j].id, true)
	}
	console.log(ma);

	export default {
		computed: {
			// 使用对象展开运算符将 getters 混入 computed 对象中
			...mapGetters([
				'getCount'
				// ...
			])
		},
		data() {
			return {
				show: true,
				msg: "你好啊个hafdshersghhsdghfhntjhethththrtjngrtjhryhdfssrgwdsghrhhbrhrthrth",
				list: cardlist,
				active: '',
				showId: '',
				showTest: '',
			}
		},
		methods: {
			open() {
				this.show = true;
				//this.$message(this.msg);
			},

			openVn() {
				const h = this.$createElement;
				this.$message({
					message: h('p', null, [
						h('span', null, '内容可以是 '),
						h('i', {
							style: 'color: teal'
						}, 'VNode')
					])
				});
			},
			changeList() {
				this.list = [{
					msg: "dgaadgj",
					id: "1",
					show: true
				}, {
					msg: "dgawhdgj",
					id: "2",
					show: true
				}, {
					msg: "dgawhdgj",
					id: "3",
					show: true
				}, {
					msg: "dgawhdgj",
					id: "4",
					show: true
				}, {
					msg: "dgawhdgj",
					id: "5",
					show: true
				}];
			},
			mouseOver(id) {
				this.showId = id
			},
			mouseLeave() {
				this.showId = '';
			},
			deleteItem(id) {
				this.list = [{
					msg: "dgaadgj",
					id: "1",
					show: true
				}, {
					msg: "dgawhdgj",
					id: "2",
					show: true
				}, {
					msg: "dgawhdgj",
					id: "3",
					show: true
				}];
			},
			changeItem(index) {
				//				map.forEach(function(value, key) {　　　　　　　　　　　　
				//					if(index == key) {
				//						cardlist[index].show = false;
				//					} else {
				//						cardlist[index].show = true;
				//					}　　　　　　　　　
				//				});
				console.log("index " + index);
				cardlist.forEach((value, key, array) => {　　　　　　　　　　　
					if(index == key) {
						cardlist[key].show = false;
					} else {
						cardlist[key].show = true;
					}　　　　　　　　　
				});
				//cardlist[index].show = false;
				console.log(cardlist);
			},
			save() {

			}
		}
	}
</script>

<style scoped lang="scss">
	.my-card {
		width: 300px;
		border: 1px solid #d5d545;
		background-color: #74f12f;
		padding-top: 40px;
		padding-left: 15px;
		border-radius: 5px;
		cursor: pointer;
		word-wrap: break-word;
	}
	
	.cc {
		width: 300px;
		border: 1px solid #d5d545;
		cursor: pointer;
		word-wrap: break-word;
		margin-top: 10px;
		margin-left: 5px;
		height: 100px;
	}
	
	.my-text {
		width: 300px;
		border: 1px solid #d5d545;
		padding-left: 5px;
		padding-top: 30px;
		border-radius: 5px;
	}
	
	.mydiv {
		width: 350px;
		border-radius: 5px;
		background-color: #D5D545;
		margin-top: 30px;
		display: flex;
		float: left;
		margin-left: 10px;
	}
	
	.myi {
		margin-left: 200px;
		color: red;
	}
</style>