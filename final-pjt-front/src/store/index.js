import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    reviews: [],
    token: null,
    userId: null,
    userName: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'movie' })
    },
    DELETE_TOKEN(state) {
      state.token = null
    },
    GET_ID(state, userData) {
      console.log('아이디랑 유저네임 바뀜')
      state.userId = userData.pk
      state.userName = userData.username
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then((res) => {
          // console.log(res, context)
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getReviews(context, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movie_id}/reviews/`,
      })
        .then((res) => {
          console.log(res.data)
          context.commit('GET_REVIEWS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .then(() => {
          context.dispatch('getId')
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          // console.log(res.data.key)
          context.commit('DELETE_TOKEN', res.data.key)
        })
        
    },
    getId(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
            Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('GET_ID', res.data)
          // this.userId = res.data.pk
        })
        .catch((err) => {
          console.loe(err, 'getId 에러')
        })
    }
  },
  modules: {
  }
})
