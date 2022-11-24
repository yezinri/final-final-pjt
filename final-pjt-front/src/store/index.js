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
    // movies: [],
    reviews: [],
    token: null,
    userId: null,
    userName: null,
    randomMovies: null,
    recommendedMovies: null,
    latestMovies: null,
    searchMovies: null,
    searchWord: null,
    backdropPath: null,
    todayMovie: null,
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
    GET_RECOMMED_MOVIES(state, movies) {
      state.recommendedMovies = movies
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    // 회원가입과 로그인했을 때의 이동페이지가 달라서 아마 이것도 구분해줘야할듯 (11.20 민혁)
    SAVE_TOKEN_SIGNUP(state, token) {
      state.token = token
      // router.push({ name: 'movie' })
      router.push({ name: 'selection' })
    },
    SAVE_TOKEN_LOGIN(state, token) {
      state.token = token
      router.push({ name: 'movie' })
      // router.push({ name: 'selection' })
    },
    DELETE_TOKEN(state) {
      state.token = null
      router.push({ name: 'movie' })
    },
    GET_ID(state, userData) {
      console.log('아이디랑 유저네임 바뀜')
      state.userId = userData.pk
      state.userName = userData.username
    },
    RANDOM_MOVIES(state, randomMovies) {
      // console.log('드디어 랜덤영화왔다..')
      state.randomMovies = randomMovies['random_top_movies']
    },
    GET_LATEST_MOVIES(state, latestMovies) {
      // console.log(latestMovies)
      state.latestMovies = latestMovies
    },
    SEARCH_MOVIE(state, data) {
      state.searchMovies = data[0]
      state.searchWord = data[1]
    },
    CHANGE_BACKGROUND(state, backdrop_path) {
      state.backdropPath = backdrop_path
    },
    TODAY_MOVIE(state, todayMovie) {
      console.log(todayMovie)
      state.todayMovie = todayMovie
    }
  },
  actions: {
    // getMovies(context) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies/`,
    //   })
    //     .then((res) => {
    //       // console.log(res, context)
    //       context.commit('GET_MOVIES', res.data)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    getRecommendMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${context.state.userName}/recommend/`,
      })
        .then((res) => {
          // console.log(res)
          context.commit('GET_RECOMMED_MOVIES', res.data)
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
          context.commit('SAVE_TOKEN_SIGNUP', res.data.key)
        })
        .then(() => {
          // console.log('자동 로그인')
          context.dispatch('getId')
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
          context.commit('SAVE_TOKEN_LOGIN', res.data.key)
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
    },
    randomMovies(context) {
      // console.log('actions')
      axios({
        method: 'get',
        url: `${API_URL}/movies/random_movies/`,
      })
        .then((res) => {
          context.commit('RANDOM_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getLatestMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/latest_movies/`,
      })
        .then((res) => {
          context.commit('GET_LATEST_MOVIES', res.data.random_latest_movies)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getTodayMovie(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/today_movie/`,
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('TODAY_MOVIE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
