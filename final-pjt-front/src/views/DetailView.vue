<template>
  <div>
    <h1>Detail</h1>
    <p v-if="movie">{{ movie.title }}</p>
    <p v-if="movie">{{ movie.overview }}</p>
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
    }
  },
  created() {
    this.getMovieDetail()
    this.getReviews()
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
    }
  }
}
</script>

<style>

</style>