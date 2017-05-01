<template>
  <!-- Main Page Container -->
  <div class="container" id="app">

  <!-- Left Hand Side Bar -->
  <div class="col-sm-2">
    <p> this is home </p>
  </div>

  <!-- Main (Center) Content -->
  <div class="col-sm-8">

    <div class="page-header">
      <!-- Header -->
      <div id="header"> 
        <img id="logoImg" src="/assets/logo.svg"/>
        <h1 id="logoText"> bookflip </h1> 
      </div>

      <!-- Navigation Bar -->
      <div id="navbar" class="text-center">

        <span id="schoolName"> WPI </span>

        <span id="transaction" v-if="authenticated">
        <router-link to="/buy"> Buy </router-link>
        |
        <router-link to="/sell"> Sell </router-link>
        </span>

        <span id="transaction" v-else-if="!authenticated">
        <router-link to="/buy"> Buy </router-link>
        </span>

        <span id="account">
        <router-link to="/login"> Login </router-link>
        |
        <router-link to="/signup"> Signup </router-link>
        </span>

      </div>
    </div>

    <!-- Search Bar -->
    <div v-if="true">
        <input type="text" class="form-control" id="searchBar" placeholder="Search for a book...">
    </div>

    <!-- Dynamicaly Loaded Content -->
    <div>
      <router-view></router-view>
    </div>
  </div>

  <!-- Right Hand Sidebar -->
  <div class="col-sm-2">
    <p> this is home </p>
  </div>


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
        if(response.data.status == "LoggedIn"){
          self.authenticated = true;
        }
      }).catch(function(error) {
        console.log(error);
      });
    },
    logout: function(){
      var self = this;
      axios.get('/api/logout').then(function(response) {
        if(response.data.status == "success"){
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