<template>

  <div class="container-lg" style="height: 100%;">


    <div v-if="movie" class="container-lg" style="height: 100%;">
      <div class="row">
        <img class="col-4" :src="movieSrc" :alt="movie.title">
        <div class="col-8 d-flex flex-column">
          <div>
            <h1>{{ movie.title }}</h1>
            <p class="fw-lighter">{{ movie.release_date }}</p>
            <p class="fw-lighter">평점★ {{ movie.vote_average }}</p>
            <span v-for="genre in movie.genre_ids" :key="genre">
              {{ genres[genre] }}
            </span>
          </div>
          <div class="mt-auto">
            <button class="btn btn-primary mb-2" style="background-color: #00ABB3; border: #00ABB3;" id="like-btn" v-if="!isLike" @click="movieLike">좋아요</button>
            <button class="btn btn-primary mb-2" style="background-color: #00ABB3; border: #00ABB3;" id="like-btn" v-if="isLike" @click="movieLike">좋아요 취소</button>
            <p class="mb-0 fw-lighter">{{ movie.overview }}</p>
          </div>
        </div>
      </div>
    </div><br>

    <hr><br>

    <div class="container-lg">

      <SimilarMovieList :similarMovies="similarMovies"/><br><br>
      <ReviewCreate @createReview="getReviews"/>
      <ReviewList :reviews="reviews" @deleteReview="getReviews" @updateReview="getReviews"/><br>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

import ReviewList from '@/components/ReviewList'
import ReviewCreate from '@/components/ReviewCreate'
import SimilarMovieList from '@/components/SimilarMovieList'

export default {
  name: 'DetailView',
  components: {
    ReviewList,
    ReviewCreate,
    SimilarMovieList,
  },
  data() {
    return {
      movie: null,
      reviews: null,
      userId: this.$store.state.userId,
      genres: {
        28: "액션",
        12: "모험",
        16: "애니메이션",
        35: "코미디",
        80: "범죄",
        99: "다큐멘터리",
        18: "드라마",
        10751: "가족",
        14: "판타지",
        36: "역사",
        27: "공포",
        10402: "음악",
        9648: "미스터리",
        10749: "로맨스",
        878: "SF",
        10770: "TV 영화",
        53: "스릴러",
        10752: "전쟁",
        37: "서부"
      },
      similarMovies: null,
    }
  },
  created() {
    this.getMovieDetail()
    this.getSimilarMovies()
    this.getReviews()

  },
  computed: {
    isLike: {
      get() {
        return this.movie?.like_users?.includes(this.userId)
      },
      set() {

      }
    },
    movieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
      return movieSrc
    },
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}`,
      })
        .then((res) => {
          // console.log(res.data)
          this.movie = res.data
        })
        .then(() => {
          this.$store.commit('CHANGE_BACKGROUND', this.movie.backdrop_path)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getReviews() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/reviews/`,
      })
        .then((res) => {
          // console.log(res.data)
          this.reviews = res.data
        })
        .catch((err) => {
          if (err.response.status === 404) {
            this.reviews = null
          }
        })
    },
    movieLike() {
      if (this.isLogin) {

        axios({
          method: 'post',
          url: `${API_URL}/movies/${this.$route.params.movie_id}/likes/`,
          headers: {
              Authorization: `Token ${ this.$store.state.token }`
          }
        })
          .then((res) => {
            console.log(res)
            const likeBtn = document.querySelector('#like-btn')
  
            if (res.data.is_like === true) {
              likeBtn.innerText = '좋아요 취소'
            } else {
              likeBtn.innerText = '좋아요'
            }
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'login' })
      }
    },
    getSimilarMovies() {    // 11.23 민혁 추가
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/similar_movies/`,
      })
        .then((res) => {
          console.log(res.data)
          this.similarMovies = res.data.random_similar_movies
        })
        .catch((err) => {
          if (err.response.status === 404) {
            this.similarMovies = null
          }
        })
    },

  }
}
</script>

<style>

</style>