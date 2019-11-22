<template>
	<div class="detail container">
	  <router-link to="/" class="btn btn-default">返回</router-link>
	
	
	   <span class="pull-right">
	         <router-link v-bind:to="'/edit/'+customer.id" class="btn btn-primary">编辑</router-link>
	         <button class="btn btn-danger" v-on:click="deletecut(customer.id)">删除</button>
	   </span>
	  </h1>
	  <ul class="list-group">
	    <li class="list-group-item"><span class="glyphicon glyphicon-plus ">{{team.team_id}}</span></li>
	    <li class="list-group-item"><span class="glyphicon glyphicon-plus ">{{team_name}}</span></li>
	  </ul>
	</div>
</template>

<script>
	export default {
	  name: 'update',
	  data() {
	    return {
	      team: ""
	    }
	  },
	  methods: {
	    fetchCustomer(id) {
	      this.$http.get("http://localhost:3000/user/" + id)
	        .then(function(response) {
	          //console.log(response)
	          this.customer = response.body
	        })
	    },
	    deletecut(id){
	      this.$http.delete("http://localhost:3000/user/" + id)
	        .then(function(response) {
	         
	          this.$route.push({path:"/"});
	        })
	    }
	  },
	  created() {
	    this.fetchCustomer(this.$route.params.id)
	  }
	
	}
</script>

<style>
</style>
