<template>
  <div>
    <RecommendMovieList/><br>
    <MovieList v-show="false"/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import RecommendMovieList from '@/components/RecommendMovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList,
    RecommendMovieList,
  },
  created() {
    this.getMovies()
    this.getRecommendMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getRecommendMovies() {
      this.$store.dispatch('getRecommendMovies')
    }
  }
}
</script>

<style>

</style>