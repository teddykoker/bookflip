<template>
  <div class="container" id="app">
    <h1>bookswitch</h1>
      <router-link v-show="!authenticated" to="/login" ><a>Login</a></router-link>
      <router-link v-show="!authenticated" to="/signup" ><a>Signup</a></router-link>
      <a v-show="authenticated" v-on:click="logout" href="#">Logout</a>
      <ul class="nav nav-tabs">
        <router-link tag="li" to="/buy" active-class="active"><a>Buy</a></router-link>
        <router-link tag="li" to="/sell" active-class="active"><a>Sell</a></router-link>
      </ul>
      <br>
      <router-view></router-view>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'app',
  data: function () {
    return {
      authenticated: false
    }
  },
  methods: {
   checkAuth: function(){
     var self = this;
     axios.get('/api/me').then(function(response) {
       if(response.data.loggedIn){
         self.authenticated = true;
       }
     }).catch(function(error) {
       console.log(error);
     });
   },
   logout: function(){
     var self = this;
     axios.get('/api/logout').then(function(response) {
       if(!response.data.loggedIn){
         self.authenticated = false;
       }
     }).catch(function(error) {
       console.log(error);
     });
   }
  },
  beforeMount: function(){
    this.checkAuth();
  },
}
</script>

