<template>
  <div>
      <div class="col">
        <router-link :to="{ name: 'detail', params: { movie_id: movie.movie_id } }">
          <img :src="movieSrc" class="card-img-top" :alt="movie.title">
        </router-link>
      </div>

    <!-- <h5>{{ movie.title }}</h5>
    <p>{{ movie.id }}</p>
    <button :id="'like-btn-' + movie.id" v-if="!isLike" @click="movieLike">좋아요</button>
    <button :id="'like-btn-' + movie.id" v-if="isLike" @click="movieLike">좋아요 취소</button>
    <br>
    <router-link :to="{ name: 'detail', params: { id: movie.id } }">
      [DETAIL]
    </router-link>
    <hr> -->

  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  data() {
    return {
      userId: this.$store.state.userId,
    }
  },
  computed: {
    isLike() {
      return this.movie.like_users?.includes(this.userId)
    },
    movieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
      return movieSrc
    }
  },
  methods: {
    movieLike() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie.movie_id}/likes/`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
          const likeBtn = document.querySelector(`#like-btn-${this.movie.movie_id}`)

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