import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import index from '@/components/index'
import query from '@/components/query'

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
    }
  ]
})
