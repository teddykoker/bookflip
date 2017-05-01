import Vue from 'vue'
import VueRouter from 'vue-router'

// Main Web Components
import App from './components/App.vue'
import Feed from './components/Feed.vue'

// Book Buy, Sell and sub pages
import Buy from './components/Buy.vue'
import Sell from './components/Sell.vue'

// Specific pages for user account managment and interface.
import Login from './components/Login.vue'
import Signup from './components/Signup.vue'


Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/', component: Feed},
    { path: '/buy', component: Buy},
    { path: '/sell', component: Sell},
    { path: '/login', component: Login},
    { path: '/signup', component: Signup}
  ]
})

new Vue({ // eslint-disable-line no-new
  el: '#app',
  router,
  render: h => h(App)
})