<template>
  <div>
    <h3>좋아요 기반 추천 영화</h3><br>
    <div class="row row-cols-1 row-cols-md-3 row-cols-xl-5 g-4">
      <RecommendMovieListItem
        v-for="recommendMovie in recommendMovies"
        :key="recommendMovie.id"
        :recommendMovie="recommendMovie"
      />
    </div>
  </div>
</template>

<script>
import RecommendMovieListItem from '@/components/RecommendMovieListItem'

export default {
  name: 'RecommendMovieList',
  components: {
    RecommendMovieListItem,
  },
  computed: {
    recommendMovies() {
      return this.$store.state.recommendedMovies.final_movies
    }
  }
}
</script>

<style>

</style>