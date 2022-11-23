<template>
  <div>
    <div>
      <router-link :to="{ name: 'detail', params: { movie_id: recommendMovie.id } }">
        <img :src="movieSrc" class="card-img-top" :alt="recommendMovie.title">
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendMovieListItem',
  props: {
    recommendMovie: Object,
  },
  computed: {
    movieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.recommendMovie.poster_path}`
      return movieSrc
    }
  },
}
</script>

<style>

</style>