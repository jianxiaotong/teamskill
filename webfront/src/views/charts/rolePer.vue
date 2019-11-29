<template>
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
                     symbolSize: 60,
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
                             name: '角色权限',
                             children: [
                                 {
									 "name": "普通成员",
									 symbol: 'circle',
									 lineStyle:{
									     color:"red"
									 },
									 children: [
									     {
									         name: '王一',
									         
									         
									         lineStyle:{
									             color:"blue"
									         }
									     },
									     {
									         name: '网二',
									      
									        
									         lineStyle:{
									             color:"blue"
									         }
									     }
									 ]
																						 
                                 },
                                 {
                                     name: '管理员',
                                     symbol: 'circle',
                                    
                                     lineStyle:{
                                         color:"blue"
                                     },
                                     children: [
                                         {
                                             name: '王一',
                                             
                                             
                                             lineStyle:{
                                                 color:"blue"
                                             }
                                         },
                                         {
                                             name: '网二',
                                          
                                            
                                             lineStyle:{
                                                 color:"blue"
                                             }
                                         }
                                     ]
                                 },
                            {
                                name: '创建者',
                                symbol: 'circle',
                               
                                lineStyle:{
                                    color:"blue"
                                },
                                children: [
                                    {
                                        name: '王一',
                                        
                                        
                                        lineStyle:{
                                            color:"blue"
                                        }
                                    },
                                    {
                                        name: '网二',
                                     
                                       
                                        lineStyle:{
                                            color:"blue"
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
 </style>
