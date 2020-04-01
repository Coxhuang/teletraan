import Vue from 'vue'
import Vuex from 'vuex' // 使用CDN后注释掉

// 告诉 vue “使用” vuex
Vue.use(Vuex); // 使用CDN后注释掉

// 创建一个对象来保存应用启动时的初始状态
// 需要维护的状态
const store = new Vuex.Store({
    state: {
        image:{
            base64_data:[],
            key_data:[],
        }
    },
    mutations:{
        update_current_image_data: (state, value) => {
            console.log("value:",value);
            state.image.base64_data.push(value["ocr_img"]);
            state.image.key_data.push(value["ocr_key"])
        },
    },
    getters: {
        get_current_image_detail: state => {
            return state.image;
        },
    }
});




// 整合初始状态和变更函数，我们就得到了我们所需的 store
// 至此，这个 store 就可以连接到我们的应用中
export default store
