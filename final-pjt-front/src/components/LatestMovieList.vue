<template>
  <div class="mx-3">
    <h4 class="mb-4">최신 영화</h4>
    <div class="row row-cols-3 row-cols-xl-6 g-4">
      <LatestMovieListItem
        v-for="latestMovie in latestMovies"
        :key="latestMovie.id"
        :latestMovie="latestMovie"
      />
    </div>
  </div>
</template>

<script>
import LatestMovieListItem from '@/components/LatestMovieListItem'

export default {
  name: 'LatestMovieList',
  components: {
    LatestMovieListItem,
  },
  computed: {
    latestMovies() {
      return this.$store.state.latestMovies
    }
  }
}
</script>

<style>

</style>