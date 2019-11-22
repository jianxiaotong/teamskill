<template>
	<div :class="className" :id="id" :style="{height:height,width:width}" ref="myEchart">
	</div>
</template>

<script>
	import echarts from 'echarts'
	// import  '../../common/js/echarts.all'
	export default {
		props: {
			className: {
				type: String,
				default: 'yourClassName'
			},
			id: {
				type: String,
				default: 'yourID'
			},
			width: {
				type: String,
				default: '800px'
			},
			height: {
				type: String,
				default: '800px'
			}
		},
		data() {
			return {
				chart: null
			}
		},
		mounted() {
			this.initChart();
		},
		beforeDestroy() {
			if (!this.chart) {
				return
			}
			this.chart.dispose();
			this.chart = null;
		},
		methods: {
			initChart() {
				this.chart = echarts.init(this.$refs.myEchart);
				// 把配置和数据放这里
				let app = {};
				let option = null;
				this.chart.showLoading();
				this.chart.hideLoading();
				let data = {
					"name": "工程服务团队",
					"children": [{
							"name": "管理",
							"children": [{
									"name": "敏捷开发",
									"children": [{
										"name": "scrum",
								
									}, ]
								},
								{
									"name": "原型",
									"children": [{
										"name": "Axure",
										
									}, ]
								},
								{
									"name": "用户故事地图",
								},
								{
									"name": "看板",
								},
							]
						},
						{
							"name": "测试",
							"children": [{
									"name": "Easing",
									
								},
								{
									"name": "FunctionSequence",
									
								},
								{
									"name": "interpolate",
									"children": [{
											"name": "ArrayInterpolator",
											
										},
										{
											"name": "ColorInterpolator",
										
										},
										{
											"name": "DateInterpolator",
											
										},

										{
											"name": "RectangleInterpolator",
											
										}
									]
								},
								{
									"name": "ISchedulable",
									
								},
								{
									"name": "Parallel",
									
								},
								{
									"name": "TransitionEvent",
									
								},
								{
									"name": "Tween",
									
								}
							]
						},
						{
							"name": "前端",
							"children": [{
									"name": "converters",
									"children": [{
											"name": "Converters",

										},
										{
											"name": "DelimitedTextConverter",
							
										},
										{
											"name": "GraphMLConverter",
											
										},
										{
											"name": "IDataConverter",

										},
										{
											"name": "JSONConverter",
									
										}
									]
								},
								{
									"name": "DataField",
								
								},
								{
									"name": "DataSchema",
									
								},
								{
									"name": "DataSet",
									
								},
								{
									"name": "DataSource",
								
								},
								{
									"name": "DataTable",
									
								},
								{
									"name": "DataUtil",
									
								}
							]
						},
						{
							"name": "后端",
							"children": [{
									"name": "DirtySprite",
								
								},
								{
									"name": "LineSprite",
									
								},
								{
									"name": "RectSprite",
								
								},
								{
									"name": "TextSprite",
								
								}
							]
						},
						{
							"name": "运维",
							"children": [{
								"name": "FlareVis",
							
							}]
						},



					]
				};
				echarts.util.each(data.children, function(datum, index) {
					index % 2 === 0 && (datum.collapsed = true);
				});
				this.chart.setOption({
					tooltip: {//提示框组件
						trigger: 'item',//触发类型
						triggerOn: 'mousemove'//触发条件
					},
					series: [{
						type: 'tree',
						data: [data],
						//排列方式，横向、纵向
						orient: 'vertical',
						left: '2%',
						right: '2%',
						top: '2%',
						bottom: '12%',
						symbolSize: 8,//标记的大小
						label: {//每个节点的样式
							normal: {
								position: 'left',
								verticalAlign: 'middle',
								align: 'right',
								fontSize: 12
							}
						},

						leaves: {
							label: {//叶子结点的特殊配置
								normal: {
									position: 'bottom',
									verticalAlign: 'middle',
									align: 'center'
								}
							}
						},
                        initialTreeDepth:2,
						expandAndCollapse: true,//子树折叠和展开的交互，默认打开
						animationDuration: 550,
						animationDurationUpdate: 750
					}]

				});
				if (option && typeof option === "object") {
					this.chart.setOption(option, true);
				}
			}
		}
	}
</script>

<style>
</style>



