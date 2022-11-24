<template>
    <div :v-if="similarMovie">
      <div>{{ similarMovie.title }}</div>
      <!-- <img :src="movieSrc" :alt="similarMovie.title"> -->
    </div>
</template>

<script>
export default {
  name: 'SimilarMovieListItem',
  props: {
    similarMovie: Array,
  },
  computed: {
    movieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.similarMovie.poster_path}`
      return movieSrc
    }
  },
}
</script>

<style>

</style>