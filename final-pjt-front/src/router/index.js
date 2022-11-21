import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieView from '@/views/MovieView'
import LoginView from '@/views/LoginView'
import DetailView from '@/views/DetailView'
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
    path: '/selection',
    name: 'selection',
    component: SelectionView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/:movie_id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  },
})

export default router

