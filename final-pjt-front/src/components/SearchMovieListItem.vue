<template>
  <div>
    <div class="col">
      <router-link :to="{ name: 'detail', params: { movie_id: searchMovie.movie_id } }">
        <img :src="movieSrc" class="card-img-top" :alt="searchMovie.title">
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchMovieListItem',
  props: {
    searchMovie: Object,
  },
  computed: {
    movieSrc() {
    //   console.log(this.latestMovie)
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.searchMovie.poster_path}`
      return movieSrc
    }
  },
}
</script>

<style>

</style>