<!-- <template>
     <div>
         <div id="tree" ref="myEchart"></div>
     </div>
 </template>
 <script>
	 import echarts from 'echarts'
 export default {
     data(){
         return{
  
         }
     },
     mounted(){
         this.tree();
     },
     methods:{
         tree(){
             //let tr = this.$echarts.init(document.getElementById("tree"));
			 this.chart = echarts.init(this.$refs.myEchart);
             this.chart.setOption({
                 title : {
                     show:false
                 },
                 calculable : false,
                 series : [{
                     name:'树图',
                     type:'tree',
                     //排列方式，横向、纵向
                     orient: 'vertical', 
                     left: '2%',
                     right: '2%',
                     top: '12%',
                     bottom: '12%',
                     //连接线长度
                     layerPadding: 30,
                     //结点间距
                     nodePadding: 20,
                     //图形形状
                     symbol: 'circle',
                     //尺寸大小
                     symbolSize: 40,
                     label:{
                         normal:{
                             show:true,
                             formatter:function(param){
                                 if(param.name=="工程服务"){
                                     return ''
                                 }else{
                                     return param.name
                                 }
                             },
                         },
                         emphasis:{
                             show:false,
                         }
                     },
                     leaves: {//最底部文字样式
                         label: {
                             normal: {
                                 position: 'bottom',
                                 rotate: -90,
                                 verticalAlign: 'middle',
                                 align: 'left',
                                 show:false
                             },
                             emphasis:{
                                 show:false
                             }
                         }
                     },
                     lineStyle:{//正常情况显示
                         color: 'red',
                         width: 1,
                     },
                     data: [
                         {
                             name: '工程服务',
                             //图片大小
                             symbolSize: [50, 50],
                             //自定义图片
                             symbol: 'image://https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg',
                             children: [
                                 {
									 "name": "管理",
									 symbol: 'circle',
									 lineStyle:{
									     color:"red"
									 },
									 symbolSize: [60, 60],
									 "children": [
										 {						
											name: '敏捷开发',
									 		"children": [{
									 				"name": "scrum",
									 			},
									 		]
									 	},
									 	{
									 		"name": "原型",
									 		"children": [{
									 				"name": "Axure",
									 			},
									 		]
									 	},
									 	{
									 		"name": "用户故事地图",
									 	},
									 	{
									 		"name": "看板",
									 	},
									 ]

                                 },
                                 {
                                     name: '测试',
                                     symbol: 'circle',
                                     symbolSize: [60, 60],
                                     lineStyle:{
                                         color:"blue"
                                     },
                                     children: [
                                         {
                                             name: '王一',
                                             symbol: 'image://https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
                                             symbolSize: [60, 80],
                                             lineStyle:{
                                                 color:"blue"
                                             }
                                         },
                                         {
                                             name: '网二',
                                             symbol: 'image://https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
                                             symbolSize: [60, 80],
                                             lineStyle:{
                                                 color:"blue"
                                             }
                                         }
                                     ]
                                 },
                                 {
                                     name: '前端',
                                     symbol: 'circle',
                                     symbolSize: [60, 60],
                                     lineStyle:{
                                         color:"#aaa"
                                     },
                                     children: [
                                         {
                                             name: '六大',
                                             symbol: 'image://https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
                                             symbolSize: [60, 80],
                                             lineStyle:{
                                                 color:"#aaa"
                                             }
                                         },
                                         {
                                             name: '六二',
                                             symbol: 'image://https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg',
                                             symbolSize: [60, 80],
                                             lineStyle:{
                                                 color:"#aaa"
                                             }
                                         }
                                     ]
                                 },
                                 {
                                     name: '后端',
                                     symbol: 'circle',
                                     symbolSize: [60, 60],
                                     lineStyle:{
                                         color:"green"
                                     },
                                     children: [
                                         {
                                             name: '张一',
                                             symbol: 'image://https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
                                             symbolSize: [60, 80],
                                             lineStyle:{
                                                 color:"green"
                                             }
                                         },
                                         {
                                             name: '张二',
                                             symbol: 'image://https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
                                             symbolSize: [60, 80],
                                             lineStyle:{
                                                 color:"green"
                                             }
                                         }
                                     ]
                                 },
								 {
								     name: '运维',
								     symbol: 'circle',
								     symbolSize: [60, 60],
								     lineStyle:{
								         color:"green"
								     },
								     children: [
								         {
								             name: '张一',
								             symbol: 'image://https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
								             symbolSize: [60, 80],
								             lineStyle:{
								                 color:"green"
								             }
								         },
								         {
								             name: '张二',
								             symbol: 'image://https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
								             symbolSize: [60, 80],
								             lineStyle:{
								                 color:"green"
								             }
								         }
								     ]
								 },
                             ]
                         }
                     ]
                 }]
             })
         }
     }
 }
 </script>
 <style scoped>
    #tree{
        display:inline-block;
        width:900px;
        height:460px;
        background-color:#1d273e;
    }
 </style> -->
