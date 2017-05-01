 <template>
  <!-- Main Page Container -->
  <div>

    <!-- Main Header Content -->
    <div class="container-fluid">

      <!-- Header -->
      <div id="header" class="row">   
        <div class="col-md-8 col-md-offset-2 col-xs-12">

          <div class="row">
            <div class="col-md-6 col-xs-8">
              <img id="logoImg" src="/assets/logo.svg"/>
              <h1 id="logoText"> bookflip </h1> 
            </div>

            <div id="accountButtons" class="col-md-6 col-xs-4" v-if="true">
              <div class="row">
                <div class="col-md-6 hidden-sm hidden-xs"> 
                  <router-link to="/login" id="login" class="btn btn-default"> Log In </router-link> 
                </div>
                <div class="col-md-6 hidden-sm hidden-xs"> 
                  <router-link to="/signup" id="signup" class="btn btn-default"> Sign Up </router-link> 
                </div>
                <div class="col-xs-12 hidden-md hidden-lg">
                  <div class="btn-group-verticle" role="group">
                    <router-link to="/login" class="btn btn-default"> Tiny </router-link> 
                    <router-link to="/singup" class="btn btn-default"> Also Tiny </router-link> 
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
        

      <!-- Navigation Bar -->
      <div id="navbar" class="row">
        <div class="col-md-8 col-md-offset-2 col-xs-12">

          <div id="schoolName" class="col-md-9 hidden-sm hidden-xs"> Worcester Polytechnic Institute </div>

          <div id="transaction" class="col-md-3 col-xs-12" v-if="authenticated">
            <router-link to="/buy"> Buy </router-link>
            |
            <router-link to="/sell"> Sell </router-link>
          </div>

          <div id="transaction" class="col-md-3 col-xs-12" v-else-if="!authenticated">
            <router-link to="/buy"> Buy </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Search Bar & Dynamic Content -->
    <div class="container-fluid">

      <div class="row" v-if="true">
        <div class="col-md-8 col-md-offset-2 col-sm-12">
          <!-- Search Bar -->
          <div>
            <input type="text" class="form-control" id="searchBar" placeholder="Search for a book...">
          </div>
        </div>
      </div>

      <div class="row">

        <!-- Dynamicaly Loaded Content -->
        <div class="col-md-8 col-md-offset-2 col-xs-12">
          <router-view></router-view>
        </div>

      </div>
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