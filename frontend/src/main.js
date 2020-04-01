// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import router from './router';
import store from './../store/index'
import axios from "./api/";

Vue.config.productionTip = false;
Vue.prototype.$api = axios;

Vue.use(ViewUI);

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store:store,
    components: { App },
    template: '<App/>'
});
