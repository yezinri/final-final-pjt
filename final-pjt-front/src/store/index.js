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
    // isLike: null,
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
    // REVIEW_LIKE(state, isLike) {
    //   state.isLike = isLike
    // }
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
          // console.log(res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
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
    // reviewLike(context, payload) {
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/movies/${payload.movie_id}/reviews/${payload.review_id}/likes/`,
    //     headers: {
    //         Authorization: `Token ${ context.state.token }`
    //     }
    //   })
    //     .then((res) => {
    //       // console.log(res.data.is_like)
    //       context.commit('REVIEW_LIKE', res.data.is_like)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // }
  },
  modules: {
  }
})
