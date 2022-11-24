<template>
  <div>
    <div class="col">
      <router-link :to="{ name: 'detail', params: { movie_id: latestMovie.id } }">
        <img class="card-img-top" style="postiion : relative;" :src="movieSrc" :alt="latestMovie.title">
      </router-link>
      <button class="like-btn fs-4 fw-bold" :id="'like-btn-' + latestMovie.id" v-if="!isLike" @click="movieLike">♡</button>
      <button class="like-btn fs-4 fw-bold" :id="'like-btn-' + latestMovie.id" v-if="isLike" @click="movieLike">♥</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'LatestMovieListItem',
  props: {
    latestMovie: Object,
  },
  data() {
    return {
      userId: this.$store.state.userId,
    }
  },
  computed: {
    isLike() {
      return this.latestMovie.like_users?.includes(this.userId)
    },
    movieSrc() {
    //   console.log(this.latestMovie)
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.latestMovie.poster_path}`
      return movieSrc
    }
  },
  methods: {
    movieLike() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.latestMovie.id}/likes/`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
          const likeBtn = document.querySelector(`#like-btn-${this.latestMovie.id}`)

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
.like-btn {
  display: none;
  position: absolute; 
  color: #00ABB3;
  background-color: transparent;
  border: none;
  top: 75%;
  left: 65%;
}
</style>