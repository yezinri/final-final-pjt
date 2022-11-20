import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieView from '@/views/MovieView'
import LoginView from '@/views/LoginView'
import DetailView from '@/views/DetailView'
import PreferView from '@/views/PreferView'
import SignupView from '@/views/SignupView'
import ProfileView from '@/views/ProfileView'
import SelectionView from '@/views/SelectionView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/prefer',
    name: 'prefer',
    component: PreferView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/selection',
    name: 'selection',
    component: SelectionView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
