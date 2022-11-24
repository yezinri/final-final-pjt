<template>
  <div>
    <div class="col">
      <!-- <div :class="{selected-movie: is_like }"> -->
        <img
          v-if="randomMovie"
          :class="[{ 'selected-movie': is_like }, { 'card-img-top': true }]"
          :alt="randomMovie.title"
          :src="movieSrc" 
          @click="movieLike">
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SelectionListItem',
  data() {
    return {
      is_like: false,
    }
  },
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
          this.is_like = res.data.is_like
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>
.selected-movie {
  box-shadow: 0px 0px 50px 1px #fff;
  overflow: hidden;
}

.card-img-top {
  transition: transform 500ms;
}

.card-img-top:hover,  
.card-img-top:focus{
  transform: scale(1.2);
  z-index: 1;
}

/* .gallery {
  transition: 0.3s;
}
.gallery a:hover img, .gallery a:focus img{
  transform: scale(1.2);
} */
</style>