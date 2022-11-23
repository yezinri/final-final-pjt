<template>
  <div>
    <h2>{{ todayMovie.title }}</h2>
    <img :src="movieSrc" :alt="todayMovie.title">
  </div>
</template>

<script>
export default {
  name: 'TodayMovie',
  computed: {
    todayMovie() {
      return this.$store.state.todayMovie
    },
    movieSrc() {
    const movieSrc = `https://image.tmdb.org/t/p/original/${this.todayMovie.poster_path}`
    return movieSrc
    },
  },

}
</script>

<style>

</style>