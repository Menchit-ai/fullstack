import Vue from 'vue'
import VueRouter from 'vue-router'

import HelloWorld from '@/components/HelloWorld.vue'
import ShowUser from '@/components/ShowUser.vue'
import CreateUser from '@/components/CreateUser.vue'
import CreateText from '@/components/CreateText.vue'
import Quizz from '@/components/Quizz.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HelloWorld
  },
  {
    path: '/suser',
    name: 'Show user',
    component: ShowUser
  },
  {
    path: '/cuser',
    name: 'Create user',
    component: CreateUser
  },
  {
    path: '/ctext',
    name: 'Create text',
    component: CreateText
  },
  {
    path: '/quizz',
    name: 'Quizz',
    component: Quizz
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router