<template>
  <div>
    <div>
      <router-link :to="{ name: 'detail', params: { movie_id: recommendMovie.id } }">
        <img class="card-img-top" style="postiion : relative;" :src="movieSrc" :alt="recommendMovie.title">
      </router-link>
      <button class="like-btn fs-4 fw-bold" :id="'like-btn-' + recommendMovie.id" v-if="!isLike" @click="movieLike">♡</button>
      <button class="like-btn fs-4 fw-bold" :id="'like-btn-' + recommendMovie.id" v-if="isLike" @click="movieLike">♥</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'RecommendMovieListItem',
  props: {
    recommendMovie: Object,
  },
  data() {
    return {
      userId: this.$store.state.userId,
    }
  },
  computed: {
    isLike() {
      return this.recommendMovie.like_users?.includes(this.userId)
    },
    movieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.recommendMovie.poster_path}`
      return movieSrc
    }
  },
  methods: {
    movieLike() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.recommendMovie.id}/likes/`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
          const likeBtn = document.querySelector(`#like-btn-${this.recommendMovie.id}`)

          if (res.data.is_like === true) {
            likeBtn.innerText = '♥'
          } else {
            likeBtn.innerText = '♡'
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