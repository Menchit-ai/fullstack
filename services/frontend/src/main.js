import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import Vue from 'vue';

import App from './App.vue';
import router from './router.js';


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://kong:8000/api/';  // the FastAPI backend
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*" // for all requests

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')