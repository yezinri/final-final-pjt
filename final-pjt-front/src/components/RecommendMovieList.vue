<template>
  <div class="mx-3">
    <h4 class="mb-4">좋아요 기반 추천 영화</h4>
    <div class="hover-container g-4">
      <RecommendMovieListItem
        v-for="recommendMovie in recommendMovies"
        :key="recommendMovie.id"
        :recommendMovie="recommendMovie"
        class="item"
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