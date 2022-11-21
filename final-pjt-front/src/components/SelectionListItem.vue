<template>
  <div>
    <div class="col">
      <img v-if="randomMovie" :src="movieSrc" class="card-img-top" :alt="randomMovie.title" @click="movieLike">
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SelectionListItem',
  props: {
    randomMovie: Object,
  },
  computed: {
    movieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.randomMovie.poster_path}`
      return movieSrc
    }
  },
  methods: {
    movieLike() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.randomMovie.movie_id}/likes/`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>

</style>