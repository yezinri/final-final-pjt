<template>
  <div class="mx-3">
    <!-- <div class="row">
      <h4 class="mb-4">오늘의 영화</h4>
      <img class="col-4 mt-0 g-4" style="height: 10%" :src="movieSrc" :alt="todayMovie.title">
    </div> -->
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