<template>

  <div class="container">

    <div v-if="movie" class="container">
      <div class="row">
        <img class="col-4" :src="movieSrc" :alt="movie.title">
        <div class="col-8 d-flex align-content-between flex-wrap">
          <h2>{{ movie.title }}</h2>
          <div>
            <button class="btn btn-primary mb-2" style="background-color: #00ABB3; border: #00ABB3;" id="like-btn" v-if="!isLike" @click="movieLike">좋아요</button>
            <button class="btn btn-primary mb-2" style="background-color: #00ABB3; border: #00ABB3;" id="like-btn" v-if="isLike" @click="movieLike">좋아요 취소</button>
            <p>{{ movie.overview }}</p>
          </div>
        </div>
      </div>
    </div><br>

    <hr><br>

    <div class="container">
      <ReviewCreate @createReview="getReviews"/>
      <ReviewList :reviews="reviews" @deleteReview="getReviews"/>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

import ReviewList from '@/components/ReviewList'
import ReviewCreate from '@/components/ReviewCreate'

export default {
  name: 'DetailView',
  components: {
    ReviewList,
    ReviewCreate,
  },
  data() {
    return {
      movie: null,
      reviews: null,
      userId: this.$store.state.userId,
    }
  },
  created() {
    this.getMovieDetail()
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
    },
  }
}
</script>

<style>

</style>