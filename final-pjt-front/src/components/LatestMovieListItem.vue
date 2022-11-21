<template>
  <div>
    <div class="col">
      <router-link :to="{ name: 'detail', params: { movie_id: latestMovie.id } }">
        <img :src="movieSrc" class="card-img-top" :alt="latestMovie.title">
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LatestMovieListItem',
  props: {
    latestMovie: Object,
  },
  computed: {
    movieSrc() {
    //   console.log(this.latestMovie)
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.latestMovie.poster_path}`
      return movieSrc
    }
  },
}
</script>

<style>

</style>