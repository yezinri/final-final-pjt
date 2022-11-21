<template>
  <div>
    <div class="col">
      <router-link :to="{ name: 'detail', params: { movie_id: likeMovie.movie_id } }">
        <img :src="movieSrc" class="card-img-top" :alt="likeMovie.title">
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikeMovieListItem',
  props: {
    likeMovie: Object,
  },
  computed: {
    movieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.likeMovie.poster_path}`
      return movieSrc
    }
  },
}
</script>

<style>

</style>