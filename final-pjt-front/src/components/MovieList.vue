<template>
  <div>    
    <div class="row row-cols-1 row-cols-md-3 row-cols-xl-5 g-4">
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
  
</template>

<script>
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  }
  
}
</script>

<style>

</style>