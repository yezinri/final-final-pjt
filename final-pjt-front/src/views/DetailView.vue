<template>
  <div>
    <h1>Detail</h1>
    <p v-if="movie">{{ movie.title }}</p>
    <p v-if="movie">{{ movie.overview }}</p>
    <button id="like-btn" v-if="!isLike" @click="movieLike">좋아요</button>
    <button id="like-btn" v-if="isLike" @click="movieLike">좋아요 취소</button>
    <hr>
    <ReviewCreate @createReview="getReviews"/>
    <ReviewList :reviews="reviews" @deleteReview="getReviews"/>
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
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}`,
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
        url: `${API_URL}/movies/${this.$route.params.id}/reviews/`,
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
        url: `${API_URL}/movies/${this.$route.params.id}/likes/`,
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