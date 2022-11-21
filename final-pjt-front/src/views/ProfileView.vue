<template>
  <div>
    <h2 v-if="userData" style="color: #00ABB3;">{{ userData.username }}</h2><br>
    <LikeMovieList :likeMovies="userData?.like_movies"/><br>
    <MyReviewList :myReviews="userData?.my_reviews" @deleteReview="getProfile"/>
  </div>
</template>

<script>
import axios from 'axios'
import LikeMovieList from '@/components/LikeMovieList'
import MyReviewList from '@/components/MyReviewList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    LikeMovieList,
    MyReviewList,
  },
  data() {
    return {
      userData: null,
    }
  },
  created() {
    this.getProfile()
  },
  methods: {
    getProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$route.params.username}/`
      })
        .then((res) => {
          // console.log(res.data)
          this.userData = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
  
}
</script>

<style>

</style>

