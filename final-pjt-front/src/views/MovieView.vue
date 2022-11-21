<template>
  <div>
    <RecommendMovieList v-if="isLogin"/><br><br>
    <LatestMovieList/><br>
    <MovieList v-show="false"/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import RecommendMovieList from '@/components/RecommendMovieList'
import LatestMovieList from '@/components/LatestMovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList,
    RecommendMovieList,
    LatestMovieList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovies()
    this.getRecommendMovies()
    this.getLatestMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getRecommendMovies() {
      this.$store.dispatch('getRecommendMovies')
    },
    getLatestMovies() {
      this.$store.dispatch('getLatestMovies')
    }
  }
}
</script>

<style>

</style>