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
              <img id="logoImg" class="hidden-sm hidden-xs" src="/assets/logo.svg"/>
              <h1 id="logoText" class="hidden-sm hidden-xs"> bookflip </h1> 

              <img id="logoImgSmall" class="hidden-md hidden-lg" sr="/assets/logo.svg"/>
              <h1 id="logoTextSmall" class="hidden-md hidden-lg"> bookflip </h1>
            </div>

            <div class="col-md-6 col-xs-4" v-if="true">
              <div class="row">
                <div class="col-lg-12 hidden-sm hidden-xs hidden-md"> 
                  <div class="btn-group accountBtn" role="group">
                    <router-link to="/login" class="btn btn-default"> Log In </router-link>
                    <router-link to="/signup" class="btn btn-default"> Sign Up </router-link>
                  </div>
                </div>
                <div class="col-xs-12 hidden-lg">
                  <div class="btn-group-vertical accountBtn" role="group">
                    <router-link to="/login" class="btn btn-default"> Log In </router-link> 
                    <router-link to="/signup" class="btn btn-default"> Sign Up </router-link> 
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
          <div id="schoolName" class="col-xs-4 hidden-md hidden-lg"> WPI </div>

          <div id="transaction" class="col-md-3 col-xs-8" v-if="authenticated">
            <router-link to="/buy"> Buy </router-link>
            |
            <router-link to="/sell"> Sell </router-link>
          </div>

          <div id="transaction" class="col-md-3 col-xs-8" v-else-if="!authenticated">
            <router-link to="/buy"> Buy </router-link>
            |
            <router-link to="/sell"> Sell </router-link>
          </div>

        </div>
      </div>
    </div>

    <!-- Dynamic Content -->
    <div class="container-fluid">
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