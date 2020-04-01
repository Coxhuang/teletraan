import axios from '@/utils/axios'

const api_all = {
    // 获取所有博文列表
    get_article_list_api(params) { // 获取博文列表
        return axios({
            url: '/api/article/blog/list-article/',
            method: 'GET',
            params: params, // {"page":callback_page}
        })
    },
    // get_article_detail_api(id) { // 获取博文详细信息
    //     return axios({
    //         url: '/api/article/blog/detail-article/'+id+'/',
    //         method: 'GET',
    //     })
    // },
    // get_user_detail_api() { // 获取用户详细信息
    //     return axios({
    //         url: '/api/user/blog/detail-user/admin/',
    //         method: 'GET',
    //     })
    // },
    // get_data_detail_api() { // 获取用户data
    //     return axios({
    //         url: '/api/user/blog/detail-data/admin/',
    //         method: 'GET',
    //     })
    // },
};

export default api_all
