import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import index from '@/components/index'
import query from '@/components/query'
import send_sms from '@/components/send_sms'
import group from '@/components/group'
Vue.use(Router)

export default new Router({
  routes: [
//    {
//      path: '/',
//      name: 'HelloWorld',
//      component: HelloWorld
//    },
    {
      path: '/index',
      name: 'index',
      component: index
    },
    {
      path: '/query',
      name: 'query',
      component: query
    },
    {
      path: '/send_sms',
      name: 'send_sms',
      component: send_sms
    },
    {
      path: '/group',
      name: 'group',
      component: group
    }
  ]
})
